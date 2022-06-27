from bus import Bus
bus = Bus('Bus',4,120,'v5555')
#bus.color = 'Blue'
bus.set_colour('Blue')
#bus.capacity = 34
bus.set_capacity(34)
bus.bus_detail()

from mortorcycle import Mortorcycle
bike = Mortorcycle('Mortorcycle',2,100,'v5432')
#bike.cc =1200
bike.set_cc(1200)
bike.bike_detail()