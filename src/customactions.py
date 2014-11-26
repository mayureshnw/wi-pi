pretext={"name":["Whats your name","What is your name","What your name"],
"marry":["Will you marry me","marry me"],
}
     
import sys

text = sys.argv[1:]

if "name" in text:
	x=pretext["name"]
   	for i in range(len(x)):
    		if text==x[i]:
     			print "Hello,I am WiPi"
elif "marry" in text:
	x=pretext["marry"]
   	for i in range(len(x)):
    		if text==x[i]:
     			print "Seriously ?, Get a life !"


