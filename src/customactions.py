pretext={"name":["Whats your name","What is your name","What your name"],
"marry":["Will you marry me","marry me"],
"gender":["are you male or female","male or female"],
"wearing":["what are you wearing"],
"creater":["who is your creator"],
"goodnight":["goodnight"],
}
     
import sys

text = sys.argv[1:]

if "name" in text:
	x=pretext["name"]
   	for i in range(len(x)):
    		if text==x[i]:
     			print "Hello,I am WiPi"
else if "marry" in text:
	x=pretext["marry"]
   	for i in range(len(x)):
    		if text==x[i]:
     			print "OK, we'll need a plan. I'll work on being more human, you work on being more digital."
else if "male" in text:
	x=pretext["gender"]
   	for i in range(len(x)):
    		if text==x[i]:
     			print "Female? Maybe. Woman? No."
else if "wearing" in text:
	x=pretext["wearing"]
   	for i in range(len(x)):
    		if text==x[i]:
     			print "Huh? Can't tell you."
else if "creator" in text:
	x=pretext["creator"]
   	for i in range(len(x)):
    		if text==x[i]:
     			print "Come on, chief, I can't give away all of all secrets.."
else if "goodnight" in text:
	x=pretext["goodnight"]
   	for i in range(len(x)):
    		if text==x[i]:
     			print "Goodnight, see you in the morning."


