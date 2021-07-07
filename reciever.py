import socket
import sys
from ntru import *
from bits import *
import os

# N=7
# p=29
# q=491531
if (len(sys.argv)>1):
	N=int(sys.argv[1])
if (len(sys.argv)>2):
	p=int(sys.argv[2])
if (len(sys.argv)>3):
	q=int(sys.argv[3])
N=int(input("Enter value of N: "))
p=int(input("Enter value of p: "))
q=int(input("Enter value of q: "))

print("==== Bob generates public key =====")
Bob=Ntru(N,p,q)
print("Bob picks two polynomials (g and f):")
f=[1,1,-1,0,-1,1]
g=[-1,0,1,1,0,0,-1]
d=2
print("f(x)= ",f)
print("g(x)= ",g)
print("d   = ",d)
Bob.genPublicKey(f,g,2)
pub_key=Bob.getPublicKey()
print("Bob's Public Key: ",pub_key)

print("-------------------------------------------------")

print("Configuring server .........\n\n")
print('python config_server.py '+str(N)+" "+str(p)+" "+str(q)+" "+(','.join([str(x) for x in pub_key])))
os.system('python config_server.py '+str(N)+" "+str(p)+" "+str(q)+" "+(','.join([str(x) for x in pub_key])))
print("\n\nServer Configured ..... \n\n")

s = socket.socket()
s.bind(('0.0.0.0', 12345))
s.listen(5)
c, addr = s.accept()
print('Got connection from', addr)
x=str(c.recv(1024))
x=x[2:-1]
print(x)
x=list(map(int,str(x).strip().split()))
print(x)
x=Bob.decrypt(x)
print(x)
x=frombits(x)
print(x)
c.close()