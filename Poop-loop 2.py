from sys import exit
from time import sleep
import time
from os.path import exists

def make_file():

    filename = 'Poop_Tracker.csv'
    target = open(filename, 'a+')
    target.seek(0)
    target.write("Hours")
    target.write(",")
    target.write("Minutes")
    target.write(",")
    target.write("Seconds")
    target.write(",")
    target.write("\n")


def write_to_file(time_in):


    p_hours = time_in.pop(0)
    p_mins = time_in.pop(0)
    p_secs = time_in.pop(0)

    p_hours = str(p_hours)
    p_mins = str(p_mins)
    p_secs = str(p_secs)

    print "Opening the file..."

    filename = 'Poop_Tracker.csv'
    if exists(filename) == False:
        make_file()

    target = open(filename, 'a+')
    old = target.read()
    end_of_file = len(old)
    target.seek(end_of_file)
    target.write(p_hours)
    target.write(",")
    target.write(p_mins)
    target.write(",")
    target.write(p_secs)
    target.write(",")
    target.write("\n")

    print "Alright, all done"

    target.close()


def time_convert(time_start, time_stop):


   t_time = time_stop - time_start

   if t_time < 60
       return t_time
   elif t_time > 60 and

    return t_time


def record_time():

    print "recording time"
    print "Press CTRL + C to stop recording."
    time_start = time.time()
    time_start = int(time_start)

    try:
        while time_start:
            print "."
            sleep(5)
    except KeyboardInterrupt:
        time_stop = time.time()
        time_stop = int(time_stop)
        return time_start, time_stop


print "Are you ready to poop?"

answer = raw_input("Type Yes or No> ")

if 'Y' in answer or 'y' in answer:
    start_time, stop_time = record_time()
    time_total = time_convert(start_time, stop_time)
    #print time_total
    write_to_file(time_total)

else:
    print "Okay, tell me when you're ready to poop"
    exit()
