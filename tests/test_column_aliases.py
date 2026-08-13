import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from excel_watch import completed, outstanding
from excel_watch.common import find_columns


class CompletedColumnAliasesTest(unittest.TestCase):
    def test_old_and_new_column_names_prepare_identical_data(self):
        old_input = pd.DataFrame(
            {
                "Customer": ["Acme"],
                "Sub Customer": ["North"],
                "Invoice #": ["INV-1"],
                "Invoice Date": ["2026-08-01"],
                "Type": ["Standard"],
                "Subscription": ["Annual"],
                "Total": [125.0],
                "Created": ["User • Alice"],
                "Sent": ["User • Bob"],
            }
        )
        new_input = old_input.rename(
            columns={
                "Type": "Invoice Type",
                "Subscription": "Subscription Type",
                "Created": "CreatedBy",
                "Sent": "MarkedAsSentBy",
            }
        )

        old_columns, old_missing = find_columns(old_input, completed.EXPECTED_COLUMNS)
        new_columns, new_missing = find_columns(new_input, completed.EXPECTED_COLUMNS)

        self.assertEqual(old_missing, [])
        self.assertEqual(new_missing, [])
        assert_frame_equal(
            completed.prepare_data(old_input, old_columns),
            completed.prepare_data(new_input, new_columns),
        )


class OutstandingColumnAliasesTest(unittest.TestCase):
    def test_old_and_new_total_names_prepare_identical_data(self):
        old_input = pd.DataFrame(
            {
                "Customer": ["Acme"],
                "Invoice Date": ["2026-08-01"],
                "Total": [125.0],
            }
        )
        new_input = old_input.rename(columns={"Total": "Total USD"})

        old_columns, old_missing = find_columns(old_input, outstanding.REQUIRED_COLUMNS)
        new_columns, new_missing = find_columns(new_input, outstanding.REQUIRED_COLUMNS)

        self.assertEqual(old_missing, [])
        self.assertEqual(new_missing, [])
        assert_frame_equal(
            outstanding.prepare_data(old_input, old_columns),
            outstanding.prepare_data(new_input, new_columns),
        )


if __name__ == "__main__":
    unittest.main()
