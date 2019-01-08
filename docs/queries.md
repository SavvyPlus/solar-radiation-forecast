```
select radiationtype, longitude, latitude, year, month, sum(radiation)
from bom_parquet_test where year = '2005' and month = '01'
group by radiationtype, longitude, latitude, year, month
```


```
SELECT Count(*)
FROM   (
        SELECT DISTINCT
               longitude
             , latitude

        FROM   bom_parquet_test WHERE year = '2004'
       ) As count_location
-- results 569681      
```


## Query get radiation data by coordinates
```
SELECT "year" AS "year",
       "month" AS "month",
       avg(radiation) AS "radiation"
FROM "gzip_lat"
WHERE (latitude = '-41.57522170000015'
      and longitude = '145.27194600000016'
      AND radiation != -999)
GROUP BY "year",
        "month"
ORDER BY "year" ASC,
        "month" ASC
LIMIT 50000      
```

```
SELECT "year" AS "year",
       "month" AS "month",
       radiation
FROM "bom_parquet_test"
WHERE (latitude = -41.57522170000015
      and longitude = 145.27194600000016
      AND radiation != -999)
LIMIT 100
```

## Query to get train data
```
SELECT "year" AS "year",
       "month" AS "month",
       "radiationtype" as "radiationtype",
       avg(radiation) AS "radiation"
FROM "gzip_lat"
WHERE (latitude = '-41.57522170000015'
      AND longitude = '145.27194600000016'
      AND radiation != -999
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )
GROUP BY "year",
         "month",
         "radiationtype"
ORDER BY "year" ASC,
         "month" ASC
LIMIT 50000        
```


```
SELECT "year" AS "year",
       "month" AS "month",
       "radiationtype" as "radiationtype",
       avg(radiation) AS "radiation"
FROM "gzip_lat"
WHERE (latitude = '-41.57522170000015'
      AND longitude = '145.27194600000016'
      AND radiation != -999
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )
GROUP BY "year",
         "month",
         "radiationtype"
```
