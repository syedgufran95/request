import requests
from mymodule import *


#Making an http request using get method at an API 
response=requests.get("http://api.open-notify.org/astros.json")


#printing response it must be 200 which means success
print(response.status_code)

#the data recieved is in json format as mentioned in the documentation
#lets have a look at the data
print("The response of type %s and he data is \n  %s : "%(type(response.json()),response.json()))
gprint(response.json())



