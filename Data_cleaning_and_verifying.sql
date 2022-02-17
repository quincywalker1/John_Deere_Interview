-- In this portion I want to make sure there are no duplicates so I used distinct count(*)
select
distinct 
count(*) as 'distinct'
from
[John Deere]..John_deere$;

select
count(*) as 'all'
from
[John Deere]..John_deere$;

-- In this portion I want to clean all null, agian here I used count to insure it has made a difference
select
count(*) as 'min, max, modal'
from
[John Deere]..John_deere$
where [Min_price($)] is not null
and [Modal_price($)] is not null
and [Max_price($)] is not null;

select
count(*) as 'min'
from
[John Deere]..John_deere$
where [Min_price($)] is not null;

select
count(*) as 'max'
from
[John Deere]..John_deere$
where [Max_price($)] is not null;

select
count(*) as 'modal'
from
[John Deere]..John_deere$
where [Modal_price($)] is not null;

-- Just in case I cleand everything that could have a null so I can compute it in python
select
* 
from [John Deere]..John_deere$
where [Min_price($)] is not null
and [Modal_price($)] is not null
and [Max_price($)] is not null
order by County_name, Commodity, Date;

