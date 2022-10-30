import threading 
from time import sleep
class Task1(threading.Thread):
    def run(self):
        for i in range(5):
            print(i)
            sleep(1)
class Task2(threading.Thread):
    def run(self):
        for i in range(5):
            print("Task2")
            sleep(1)
inst1 = Task1()

inst2 = Task2()
inst1.start()
sleep(0.2)
inst2.start()

inst1.join() #To join the threads to main thread for further smooth processing
inst2.join()

#after joining the threads  inst1 and inst2 , now main threads start processing again alone 

print("Main Thread working Now ") #if we don't do this then main thread don't wait for other threads to finish their processing and move on