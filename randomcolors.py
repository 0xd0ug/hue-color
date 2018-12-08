import time
from phue import Bridge
import random

random.seed()
b=Bridge('192.168.2.120')
#b.connect()
lights=b.get_light_objects()
while True:
    change=random.randint(-10,10)/200.0
    axis=random.randint(1,2)
    for x in range(1,random.randint(1,10)):
      light=random.randint(8,11)
      x=lights[light].xy[0]
      y=lights[light].xy[1]
      print "Changing " + lights[light].name,
      print "by",
      print change
      if axis==1:
          x+=change
      else:
          y+=change
      lights[light].xy=[x,y]
      time.sleep(5)
