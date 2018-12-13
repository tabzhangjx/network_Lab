import sim.api as api
import sim.basics as basics
'''
Create your distance vector router in this file.
p1.routingVector[p2]=[p3, p4]
p1:source, p2:destination, p3, p4: minimumLatency
'''

class DVRouter (api.Entity):
    def handle_timer(self):


    def send_RUP():
    	if self.Route_table.has_key(self):
    		pass
    	else:
    		self.Route_table[self]=[0, 0]
    	a = RoutingUpdate()
    	keys_ = Route_table.keys()
		for i in keys_:
   			a.add_destination(i, self.Route_table[i])
   		self.send(a, ports, flood = False)

    def RouteUpdate(self, RUP):
    	def same_con(i, j):
    		if i==self:
    			pass
    		else:
    			if self.Route_table[i][1]=RUP[i][1]:
    				self.Route_table[i][2]=RUP[i][2]+1
    			else:
    				if self.Route_table[i][2]>RUP[i][2]+1:
    					self.Route_table[i][1]=RUP[i][1]
    					self.Route_table[i][2]=RUP[i][2]+1
    			#更新时存在一个问题

    	def diff_con(i, j):
    		self.Route_table[i][1]=RUP[i][1]
    		self.Route_table[i][2]=RUP[i][2]+1

    	keys_ = RUP.keys()
    	for i in keys_:
    		if self.Route_table.has_key(i):
    			same_con(i, i)
    		else:
    			diff_con(i, i)


    def __init__(self):


   a = RoutingUpdate()
   for i in route_table:
   	a.adddestnation(i)