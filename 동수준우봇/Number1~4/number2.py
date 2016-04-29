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

    ggulzam_value = []

    for i in range(0,len(user_list)):
        count = 0
        for j in range(0,7): # 일주일간의 수면시간 체크!!!!!
                for k in range(0, len(sleep_list[i][j]['sleep'])):
                    for l in range(0, len(sleep_list[i][j]['sleep'][k]["minuteData"])):
                        sleeptime = int(sleep_list[i][j]['sleep'][k]["minuteData"][l]["dateTime"][0:2])
                        if  (0 <= sleeptime and sleeptime <= 7) or (23 <= sleeptime and sleeptime <= 24) :
                            count += 1
        ggulzam_value.append(count)

    dic = {}

    for i in range(0,len(user_list)):
        dic["User Number : " + str(user_list[i])] = ggulzam_value[i]

    final_list = sorted(dic.iteritems(), key=itemgetter(1), reverse=True)

    print("11월 1일 부터 일주일간 꿀잠 랭킹")
    for i in range(0,6):
        print str(final_list[i][0]) +"\t"+ str(final_list[i][1])

    print("\n가장 꿀잠을 주무신 분")
    print str(final_list[0][0])
    matplotlib.style.use("ggplot")

    y_pos = np.arange(len(ggulzam_value))
    colors = []
    for i in range (0, len(user_list)):
        colors.append ("#%06x" % random.randint(0, 0xFFFFFF)     )
 
    bar= plt.bar(y_pos, ggulzam_value, align='center', alpha=0.5,color = colors)
    plt.xticks(y_pos, user_list)
    plt.ylabel('꿀잠 지수 ',family=['NanumGothic'])

    plt.title('꿀잠 지수 그래프',family=['NanumGothic'])

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width()/2., 0.5*height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(bar)
    plt.show()    
    

if __name__ == "__main__":

    main()