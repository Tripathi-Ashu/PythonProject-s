from time import*
import random as r

def mistake(partesr, usertest):
    error =0
    for i in range(len(partesr)):
        try:
            if partesr[i] != usertest[i]:
                error = error +1

        except:
            error =error+1

    return error           

def speed_time(time_s, time_e,userinput):
    time_delay= time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput)/time_R
    return round(speed)


test = ["How do I get the time library in Python? The time library is part of the Python Standard Library, so you don't need to install it separately. You can simply import it using import time ","import the time module first, and then you can use the ctime() method to get the current date and time" ," My name Ashutosh Tripathi"]
test1 = r.choice(test)

print("*** typing Speed ****")

print(test1)
print()
print()
time_1 = time()


testinput = input("Enter:" )
time_2 =time()

print('speed:' , speed_time(time_1,time_2,testinput),"w/s")
print("Error:" , mistake(test1,testinput))
