from pyspark.sql import SparkSession

spark=SparkSession.builder.getOrCreate()
df=spark.read.format('json').option('multiline',True).load('D:\ccrmrd\my_glue_rmrd\2_Thalaivasal CC_1614_2023_12_01.json')
df.show()