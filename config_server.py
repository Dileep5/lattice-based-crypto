import mysql.connector
import socket
import sys
from ntru import *
from bits import *

N=int(sys.argv[1])
p=int(sys.argv[2])
q=int(sys.argv[3])
pub_key=sys.argv[4]

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="test"
)

mycursor = mydb.cursor()
sql = "UPDATE public_key SET N="+str(N)+",p="+str(p)+",q="+str(q)+",pub_key='"+pub_key+"'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")