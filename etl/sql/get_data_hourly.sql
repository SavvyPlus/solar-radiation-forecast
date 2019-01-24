-- Scripts for 1
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -15.627609100000022
      AND longitude = 128.77346400000008
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -16.427535500000026
      AND longitude = 126.42368020000006
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -14.477714900000016
      AND longitude = 132.3731328000001
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -17.02748030000003
      AND longitude = 128.22351460000007
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for sample_points
-- End scripts for 1
-- Scripts for 2
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -13.927765500000014
      AND longitude = 143.22213460000015
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -15.477622900000021
      AND longitude = 144.17204720000015
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -19.27727330000004
      AND longitude = 146.82180340000016
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -15.477622900000021
      AND longitude = 141.72227260000014
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for sample_points
-- End scripts for 2
-- Scripts for 3
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -19.827222700000043
      AND longitude = 141.37230480000014
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -22.077015700000054
      AND longitude = 146.22185860000016
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -21.12710310000005
      AND longitude = 149.17158720000018
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -23.42689150000006
      AND longitude = 144.27203800000015
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for sample_points
-- End scripts for 3
-- Scripts for 4
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -27.47651890000008
      AND longitude = 153.0212330000002
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -26.326624700000075
      AND longitude = 150.62145380000018
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -26.576601700000076
      AND longitude = 148.77162400000017
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -27.57650970000008
      AND longitude = 151.9713296000002
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for sample_points
-- End scripts for 4
-- Scripts for 5
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -31.4261555000001
      AND longitude = 152.9212422000002
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -33.87593010000011
      AND longitude = 151.22139860000019
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -32.92601750000011
      AND longitude = 151.7713480000002
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -33.77593930000011
      AND longitude = 150.92142620000018
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for sample_points
-- End scripts for 5
-- Scripts for 6
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -33.77593930000011
      AND longitude = 149.77153200000018
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -32.2260819000001
      AND longitude = 148.62163780000017
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -34.275893300000114
      AND longitude = 148.32166540000017
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -33.27598530000011
      AND longitude = 149.12159180000017
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points
-- -- End scripts for sample_points
-- End scripts for 6
-- Scripts for 7
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -35.32579670000012
      AND longitude = 149.12159180000017
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -37.52559430000013
      AND longitude = 149.77153200000018
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -37.97555290000013
      AND longitude = 146.97178960000016
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -36.475690900000124
      AND longitude = 148.27167000000017
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points
-- -- End scripts for sample_points
-- End scripts for 7
-- Scripts for 8
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -37.82556670000013
      AND longitude = 144.97197360000015
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -38.375516100000134
      AND longitude = 142.52219900000014
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -37.67558050000013
      AND longitude = 143.37212080000015
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -38.525502300000134
      AND longitude = 143.97206560000015
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points
-- -- End scripts for sample_points
-- End scripts for 8
-- Scripts for 9
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -34.22589790000011
      AND longitude = 142.12223580000014
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -35.32579670000012
      AND longitude = 143.57210240000015
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -33.02600830000011
      AND longitude = 145.17195520000016
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -34.775847300000116
      AND longitude = 146.92179420000016
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points
-- -- End scripts for sample_points
-- End scripts for 9
-- Scripts for 10
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -42.07517570000015
      AND longitude = 148.22167460000017
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -41.02527230000015
      AND longitude = 148.27167000000017
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -42.875102100000156
      AND longitude = 147.32175740000017
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -42.37514810000015
      AND longitude = 147.02178500000016
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for sample_points
-- End scripts for 10
-- Scripts for 11
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -42.12517110000015
      AND longitude = 145.32194140000016
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -41.07526770000015
      AND longitude = 144.67200120000015
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -40.675304500000145
      AND longitude = 144.92197820000015
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -42.775111300000155
      AND longitude = 146.07187240000016
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for sample_points
-- End scripts for 11
-- Scripts for 12
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -34.92583350000012
      AND longitude = 138.62255780000012
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -34.725851900000116
      AND longitude = 135.8728108000001
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -33.47596690000011
      AND longitude = 136.1727832000001
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -33.12599910000011
      AND longitude = 134.3729488000001
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points
-- -- End scripts for sample_points
-- End scripts for 12
-- Scripts for 13
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -29.27635330000009
      AND longitude = 124.67384120000006
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -28.326440700000084
      AND longitude = 116.67457720000002
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -30.976196900000097
      AND longitude = 135.7728200000001
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -32.376068100000104
      AND longitude = 142.42220820000014
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points
-- -- End scripts for sample_points
-- End scripts for 13
-- Scripts for 14
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -33.37597610000011
      AND longitude = 117.92446220000002
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = 31.926109500000102
      AND longitude = 115.87465080000001
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -33.32598070000011
      AND longitude = 115.62467380000001
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -34.375884100000114
      AND longitude = 119.37432880000003
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for sample_points
-- End scripts for 14
-- Scripts for 15
-- -- Scripts for central_points

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -23.67686850000006
      AND longitude = 133.8729948000001
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -27.37652810000008
      AND longitude = 141.82226340000014
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -21.17709850000005
      AND longitude = 119.72429660000003
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --

SELECT date, radiationtype, radiation
FROM "bom_parquet_test"
WHERE (latitude = -22.826946700000057
      AND longitude = 127.72356060000007
      AND contains(ARRAY['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], year)
      )

-- -- --
-- -- End scripts for central_points
-- -- Scripts for sample_points
-- -- End scripts for sample_points
-- End scripts for 15
