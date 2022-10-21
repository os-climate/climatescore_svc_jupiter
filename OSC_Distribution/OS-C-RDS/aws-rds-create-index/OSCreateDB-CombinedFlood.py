import psycopg2
connection = psycopg2.connect(
    host="os-c-db.cfxe5jyx7l0h.us-east-2.rds.amazonaws.com", port=5432, database="os-c-db", user="postgres", password="os-c-db-NoPassword123!")
cursor = connection.cursor()


# cursor.execute("DROP TABLE osdbcombinedflood")
# connection.commit()

cursor.execute(
    "CREATE TABLE osdbcombinedflood " +
    "(key VARCHAR(24), latitude NUMERIC(12,6), longitude NUMERIC(12,6)," +

    " combinedfloodssp1262020floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp1262030floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp1262040floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp1262050floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp1262075floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp1262100floodedfraction200yrmetric_mean NUMERIC(12,6), " +


    " combinedfloodssp5852020floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp5852030floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp5852040floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp5852050floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp5852075floodedfraction200yrmetric_mean NUMERIC(12,6), " +
    " combinedfloodssp5852100floodedfraction200yrmetric_mean NUMERIC(12,6) " +




    ")"
)

connection.commit()

cursor.execute("CREATE INDEX keycombinedflood_idx ON osdbcombinedflood(key)")

connection.commit()
connection.close()
