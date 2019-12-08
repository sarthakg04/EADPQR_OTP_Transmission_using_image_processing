import cv2
import numpy as np
import cv2
import pyqrcode 
from pyqrcode import QRCode 
from PIL import Image
import numpy as np
#---------------------Code for Primary OTP Starts here----------------------------------#

flag=0
while(flag==0):
    import random
    q=[]
    a=[x for x in range(65,91)]
    for f in range(48,58):
        a.append(f)
    for e in range(97,123):
        a.append(e)
    a.append(35)
    a.append(42)
    matrix=[]
    for i in range(0,8):
        inArray=[] 
        for j in range(0,8):
            c=a[random.randint(0,len(a)-1)]
            a.remove(c)
            inArray.append(chr(c))
        matrix.append(inArray)
    print("Enter The Number of OTP Digits:")
    num=int(input())
    for r in range(num):
        l=random.randint(0,7)
        p=random.randint(0,7)
        q.append(matrix[l][p])
    print("DYNAMIC OTP IS:-")
    for k in q:
        print(k," ",end="")
    print("\nTo Continue Generating Passwords Press 0 Else Press 1")
    ch=int(input())
    if(ch==0):
        flag=0
    elif(ch==1):
        flag=1
print(q)
o = ''.join([str(elem) for elem in q])
url = pyqrcode.create(o) 
url.svg("OTP.svg", scale = 8)
url.png('OTP.png')

#---------------------------------Code for SKIN OTP STARTS HERE-------------------------#
mat=[]
a=[x for x in range(65,91)]
for f in range(48,58):
    a.append(f)
for e in range(97,123):
    a.append(e)
a.append(35)
a.append(42)
matrix=[]
for i in range(0,8):
    inArray=[] 
    for j in range(0,8):
        c=a[random.randint(0,len(a)-1)]
        a.remove(c)
        inArray.append(chr(c))
    matrix.append(inArray)
for r in range(num):
    l=random.randint(0,7)
    p=random.randint(0,7)
    mat.append(matrix[l][p])
print("SKIN OTP IS:-")
for k in mat:
    print(k," ",end="")
print(r)
m = ''.join([str(elem) for elem in mat])
url1 = pyqrcode.create(m) 
url1.svg("SKINOTP.svg", scale = 8)
url1.png('SKINOTP.png')
org = cv2.imread('OTP.png', cv2.IMREAD_UNCHANGED)
fil = cv2.imread('SKINOTP.png', cv2.IMREAD_UNCHANGED)
bld = cv2.addWeighted(org,0.5,fil,0.5,0)
#---------------------Transmission OTP for HTTP Protocol Transmission-------------------#
cv2.imwrite('Transmission_OTP.png', bld)
#---------------------Program on the END USER to Retrieve OTP---------------------------# 
org = cv2.addWeighted(bld,2,fil,-1, 0)
cv2.imwrite('Retrieved_OTP.png', org) 