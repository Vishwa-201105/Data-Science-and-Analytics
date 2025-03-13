/*
update trips
set end_date= date(ended_at);

select * from trips;

alter table trips
drop column start_time;

alter table trips 
drop column end_time;

select * from trips;

alter table trips
add column start_time time;

alter table trips
add column end_time time;

UPDATE trips
SET start_time = TO_CHAR(started_at, 'HH24:MI:SS')::TIME;

update trips
set end_time=to_char(ended_at, 'HH24:MI:SS')::TIME;

select * from trips;

select ride_id, rideable_type, start_time, end_time, round(extract(epoch from (end_time-start_time))/60) as duration, member_casual
from trips;

alter table trips
add column duration int;

update trips
set duration = round(extract(epoch from (end_time-start_time))/60);

select ride_id, rideable_type, start_date, start_time, end_date, end_time, duration, member_casual 
from trips where duration<1;

UPDATE trips
SET
  duration = CASE
    WHEN end_time < start_time THEN
      ROUND(EXTRACT(EPOCH FROM (end_time - start_time + INTERVAL '24 hours')) / 60)
    ELSE
      ROUND(EXTRACT(EPOCH FROM (end_time - start_time)) / 60)
  END;

select ride_id, start_date, start_time, end_date, end_time, duration from trips where duration<1;

delete from trips where duration=0;
*/
select * from trips;