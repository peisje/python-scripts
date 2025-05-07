import os
import time
import datetime
import csv



output = os.popen("tasklist").read()
test = output.splitlines()
for i in range(7, len(test)):
    print(test[i])
    now =datetime.datetime.now()
    proccessname = test[i].split()
    name = proccessname[0]
    memory = proccessname[-2]
    print("time: ", now, "name: ", name, "memory: ", memory)
    

with open('proccess.csv', 'w',encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["TIME","Proccess name", "memory usage"])


            
          
    with open('proccess.csv', 'a',encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow([now,  name, memory])    
            
        print("time: ", now, "name: ", name, "memory: ", memory)
        
  