import psycopg2
connection = psycopg2.connect(
    host="os-c-db.cfxe5jyx7l0h.us-east-2.rds.amazonaws.com", port=5432, database="os-c-db", user="postgres", password="os-c-db-NoPassword123!")
cursor = connection.cursor()


# cursor.execute("DROP TABLE osdbhail")
# connection.commit()

cursor.execute(
    "CREATE TABLE osdbhail " +
    "(key VARCHAR(24), latitude NUMERIC(12,6), longitude NUMERIC(12,6)," +

    " hailssp1262020dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp1262030dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp1262040dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp1262050dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp1262075dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp1262100dayslargehailpossiblemetric_mean NUMERIC(12,6), " +


    " hailssp5852020dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp5852030dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp5852040dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp5852050dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp5852075dayslargehailpossiblemetric_mean NUMERIC(12,6), " +
    " hailssp5852100dayslargehailpossiblemetric_mean NUMERIC(12,6) " +



    ")"
)

connection.commit()

cursor.execute("CREATE INDEX keyhail_idx ON osdbhail(key)")

connection.commit()
connection.close()
