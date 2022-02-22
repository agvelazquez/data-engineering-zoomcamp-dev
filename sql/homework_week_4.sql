-- Question 1
SELECT COUNT(*) FROM `dtc-de-course-338720.production.fact_trips`
where EXTRACT(YEAR from pickup_datetime) IN (2020, 2019);


-- Question 2

SELECT service_type, COUNT(*) / (SELECT COUNT(*) FROM `dtc-de-course-338720.production.fact_trips`where EXTRACT(YEAR from pickup_datetime) IN (2020, 2019))
FROM `dtc-de-course-338720.production.fact_trips`
where EXTRACT(YEAR from pickup_datetime) IN (2020, 2019)
group by service_type
order by 1 desc;


-- Question 3
select count(*)
FROM `dtc-de-course-338720.trips_data_all.fhv_tripdata_2019`;


-- Question 4
with zones as (
    select * from  `dtc-de-course-338720.production.dim_zones` 
    where borough != 'Unknown'

)

select count(*)
FROM `dtc-de-course-338720.trips_data_all.fhv_tripdata_2019`  a 
inner join zones  b on a.DOLocationID = b.locationid
inner join zones  c on a.PULocationID = c.locationid
where EXTRACT(YEAR from pickup_datetime) = 2019;


-- Question 5
select  EXTRACT(MONTH from pickup_datetime), count(*)
FROM `dtc-de-course-338720.trips_data_all.fhv_tripdata_2019`  a
where EXTRACT(YEAR from pickup_datetime) = 2019
group by  EXTRACT(MONTH from pickup_datetime)
order by 2;
