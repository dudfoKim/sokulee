#-*- coding: utf-8 -*-

import json
import glob
from operator import itemgetter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

def readSleep(user) :

    sleep_list = []

    file_list = glob.glob("./intraday/"+str(user)+ "_*_sleep.json") 
    for f in file_list:
        file = open(f)
        js = json.loads(file.read())
        sleep_list.append(js)
        file.close()
    return sleep_list

def getUser():
    file_list = glob.glob("./intraday/*_20151101_sleep.json") 
    user_list = []
    
    for i in file_list:
        temp = i.split("/")
        user = int( temp[2].split("_")[0])

        user_list.append(user)

    return user_list

def main() :

    user_list = sorted(getUser())

    sleep_list = []
    
    for i in user_list:
        sleep_list.append(readSleep(i))

    user_value = {}
    user_sleep_date = {}
    for i in range(0,len(user_list)):
        sleeptime_list = []
        sleepdate_list = []
        for j in range(0,len(sleep_list[i])):
                for k in range(0, len(sleep_list[i][j]['sleep'])):
                    if int(sleep_list[i][j]['sleep'][k]["minutesAsleep"]) >= 240:
                        sleeptime = int(sleep_list[i][j]['sleep'][k]["minuteData"][len(sleep_list[i][j]['sleep'][k]["minuteData"])-1]["dateTime"][0:2])
                        sleepdate = sleep_list[i][j]['sleep'][k]["dateOfSleep"][8:10]

                        sleeptime_list.append(sleeptime)
                        sleepdate_list.append(sleepdate)
        user_value[user_list[i]] = sleeptime_list
        user_sleep_date[user_list[i]] = sleepdate_list

    colors = []
    for i in range (0, len(user_list)):
        colors.append ("#%06x" % random.randint(0, 0xFFFFFF))
    final_list = user_value.items()
    final_sleep_list = user_sleep_date.items()

    for i in range(0,len(user_list)):
        x =[]
        for j in range(0,len(final_sleep_list[i][1])):
            x.append(j)
        matplotlib.style.use("ggplot")

        plt.subplot(4,5,i+1)
        plt.ylim([0,24])
        plt.xticks(x, final_sleep_list[i][1],family=['NanumGothic'])
        plt.ylabel('시간',family=['NanumGothic'])
        plt.xlabel('일',family=['NanumGothic'])
        plt.title(str(final_list[i][0])+"번 참가자",family=['NanumGothic'])
        plt.plot(final_list[i][1],color=colors[i])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    main()