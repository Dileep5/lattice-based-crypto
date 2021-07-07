import socket
from bits import *
import sys
from ntru import *
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="test"
)

def getFromBob():
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM public_key")
	myresult = mycursor.fetchall()
	x=myresult[0]
	N=int(x[0])
	p=int(x[1])
	q=int(x[2])
	pub_key=list(map(int,x[3].strip().split(',')))
	return [N,p,q,pub_key]

s = socket.socket()
s.connect(('localhost', 12345))

N,p,q,pub_key=getFromBob()

print("\n==== Alice generates public key =====")
Alice=Ntru(N,p,q)
Alice.setPublicKey(pub_key)
msg=[1,0,1,0,1,1,1]
print("Alice's Message   : ",msg)
ranPol=[-1,-1,1,1]
print("Alice's Random Polynomial  : ",ranPol)
encrypt_msg=Alice.encrypt(msg,ranPol)
print("Encrypted Message          : ", encrypt_msg)
print("-------------------------------------------------")
s.send(bytes(" ".join([str(x) for x in encrypt_msg]),'utf-8'))
s.close()