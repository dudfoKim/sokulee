import pyowm

owm = pyowm.OWM('3d40c6a36bc3a271792f52f6bfd61548')

observation1 = owm.weather_at_place('DaeJeon,KR')
daejeon = observation1.get_weather()
print "Daejeon : ", daejeon

observation2 = owm.weather_at_place('Seoul,KR')
Seoul = observation2.get_weather()
print "Seoul : ", Seoul