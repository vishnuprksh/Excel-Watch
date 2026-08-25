# Excel Watch

Excel Watch is a Streamlit app for filtering invoice exports and downloading
the resulting reports.

## Run locally

Create and activate a Python virtual environment, then install the app's
dependencies:

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

The local app opens at `http://localhost:8501`.

## Deploy with Databricks Apps

The repository includes the two files Databricks needs:

- `requirements.txt` installs the same Python packages used locally.
- `app.yaml` starts the Streamlit app. Databricks supplies the cloud host and
  port automatically.

To deploy from Git:

1. Push this repository to your Git provider.
2. In your Databricks workspace, open **Apps** and create a custom app.
3. In **Configure Git**, enter the repository URL and choose a branch, tag, or
   commit.
4. If the repository is private, configure a Git credential when Databricks
   prompts for one.
5. Choose **Deploy**, then **From Git**.

No Databricks-specific code is required in the application. Continue developing
and testing locally as usual. Deploy the branch again when you want a change in
Databricks, or enable **Auto deploy on push events** for a chosen branch if that
workflow is more convenient.

## Test

```powershell
python -m unittest discover -s tests -v
```
