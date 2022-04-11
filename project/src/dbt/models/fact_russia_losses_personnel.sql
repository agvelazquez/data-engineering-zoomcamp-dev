{{config(materialized='incremental')}}

SELECT 
     cast(date as date) as date
    ,cast(day  as integer) as day
    ,cast(personnel as integer) as personnel
FROM {{ source('raw','russia_losses_personnel')}}
