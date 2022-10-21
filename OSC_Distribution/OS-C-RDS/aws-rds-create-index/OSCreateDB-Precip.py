import psycopg2
connection = psycopg2.connect(
    host="os-c-db.cfxe5jyx7l0h.us-east-2.rds.amazonaws.com", port=5432, database="os-c-db", user="postgres", password="os-c-db-NoPassword123!")
cursor = connection.cursor()


# cursor.execute("DROP TABLE osdbprecip")
# connection.commit()

cursor.execute(
    "CREATE TABLE osdbprecip " +
    "(key VARCHAR(24), latitude NUMERIC(12,6), longitude NUMERIC(12,6)," +

    " precipssp1262020onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp1262030onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp1262040onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp1262050onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp1262075onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp1262100onedayprecip100yrmetric_mean NUMERIC(12,6), " +


    " precipssp5852020onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp5852030onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp5852040onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp5852050onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp5852075onedayprecip100yrmetric_mean NUMERIC(12,6), " +
    " precipssp5852100onedayprecip100yrmetric_mean NUMERIC(12,6) " +




    ")"
)

connection.commit()

cursor.execute("CREATE INDEX keyprecip_idx ON osdbprecip(key)")

connection.commit()
connection.close()
