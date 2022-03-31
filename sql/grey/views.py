
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

import psycopg2
# import sys
# sys.path.append('/home/user/Music/learning phase/myproject/newwork/sql/grey')
# from configparser import ConfigParser

def create_connection(self):

    # connect to the db
    con = psycopg2.connect(
            host = 'localhost',
            dbname = 'postgres',
            user = 'postgres',
            password = 'user')
    # cursor
    cur = con.cursor()
    # execute query
    # cur.execute("select id, name from employees")
    # rows = cur.fetchall()
    # for r in rows:
    #     print(f"id {r[0]} name {r[1]}")
    # close the cursor
    # cur.close()
    # close the connection
    # con.close()
    return(con,cur)

def create_tables(self):
    a,b=create_connection(self)
    # print(f"{a} : {b}")

    """ create tables in the PostgreSQL database"""

    # dhar ki query
    # b.execute("CREATE TABLE ankTEmp (id SERIAL PRIMARY KEY,name VARCHAR(30),age INT(3),email VARCHAR(255) NOT NULL);")

    # ank ki query
    b.execute("CREATE TABLE ANKTEMP(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL);")
    
    a.commit()
    b.close()

    return(HttpResponse('table created see in pg admin'))

def insert_values(self):
    a,b=create_connection(self)

    """insert values into tables in the PostgreSQL database"""

    # dhar
    # insert_script="INSERT INTO student (vendor_id,name) VALUES(4,'aashish')"

    # ank
    insert_script="INSERT INTO ANKTEMP (ID,NAME,AGE) VALUES(40,'DHAR', 2)"
    
    b.execute(insert_script)
    a.commit()
    b.close()
    return(HttpResponse('value inserted  in table see in pg admin'))
# read

def update_values(self):
    a,b=create_connection(self)

    """insert values into tables in the PostgreSQL database"""

    # dhar
    # update_script="UPDATE student SET name='anil' WHERE vendor_id=4"

    # ank 
    update_script="UPDATE ANKTEMP SET NAME='KHANAK' WHERE ID=20"
 
    b.execute(update_script)
    a.commit()
    b.close()
    return(HttpResponse('value updated of table see in pg admin'))

def delete_values(self):
    a,b=create_connection(self)

    """insert values into tables in the PostgreSQL database"""

    # dhar
    # delete_script="DELETE FROM  student WHERE vendor_id=3"

    # ank
    # delete_script="DELETE FROM ANKTEMP WHERE ID=40"
    # b.execute(delete_script)

    # to DROP a table 
    drop_table = "DROP TABLE ankdemo"
    b.execute(drop_table)

    a.commit()
    b.close()

def read_values(self):
    a,b=create_connection(self)

    """insert values into tables in the PostgreSQL database"""

    read_script="SELECT * FROM student"
    
    b.execute(read_script)

    for i in b.fetchall():
        print('id=',i[0],'name=',i[1])

    a.commit()
    b.close()
    return(HttpResponse('read all tables value '))