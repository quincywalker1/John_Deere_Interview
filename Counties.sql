-- In this section I queried by counties of intrest

--Linn
select *
from [John Deere]..John_deere$
where County_name = 'Linn'
order by Townships, Commodity, Date;
--Monroe
select *
from [John Deere]..John_deere$
where County_name = 'Monroe'
order by Townships, Commodity, Date;
--Harrison
select *
from [John Deere]..John_deere$
where County_name = 'Harrison'
order by Townships, Commodity, Date;