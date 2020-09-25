import requests

from mymodule import *


response=requests.get("http://api.open-notify.org/iss-pass.json")


#------------------------------
#this code would raise an error as it is specified in the documentation of the API that it needs some paameters in the request
if(response.status_code==200):
	print(" Succcess ")
else:
	code(response.status_code)

#---------------------------

#request with parameter
parameters={
	"lat":40.71,
	"lon":-74
}

response=requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)

gprint(response.json())

pass_times=response.json()['response']
#gprint(pass_times)


rise_time=[]

for d in pass_times:
	
	time=d['risetime']
	rise_time.append(time)

print(rise_time)
#since these times are difficult to understand - they are in a format known as timestamp or epochs.
from datetime import datetime
times=[]

for x in rise_time:
	time= datetime.fromtimestamp(x)
	times.append(time)
	print(time)

