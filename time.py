from datetime import time 
from datetime import datetime 

tim=datetime.now()
h=tim.strftime("%H")
m=tim.strftime("%M")
s=tim.strftime("%S")
print(h,m,s)