import psycopg2
connection = psycopg2.connect(
    host="os-c-db.cfxe5jyx7l0h.us-east-2.rds.amazonaws.com", port=5432, database="os-c-db", user="postgres", password="os-c-db-NoPassword123!")
cursor = connection.cursor()


# cursor.execute("DROP TABLE osdbfire")
# connection.commit()

cursor.execute(
    "CREATE TABLE osdbfire " +
    "(key VARCHAR(24), latitude NUMERIC(12,6), longitude NUMERIC(12,6)," +

    " firessp1262020metric_mean NUMERIC(12,6), " +
    " firessp1262030metric_mean NUMERIC(12,6), " +
    " firessp1262040metric_mean NUMERIC(12,6), " +
    " firessp1262050metric_mean NUMERIC(12,6), " +
    " firessp1262075metric_mean NUMERIC(12,6), " +
    " firessp1262100metric_mean NUMERIC(12,6), " +


    " firessp5852020metric_mean NUMERIC(12,6), " +
    " firessp5852030metric_mean NUMERIC(12,6), " +
    " firessp5852040metric_mean NUMERIC(12,6), " +
    " firessp5852050metric_mean NUMERIC(12,6), " +
    " firessp5852075metric_mean NUMERIC(12,6), " +
    " firessp5852100metric_mean NUMERIC(12,6) " +



    ")"
)

connection.commit()

cursor.execute("CREATE INDEX key_idx ON osdbfire(key)")

connection.commit()
connection.close()
