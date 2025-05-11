{{ config(
    materialized='incremental',
    unique_key='launch_id'
) }}

SELECT
  id as launch_id,
  name as mission_name,
  date_utc as launched_at,
  success as launch_success
FROM {{ source('spacex_dataset', 'spacex_table') }}

{% if is_incremental() %}
  WHERE date_utc > (SELECT MAX(date_utc) FROM {{ this }})
{% endif %}
