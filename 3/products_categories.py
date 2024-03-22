from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("product_category").getOrCreate()

products = spark.createDataFrame([
    ("product1", "category1"),
    ("product2", "category1"),
    ("product3", "category2"),
], ["product", "category"])

categories = spark.createDataFrame([
    ("category1",),
    ("category3",),
], ["category"])

# у продукта 3 - несуществующая категория, а в категории 3 - нет ни одного продукта
# необходимо из фрейма продуктов взять все продукты и для них вывести их категорию (если существует)
# в sql исполльзуется left join 

renamed = products.withColumnRenamed("category", "prod_cat") # устранение конфликта имен
pairs = renamed.join(categories, renamed.prod_cat == categories.category, "left") # sql-аналог - left join
pairs.select(pairs.product, pairs.category).show()

