select
EXTRACT(YEAR FROM launched_at) AS launch_year,
sum(CAST(launch_success AS INT64)) as successful_launches,
count(*) as total_launches,
round(((sum(CAST(launch_success AS INT64))/count(*))*100),2) as success_rate
FROM {{ ref('staging_spacex_launches') }}
group by launch_year
order by launch_year desc