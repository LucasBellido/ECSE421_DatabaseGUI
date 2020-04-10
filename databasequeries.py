import psycopg2
from tkinter import messagebox


def getAlbums():

    try:
        lst = []
        conn = psycopg2.connect(
            host="comp421.cs.mcgill.ca",
            user="cs421g24",
            password="databaes2020",
            database="cs421")

        cur = conn.cursor()
        cur.execute("SELECT * from album order by aid;")
        print("The number of albums: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            lst.append(row)
            row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        messagebox.showerror(
            "Error", "Error connecting to database. Please close and restart")
    finally:
        if conn is not None:
            conn.close()
            return lst


def getAlbum(albumID):
    try:
        conn = psycopg2.connect(
            host="comp421.cs.mcgill.ca",
            user="cs421g24",
            password="databaes2020",
            database="cs421")

        cur = conn.cursor()

        cur.execute(
            "SELECT * from album where album.aid='{}';".format(str(albumID)))
        print("The number of albums: ", cur.rowcount)
        row = cur.fetchone()

        return row
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        messagebox.showerror(
            "Error", "Error loading the album: {}".format(error))
    finally:
        if conn is not None:
            conn.close()


def modifyAlbumEntry(albumID, albumName):
    try:
        conn = psycopg2.connect(
            host="comp421.cs.mcgill.ca",
            user="cs421g24",
            password="databaes2020",
            database="cs421")
        cur = conn.cursor()
        print(albumID)
        print(albumName)

        cur.execute("update album set aname='{}' where aid='{}'".format(
            albumName, str(albumID)))

        conn.commit()
        messagebox.showerror(
            "Confirmation", "Successfully modified album to:{}".format(albumName))
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        messagebox.showerror(
            "Confirmation", "Error: {}".format(error))
    finally:
        if conn is not None:
            conn.close()
