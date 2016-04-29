#-*- coding: utf-8 -*-

import json
import glob
from operator import itemgetter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

def readStep(user) :

    step_list = []

    file_list = glob.glob("./intraday/"+str(user)+ "_*_ste*.json") 
    for f in file_list:
        file = open(f)
        js = json.loads(file.read())
        step_list.append(js)
        file.close()
    return step_list

def getUser():
    file_list = glob.glob("./intraday/*_20151101_ste*.json") 
    user_list = []
    
    for i in file_list:
        temp = i.split("/")
        user = int( temp[2].split("_")[0])

        user_list.append(user)

    return user_list

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 0.3*height,
                '%d' % int(height),
                ha='center', va='bottom')


def main() :

    user_list = sorted(getUser())


    step_list = []
    
    for i in user_list:
        step_list.append(readStep(i))


    AM_step_count = []
    for i in range(0,len(user_list)):
        count = 0
        for j in range(0,len(step_list[0])):
                for k in range(0,719):
                    count +=step_list[i][j]["activities-steps-intraday"]["dataset"][k]["value"]

        AM_step_count.append(count)


    AM_dic = {}

    for i in range(0,len(user_list)):
        AM_dic["User Number : " + str(user_list[i])] = AM_step_count[i]

    AM_final_list = sorted(AM_dic.iteritems(), key=itemgetter(1), reverse=True)

    print("오전에 많이 운동한 사람 랭킹 TOP 5")
    for i in range(0,5):
        print str(AM_final_list[i][0]) +"\t"+ str(AM_final_list[i][1])


    PM_step_count = []


    for i in range(0,len(user_list)):
        count = 0
        for j in range(0,len(step_list[0])):
                for k in range(720,len(step_list[i][j]["activities-steps-intraday"]["dataset"])):
                    count +=step_list[i][j]["activities-steps-intraday"]["dataset"][k]["value"]
        PM_step_count.append(count)


    PM_dic = {}

    for i in range(0,len(user_list)):
        PM_dic["User Number : " + str(user_list[i])] = PM_step_count[i]

    PM_final_list = sorted(PM_dic.iteritems(), key=itemgetter(1), reverse=True)

    print("\n\n오후에 많이 운동한 사람 랭킹 TOP 5")
    for i in range(0,5):
        print str(PM_final_list[i][0]) +"\t"+ str(PM_final_list[i][1])    

    matplotlib.style.use("ggplot")
    plt.subplot(2, 1,1)
    y_pos = np.arange(len(AM_step_count))
    colors = []
    for i in range (0, len(user_list)):
        colors.append ("#%06x" % random.randint(0, 0xFFFFFF)     )
    bar=plt.bar(y_pos, AM_step_count, align='center', alpha=0.5,color = colors)
    plt.xticks(y_pos, user_list)
    plt.ylabel('걸음 수',family=['NanumGothic'])

    plt.title('오전에 누가 가장 운동을 많이했을까?',family=['NanumGothic'])

    autolabel(bar)

    plt.subplot(2, 1,2)
    y_pos = np.arange(len(PM_step_count))
   
    bar=plt.bar(y_pos, PM_step_count, align='center', alpha=0.5,color = colors)
    plt.xticks(y_pos, user_list)
    plt.ylabel('걸음 수',family=['NanumGothic'])

    plt.title('오후에 누가 가장 운동을 많이했을까?',family=['NanumGothic'])


    autolabel(bar)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    main()