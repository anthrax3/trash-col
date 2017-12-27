from Crypto.Cipher import XOR
import sys
import base64

def encrypt(key, plaintext):
  cipher = XOR.new(key)
  return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(key, ciphertext):
  cipher = XOR.new(key)
  return cipher.decrypt(base64.b64decode(ciphertext))

try:
	f1=open(sys.argv[2],"r")
	if(sys.argv[1]=="1"):
		s=encrypt(sys.argv[3],f1.read())
	elif(sys.argv[1]=="2"):
		s=decrypt(sys.argv[3],f1.read())
	else:
		print "Invalid usage"
	f2=open(sys.argv[2],"w")
	f2.write(s)
	f1.close()
	f2.close()
	print s
except:
	print "Usage : python scriptName.py optn file key\n\toptn :\n\t  1 Encrypt\n\t  2 Decrypt"
