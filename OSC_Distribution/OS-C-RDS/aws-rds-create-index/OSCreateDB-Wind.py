import psycopg2
connection = psycopg2.connect(
    host="os-c-db.cfxe5jyx7l0h.us-east-2.rds.amazonaws.com", port=5432, database="os-c-db", user="postgres", password="os-c-db-NoPassword123!")
cursor = connection.cursor()


# cursor.execute("DROP TABLE osdbwind")
# connection.commit()

cursor.execute(
    "CREATE TABLE osdbwind " +
    "(key VARCHAR(24), latitude NUMERIC(12,6), longitude NUMERIC(12,6)," +

    " windssp1262020windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp1262030windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp1262040windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp1262050windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp1262075windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp1262100windSpeed100yrmetric_mean NUMERIC(12,6), " +


    " windssp5852020windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp5852030windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp5852040windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp5852050windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp5852075windSpeed100yrmetric_mean NUMERIC(12,6), " +
    " windssp5852100windSpeed100yrmetric_mean NUMERIC(12,6) " +



    ")"
)

connection.commit()

cursor.execute("CREATE INDEX keywind_idx ON osdbwind(key)")

connection.commit()
connection.close()
