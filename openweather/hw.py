import urllib
import datetime
import matplotlib
import matplotlib.pyplot as plt
import json

city = ['Seoul, kr', 'Daejeon, kr', 'Daegue, kr', 'Busan, kr', 'Chuncheon, kr', 'Jeonju, kr', 'Gwangju, kr']
index = []
city_list = []
temperature_list = []
data = []

for i in range(0, len(city)):
	index.append(i+1)
	url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city[i]
	u = urllib.urlopen(url) 
	data = u.read() 
	j = json.loads(data) 

	print "---------------------\n"

	name = j["name"] 
	print "[City name]\n" + name + '\n'
	city_list.append(name)

	dt = j["dt"]
	current_time = datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M:%S')
	print "[Data receiving time]"
	print current_time + '\n'

	main = j["main"] 
	temp = main["temp"] 
	temperature = int(temp)-273.15
	print "[temperature]" 
	print temperature
	temperature_list.append(temperature)

	weather = j["weather"] 
	main = weather[0] 
	print "\n[weather]\n" + main["description"] + '\n'

plt.title('Real-Time Temperature\t[' + current_time + ']')
plt.plot(index, temperature_list, 'ro')
plt.xticks(index, city_list)
plt.margins(0.2)
plt.show()