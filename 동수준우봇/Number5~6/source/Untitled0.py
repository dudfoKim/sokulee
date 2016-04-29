
# coding: utf-8

# In[2]:

import json
import glob

fitbit_FILE=glob.glob("./intraday/*.json")
fitbit={}

def readfitbit(filename) :
    f = open(filename, 'r')
    js = json.loads(f.read())
    f.close()
    return js

def writefitbit(Json_file, filename) :
    f = open(filename, 'w')
    js = json.dump(Json_file,f)
    f.close()
    return js

def main() :
    global fitbit_FILE
    global fitbit
    for f in fitbit_FILE:
        fitbitJ = readfitbit(f)
        fitbitJ["_id"] = "changed_"+f[11:]
        writefitbit(fitbitJ, "changed_"+f[11:])
    
if __name__ == "__main__":
    main()


# In[66]:

## Problem 6

from pymongo import MongoClient
import pandas
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

client = MongoClient('mongodb://localhost:27017/')
db = client.local
collection = db.sokuri

#heart=collection.find({"_id":{"$regex":"_1_.*_heart"}})
total=pandas.DataFrame(columns=['Fat_min', 'Fat_cal', 'Car_min', 'Car_cal', 'Peak_min', 'Peak_cal'])
Fat_min_sum=0
Fat_cal_sum=0
Car_min_sum=0
Car_cal_sum=0
Peak_min_sum=0
Peak_cal_sum=0

for i in range(1,18):
    heart=collection.find({"_id":{"$regex":"_"+str(i)+"_.*_heart"}})
    #if(heart.count() != 0):
    for j in range(0,heart.count()):
        #sum+=heart[j]['activities-heart'][0]['heartRateZones'][1]
        try:
            Fat_min_sum+=heart[j]['activities-heart'][0]['value']['heartRateZones'][1]['minutes']
            Fat_cal_sum+=heart[j]['activities-heart'][0]['value']['heartRateZones'][1]['caloriesOut']
            Car_min_sum+=heart[j]['activities-heart'][0]['value']['heartRateZones'][2]['minutes']
            Car_cal_sum+=heart[j]['activities-heart'][0]['value']['heartRateZones'][2]['caloriesOut']
            Peak_min_sum+=heart[j]['activities-heart'][0]['value']['heartRateZones'][3]['minutes']
            Peak_cal_sum+=heart[j]['activities-heart'][0]['value']['heartRateZones'][3]['caloriesOut']
        except KeyError:
            pass
        
    total.loc[i]=[Fat_min_sum,Fat_cal_sum,Car_min_sum,Car_cal_sum,Peak_min_sum,Peak_cal_sum]
    Fat_min_sum=0
    Fat_cal_sum=0
    Car_min_sum=0
    Car_cal_sum=0
    Peak_min_sum=0
    Peak_cal_sum=0
    
print(total.iloc[:,[1]])

tt = total.iloc[:,[1,3,5]]

tt.plot(kind='barh', stacked=True)

plt.show()


# In[3]:

## Problem 5

#total=pandas.DataFrame(columns=[0:24])
time=[[0 for x in range(24)] for x in range(18)]
count=[[0 for x in range(24)] for x in range(18)]
for i in range(1,18):
    heart=collection.find({"_id":{"$regex":"_"+str(i)+"_.*_heart"}})
    print("i = "+str(i))
    #if(heart.count() != 0):
    for j in range(0,heart.count()):
        #sum+=heart[j]['activities-heart'][0]['heartRateZones'][1]
        length = len(heart[j]['activities-heart-intraday']['dataset'])
        intraday=heart[j]['activities-heart-intraday']['dataset']
        if(length!=0):
            try:
                for k in range(length):
                    #print(intraday[k]['time'][:2])
                    time[i][int(intraday[k]['time'][:2])]+=int(intraday[k]['value'])
                    count[i][int(intraday[k]['time'][:2])]+=1
            except KeyError:
                pass
        
print(time)

# In[29]:

import math
temp = [ x for x in range(24)]

beat = [[0 for x in range(24)] for x in range(18)]

for i in range(1, 18):
    for j in range(24):
        if(count[i][j]!=0):
            beat[i][j] = time[i][j] / count[i][j]
heartBeat=pandas.DataFrame(beat,columns=temp)


# In[30]:

print(time)
print(count)
print(heartBeat)


# In[60]:

import numpy as np

heartBeat_t=heartBeat.transpose()
del heartBeat_t[0]
del heartBeat_t[17]
print(heartBeat_t)
#tt.plot(kind='barh', stacked=True)


# In[67]:

plt.pcolor(heartBeat_t)
print(heartBeat_t.index)
plt.yticks(np.arange(0.5, len(heartBeat_t.index), 1), heartBeat_t.index)
print(heartBeat_t.columns)
plt.xticks(np.arange(0.5, len(heartBeat_t.columns), 1), heartBeat_t.columns)
plt.colorbar()
plt.show()


# In[68]:

from sklearn.cluster import KMeans

est=KMeans(8)
heartBeat=heartBeat_t.transpose()
est.fit(heartBeat)
labels = est.labels_

print(labels)


# In[12]:




# In[ ]:



