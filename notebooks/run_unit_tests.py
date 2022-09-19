# Databricks notebook source
# MAGIC %md 
# MAGIC # Test runner for `pytest`

# COMMAND ----------

!cp ../requirements.txt ~/.
%pip install -r ~/requirements.txt
%pip install /dbfs/fjakobs/pytest_notebook_reporter-0.1.0-py3-none-any.whl

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC pytest.main runs our tests directly in the notebook environment, providing
# MAGIC fidelity for Spark and other configuration variables.
# MAGIC 
# MAGIC A limitation of this approach is that changes to the test will be
# MAGIC cache by Python's import caching mechanism.
# MAGIC To iterate on tests during development, we restart the Python process 
# MAGIC and thus clear the import cache to pick up changes

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import pytest
import os
import sys
import pytest_notebook_reporter

# Run all tests in the repository root.
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
repo_root = os.path.dirname(os.path.dirname(notebook_path))
os.chdir(f'/Workspace/{repo_root}')

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

retcode = pytest.main([".", "-p", "no:cacheprovider", "-qq", "--no-summary", "-o", "console_output_style=classic"], plugins=[pytest_notebook_reporter])

# Fail the cell execution if we have any test failures.
assert retcode == 0, 'The pytest invocation failed. See the log above for details.'

# COMMAND ----------


