import psycopg2
connection = psycopg2.connect(
    host="os-c-db.cfxe5jyx7l0h.us-east-2.rds.amazonaws.com", port=5432, database="os-c-db", user="postgres", password="os-c-db-NoPassword123!")
cursor = connection.cursor()

# cursor.execute("DROP TABLE osdbheat")
# connection.commit()

cursor.execute(
    "CREATE TABLE osdbheat " +
    "(key VARCHAR(24), latitude NUMERIC(12,6), longitude NUMERIC(12,6)," +

    " heatssp1262020daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp1262030daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp1262040daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp1262050daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp1262075daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp1262100daysexceeding35cmetric_mean NUMERIC(12,6), " +


    " heatssp5852020daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp5852030daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp5852040daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp5852050daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp5852075daysexceeding35cmetric_mean NUMERIC(12,6), " +
    " heatssp5852100daysexceeding35cmetric_mean NUMERIC(12,6), " +

    " heatssp1262020daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp1262030daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp1262040daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp1262050daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp1262075daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp1262100daysexceeding38cmetric_mean NUMERIC(12,6), " +


    " heatssp5852020daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp5852030daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp5852040daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp5852050daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp5852075daysexceeding38cmetric_mean NUMERIC(12,6), " +
    " heatssp5852100daysexceeding38cmetric_mean NUMERIC(12,6) " +



    ")"
)

connection.commit()

cursor.execute("CREATE INDEX keyheat_idx ON osdbheat(key)")

connection.commit()
connection.close()
