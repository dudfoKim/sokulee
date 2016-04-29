# -*- coding : utf8 -*-

import csv
import matplotlib
import json

matplotlib.use('Agg')

import matplotlib.pyplot as plt

length = 11
url = []
chart = []
time_count = [0] * 24

for i in range(1, length):
	if(i<10):
		url.append('05_2016040' + str(i) + '_heart.json')
	else:
		url.append('05_201604' + str(i) + '_heart.json')
'''
for i in range(1, length):
	with open(url[i-1]) as f:
		file_Data = f.read()
		json_Data = json.loads(file_Data)

		dataset = json_Data['activities-heart-intraday']['dataset']

	length = 24
	value_list = [0]*length
	time_list = [0]*length

	for iterator in dataset:
		time = int(iterator['time'][:2])
		value = int(iterator['value'])
		value_list[time] = value_list[time] + value
		time_count[time] = time_count[time] + 1

	for j in range(0, length):
		value_list[j] = value_list[j] / time_count[j]
		time_list[j] = j

	plt.plot(time_list, value_list, marker='o')

plt.title('Heart Analysis by YLKim')
plt.xlabel('Hour')
plt.ylabel('Heart')
plt.savefig('heart.jpg')
'''

for i in range(0, length):
	with open(url[i]) as f:
		file_Data = f.read()
		json_Data = json.loads(file_Data)

		temp = json_Data['activities-heart-intraday']['dataset']

	length = 24
	time_list = [0]*length

	temp_list = temp.groupby(['time']).mean()
	value_list = temp_list['value']

	for j in range(0, length):
		time_list[j] = j

	plt.plot(time_list, value_list, marker='o')

plt.title('Heart Analysis by unknown')
plt.xlabel('Hour')
plt.ylabel('Heart')
plt.savefig('heart.jpg')