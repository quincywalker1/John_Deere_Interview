-- In this section I queried by counties of intrest using my averages table I made in Python

--Linn
select *
from [John Deere]..Averages
where County_name = 'Linn'
order by Commodity;
--Monroe
select *
from [John Deere]..Averages
where County_name = 'Monroe'
order by Commodity;
--Harrison
select *
from [John Deere]..Averages
where County_name = 'Harrison'
order by Commodity;