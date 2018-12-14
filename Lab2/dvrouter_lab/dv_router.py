from sim.api import *
from sim.basics import *

"""
Create your distance vector router in this file.
"""
class DVRouter (Entity):
    def __init__(self):
        # Add your code here!
        self.routingVector=dict()
        self.updatedFlag = False
        #print('type:%s, name:%s' % (type(self), self.name))
        #print(self)
        '''
        usage
        p1.routingVector[p2]=[p3, p4]
        p1:source, p2:destination, p3: portNumber, p4: minimumLatency
        '''
        pass
    
    def ping (self, dst, data=None):
        """ Sends a Ping packet to dst. """
        port = self.routingVector[dst.name][0]
        self.send(Ping(dst, data=data), port, flood=False)
    
    def handle_rx (self, packet, port):
        """
        Just sends the packet back out of every port except the one it came
        in on.
        """
        
        #Initialize routingVector     
        if self.name not in self.routingVector:
            self.routingVector[self.name]=[-1, 0]
        
        #Create RoutingUpdate package  
        p = RoutingUpdate()
        for dst in self.routingVector:
            p.add_destination(dest=dst, distance=self.routingVector[dst][1])
        
        if type(packet)==DiscoveryPacket :
            print("Discovering")
            #Send RoutingUpdate package
            for i in range(self.get_port_count()):
                self.send(p, i, flood=False)
            #Send DiscoveryPacket
            self.send(packet, port, flood=True)
            
        elif type(packet)==RoutingUpdate :
            #update routingVector
            self.updatedFlag = False
            p = packet
            
            for dst in p.paths:
                distance = p.paths[dst]
                if dst not in self.routingVector:
                    self.routingVector[dst]=[port, distance+1]
                    #print("dddddddddddddddddddddddddddd",self,port)
                    self.updatedFlag = True
                else:
                    if (distance + 1) < self.routingVector[dst][1] :
                        self.routingVector[dst]=[port, distance+1]
                        self.updatedFlag = True
            
            #if routingVector is updated, send RoutingUpdate Packet to neighbours         
            if self.updatedFlag:
                p = RoutingUpdate()
                for dst in self.routingVector:
                    p.add_destination(dest=dst, distance=self.routingVector[dst][1])
                    
                for i in range(self.get_port_count()):
                    self.send(p, i, flood=False)
                          
            #drop packet
            
            pass
        elif type(packet)==Ping :
            print("PPPTTT!!!",packet)
            if packet.dst is not self:
                p = Ping(packet.dst, data=packet.data)
                p.ttl = packet.ttl
                
                #print(packet.dst.name, type(packet.dst.name))
                #print(packet.dst[2])
                port = self.routingVector[packet.dst.name][0]
                self.send(p, port, flood=False)
                #self.send(p, flood=True)
            #print("DST:!!!"packet.dst)
            #find shortest path via routingVector
            pass
         
        
        

        
        
        