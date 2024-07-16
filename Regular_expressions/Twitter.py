import re

url=input("Please enter the twitter URL: ").strip()

#username=url.replace("http://twitter.com/","")
#username=url.removeprefix("http://twitter.com/","")

#This code directly assigns but if we use search it will check 
# and if it is wrong it will show NONE

#username=re.sub(r"^http?s://(www\.)?twitter\.com/","",url)
#\so that the user cant use any other address than .com
#? to possibility of http or https
#(www\.)? www could be there or not 


if matches:=re.search(r"^http?s://(?:www\.)?twitter\.com/([a-z0-9_]+)$",url,re.IGNORECASE):
    #?: tells that ıt does not need to catch it 
    print(f"Username: {matches.groups(2)}")