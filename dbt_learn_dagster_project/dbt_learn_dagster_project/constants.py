import os
from pathlib import Path

from dagster_dbt import DbtCliResource

dbt_project_dir = Path(__file__).joinpath("..", "..", "..", "dbtlearn").resolve()   # relative folder pointer: dbt_project_dir is defined as the parent (..) of the parent of the parent and then the dbtlearn folder
dbt = DbtCliResource(project_dir=os.fspath(dbt_project_dir))

# If DAGSTER_DBT_PARSE_PROJECT_ON_LOAD is set, a manifest will be created at run time.
# Otherwise, we expect a manifest to be present in the project's target directory.
if os.getenv("DAGSTER_DBT_PARSE_PROJECT_ON_LOAD"):  # if DAGSTER_DBT_PARSE_PROJECT_ON_LOAD is enabled (command "DAGSTER_DBT_PARSE_PROJECT_ON_LOAD=1 dagster dev")...
    dbt_manifest_path = (
        dbt.cli(
            ["--quiet", "parse"],                   # ... then execute from the dbt cli the parse command. parse command in dbt re-read model defintions, tests, macros etc and create a so called manifest.json...
            target_path=Path("target"),
        )
        .wait()
        .target_path.joinpath("manifest.json")      # ... to be found in ..\dbtlearn\target\manifest.json
    )
else:
    dbt_manifest_path = dbt_project_dir.joinpath("target", "manifest.json")