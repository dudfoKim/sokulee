# -*- coding : utf8 -*-

import csv
import matplotlib
import matplotlib.pyplot as plt

my_file = open ('YLKim.csv', 'r')
my_data = csv.DictReader(my_file)

result = {}
date = []
step = []
calorie = []
traveled = []

for temp in my_data:
	date.append(temp['DATE'])
	step.append(temp['STEP'])
	calorie.append(temp['CALORIE'])
	traveled.append(temp['TRAVELED'])

for i in range(1, len(date)):
	result[date[i]] = [step[i], calorie[i], traveled[i]]

plt.title('STEP ANALYSIS')
plt.xticks((0, 1, 2, 3, 4, 5, 6),(3.30, 3.31, 4.1, 4.2, 4.3, 4.4))
plt.plot(step)
plt.xlabel('DATE')
plt.ylabel('STEP')
plt.show()
