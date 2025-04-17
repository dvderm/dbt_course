"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""
from dagster_dbt import build_schedule_from_dbt_selection

from .assets import dbtlearn_dbt_assets

schedules = [
     build_schedule_from_dbt_selection(
         [dbtlearn_dbt_assets],         # The assets to materialize
         job_name="materialize_dbt_models",
         cron_schedule="0 0 * * *",     # Every midnight
         dbt_select="fqn:*",            # Specify dbt selector. fqn is fully qualified names. fqn:* betekent: materialize all. 
     ),
]