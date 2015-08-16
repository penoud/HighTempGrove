import time
import HighTemp

myHighTemp = HighTemp.HighTemp() 
myHighTemp.setNtcPin(1)
myHighTemp.setThmcPin(0)
#myHighTemp.setDebug()
while(1):
	print "NTC temp = " + str(myHighTemp.getNtcTemp())
	time.sleep(0.2) 
	print "Thmc temp = " + str(myHighTemp.getThmcTemp())
	time.sleep(0.2) 

