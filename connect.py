import psycopg2
con = psycopg2.connect(
    host="comp421.cs.mcgill.ca",
    user="cs421g24",
    password="databaes2020",
    database="cs421")

print("Database opened successfully")


cur = con.cursor()
cur.execute("SELECT * from memory limit 5;")
rows = cur.fetchall()

for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("DEPARTMENT =", row[2], "\n")

print("Operation done successfully")
con.close()


# def doQuery(conn):
#     cur = conn.cursor()

#     cur.execute("select * from memory limit 5;")

#     for mid, mlikenum in cur.fetchall():
#         print mid, mlikenum

# doQuery(myConnection)
# myConnection.close()
