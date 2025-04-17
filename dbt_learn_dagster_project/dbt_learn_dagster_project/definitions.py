import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets import dbtlearn_dbt_assets
from .constants import dbt_project_dir
from .schedules import schedules

defs = Definitions(                                                     # Definitions object in Dagster. This is what Dagster will look at. Everything defined in this object is picked up by Dagster. 
    assets=[dbtlearn_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),  # DbtCliResource sets up dbt plugin and my dbt project dir = dbt_project_dir
    },
)