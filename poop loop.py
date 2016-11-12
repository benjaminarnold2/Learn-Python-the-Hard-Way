from sys import exit
from datetime import datetime
from time import sleep
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

    s_hours = time_start.pop(0)
    s_mins = time_start.pop(0)
    s_secs = time_start.pop(0)

    e_hours = time_stop.pop(0)
    e_mins = time_stop.pop(0)
    e_secs = time_stop.pop(0)
    
    s_hours = int(s_hours)
    s_mins = int(s_mins)
    s_secs = float(s_secs)
    #print s_mins
    #print s_secs

    e_hours = int(e_hours)
    e_mins = int(e_mins)
    e_secs = float(e_secs)
    #print e_mins
    #print e_secs

    t_hours = e_hours - s_hours
    if t_hours > 0 and s_mins > e_mins:
        e_mins += 60
    t_mins = e_mins - s_mins
    if t_mins > 0 and s_secs > e_secs:
        e_secs += 60
    t_secs = e_secs - s_secs
    t_secs = int(t_secs)
    #print t_mins
    #print t_secs

    total_time = [t_hours, t_mins, t_secs]

    return total_time


def record_time():

    print "recording time"
    print "Press CTRL + C to stop recording."
    time_start = datetime.now()
    time_start = str(time_start)
    time_start = time_start[11:]
    time_start = time_start.split(':')

    try:
        while time_start:
            print "."
            sleep(5)
    except KeyboardInterrupt:
        time_stop = datetime.now()
        time_stop = str(time_stop)
        time_stop = time_stop[11:]
        time_stop = time_stop.split(':')

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
