# -*- coding : utf8 -*-

import csv
import matplotlib
import json

matplotlib.use('Agg')

import matplotlib.pyplot as plt

length = 11
url = []
chart = []

for i in range(0, length):
	if(i<10):
		url.append('05_2016040' + str(i+1) + '_steps.json')
	else:
		url.append('05_201604' + str(i+1) + '_steps.json')

for i in range(0, length):
	with open(url[i]) as f:
		file_Data = f.read()
		json_Data = json.loads(file_Data)

		dataset = json_Data['activities-steps-intraday']['dataset']

	length = 24
	value_list = [0]*length
	time_list = [0]*length

	for iterator in dataset:
		time = int(iterator['time'][:2])
		value = int(iterator['value'])
		value_list[time] = value_list[time] + value

	for j in range(0, length):
		time_list[j] = j

	plt.plot(time_list, value_list, marker='o')

plt.title('Step Analysis by unknown')
plt.xlabel('Hour')
plt.ylabel('Step')
plt.savefig('step.jpg')