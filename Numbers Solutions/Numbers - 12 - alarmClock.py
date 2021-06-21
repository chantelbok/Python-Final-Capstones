""" Create a simple alarm clock that can play a sound based on a timer or at a specific time. """
import datetime  # gives current time on the computer
from playsound import playsound  # to play a sound
import time  # for the timer function


def convert_time(pm, hour):
    """Converts to 24 hour format"""
    if pm.lower() == "pm":
        hour += 12
    return hour


def main():
    # start off by giving user a choice on how they want the alarm to function
    user_choice = input("Alarm on timer or at a specific time? Enter timer or time ")

    # if the user wants to use the timer function:
    if user_choice.lower() == 'timer':
        hour_time = int(input('After how many hours do you want the alarm to sound? '))
        min_time = int(input('After how many mins do you want the alarm to sound? '))
        # then the program will sleep for the calculated amount of seconds
        time.sleep(hour_time * 60 * 60 + min_time * 60)
        # and then play the alarm ringtone
        playsound('ringtone_deep.mp3')
    # if the user want the alarm to go off at a specific time
    else:
        # user enters hour, min and am/pm
        alarm_hour = int(input("What hour should the alarm sound? Enter 1 - 12 "))
        alarm_min = int(input("What minute should the alarm sound? Enter 0 - 59 "))
        am_pm = input("am or pm? ")
        # call the convert_time function to deal with pm values
        alarm_hour = convert_time(am_pm, alarm_hour)
        # program will run in background until
        while True:
            # the user time matches the current time on computer
            if alarm_hour == datetime.datetime.now().hour and alarm_min == datetime.datetime.now().minute:
                # and then call the playsound function from the imported library on the ringtone in mp3 format
                playsound('ringtone_deep.mp3')
                # once the ringtone is done playing the program will end
                break


if __name__ == '__main__':
    main()
