import urllib2
content = urllib2.urlopen("http://samples.openweathermap.org/data/2.5/forecast?lat=40&lon=139&appid=b1b15e88fa797225412429c1c50c122a1").read()

import json
j = json.loads(content)


#print j['list']

for value in j['list']:
    print value['dt']
