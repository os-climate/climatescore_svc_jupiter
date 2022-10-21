import psycopg2
connection = psycopg2.connect(
    host="os-c-db.cfxe5jyx7l0h.us-east-2.rds.amazonaws.com", port=5432, database="os-c-db", user="postgres", password="os-c-db-NoPassword123!")
cursor = connection.cursor()


# cursor.execute("DROP TABLE osdbdrought")
# connection.commit()

cursor.execute(
    "CREATE TABLE osdbdrought " +
    "(key VARCHAR(24), latitude NUMERIC(12,6), longitude NUMERIC(12,6)," +

    " droughtssp1262020monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp1262030monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp1262040monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp1262050monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp1262075monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp1262100monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +


    " droughtssp5852020monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp5852030monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp5852040monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp5852050monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp5852075monthsExtreme3moSPEImetric_mean NUMERIC(12,6), " +
    " droughtssp5852100monthsExtreme3moSPEImetric_mean NUMERIC(12,6) " +



    ")"
)

connection.commit()

cursor.execute("CREATE INDEX keydrought_idx ON osdbdrought(key)")

connection.commit()
connection.close()
