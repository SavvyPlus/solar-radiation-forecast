import config

# Query data by cooordinates and group monthly
FORMAT_QUERY_GROUP_DATA = """
SELECT "year" AS "year",
       "month" AS "month",
       "radiationtype" as "radiationtype",
       sum(radiation) AS "radiation"
FROM "bom_parquet_test"
WHERE (latitude = {}
      AND longitude = {}
      AND radiation != -999
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )
GROUP BY "year",
         "month",
         "radiationtype"
"""


def create_sql_scripts(path):
    with open(path, 'w') as fp:
        for key in config.CATEGORIES.keys():
            fp.write("-- Scripts for {}\n".format(key))
            central_points = config.CATEGORIES[key]['central']
            sample_points = config.CATEGORIES[key]['sample']
            fp.write("-- -- Scripts for central_points\n")
            for central_point in central_points:
                fp.write(FORMAT_QUERY_GROUP_DATA.format(central_point['lat'], central_point['long']))
                fp.write("\n-- -- -- \n")
            fp.write("-- -- End scripts for central_points\n")

            fp.write("-- -- Scripts for sample_points\n")
            for sample_point in sample_points:
                fp.write(FORMAT_QUERY_GROUP_DATA.format(sample_point['lat'], sample_point['long']))
                fp.write("\n-- -- -- \n")
            fp.write("-- -- End scripts for sample_points\n")
            fp.write("-- End scripts for {}\n".format(key))
