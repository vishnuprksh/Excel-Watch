# Graph Report - Excel-Watch  (2026-08-18)

## Corpus Check
- Corpus is ~17,497 words - fits in a single context window. You may not need a graph.

## Summary
- 35 nodes · 70 edges · 7 communities (5 shown, 2 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Completed Data Flow
- Column Alias Tests
- Outstanding Data Flow
- Brand Identity
- Package Initialization
- Project Documentation

## God Nodes (most connected - your core abstractions)
1. `render()` - 10 edges
2. `find_columns()` - 9 edges
3. `render()` - 8 edges
4. `read_input_file()` - 5 edges
5. `dataframe_to_csv()` - 5 edges
6. `clean_text_series()` - 5 edges
7. `select_filter()` - 5 edges
8. `clean_text()` - 4 edges
9. `unique_options()` - 4 edges
10. `prepare_data()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `render()` --calls--> `find_columns()`  [EXTRACTED]
  excel_watch/completed.py → excel_watch/common.py
- `render()` --calls--> `find_columns()`  [EXTRACTED]
  excel_watch/outstanding.py → excel_watch/common.py
- `render()` --calls--> `read_input_file()`  [EXTRACTED]
  excel_watch/completed.py → excel_watch/common.py
- `render()` --calls--> `dataframe_to_csv()`  [EXTRACTED]
  excel_watch/completed.py → excel_watch/common.py
- `render()` --calls--> `select_filter()`  [EXTRACTED]
  excel_watch/completed.py → excel_watch/common.py

## Import Cycles
- None detected.

## Communities (7 total, 2 thin omitted)

### Community 0 - "Completed Data Flow"
Cohesion: 0.42
Nodes (9): clean_text(), clean_text_series(), unique_options(), build_output(), extract_name(), filter_if_selected(), prepare_data(), render() (+1 more)

### Community 1 - "Column Alias Tests"
Cohesion: 0.39
Nodes (4): find_columns(), normalize_column_name(), CompletedColumnAliasesTest, OutstandingColumnAliasesTest

### Community 2 - "Outstanding Data Flow"
Cohesion: 0.46
Nodes (7): dataframe_to_csv(), read_input_file(), select_filter(), build_summary(), month_options(), prepare_data(), render()

### Community 4 - "Brand Identity"
Cohesion: 0.67
Nodes (3): INVOICEWATCH wordmark, Lime green and dark navy color contrast, InvoiceWatch logo

## Knowledge Gaps
- **3 isolated node(s):** `Excelwatch`, `InvoiceWatch logo`, `Lime green and dark navy color contrast`
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `find_columns()` connect `Column Alias Tests` to `Completed Data Flow`, `Outstanding Data Flow`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Why does `render()` connect `Completed Data Flow` to `Column Alias Tests`, `Outstanding Data Flow`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Why does `render()` connect `Outstanding Data Flow` to `Column Alias Tests`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **What connects `Excelwatch`, `InvoiceWatch logo`, `Lime green and dark navy color contrast` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._