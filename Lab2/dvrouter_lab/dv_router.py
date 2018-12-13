import sim.api as api
import sim.basics as basics
'''
Create your distance vector router in this file.
'''

INFINITY = 16

class DVRouter (api.Entity):
    def handle_timer(self):
        for i in self.routeTable.keys():
            if (((api.current_time() - self.routeTable[i][2]) <= self.ROUTE_TIMEOUT) or (
                    self.routeTable[i][2] == -1)):  # Checks if a route is expired or not
                self.send(basics.RoutePacket(i, self.routeTable[i][0]),
                          flood=True)  # updates neighbours with distance vector table
                if self.POISON_MODE == True:
                    self.send(basics.RoutePacket(i, INFINITY), self.routeTable[i][1], flood=False)
            else:
                if self.POISON_MODE == True:
                    self.p_reverse[i] = self.routeTable[i]  # populates poisoned reverse dictionary
                    self.send(basics.RoutePacket(i, INFINITY), self.routeTable[i][1], flood=False)
                del self.routeTable[i]  # deletes route from dictionary if it is expired.
        if self.POISON_MODE == True:
            for i in self.p_reverse.keys():
                self.send(basics.RoutePacket(i, INFINITY), port=None, flood=True)

        # NO_LOG = True # Set to True on an instance to disable its logging
        # POISON_MODE = True # Can override POISON_MODE here
        # DEFAULT_TIMER_INTERVAL = 5 # Can override this yourself for testing

    def __init__(self):
        """
        Called when the instance is initialized.
        You probably want to do some additional initialization here.
        """

        self.routeTable = {}  # dictionary of key:destination value:[latency,port,time_packet_was_received]
        self.neighbours = {}  # dictionary of key:port value:latency
        self.p_reverse = {}  # poisoned reverse dictionary (same key, value pairs as routeTable)
        self.start_timer()  # Starts calling handle_timer() at correct rate

    def handle_link_up(self, port, latency):
        self.neighbours[port] = latency  # populates neighbours dictionary
        for i in self.routeTable.keys():
            self.send(basics.RoutePacket(i, self.routeTable[i][0]), port, flood=False)
        """
        Called by the framework when a link attached to this Entity goes up.
        The port attached to the link and the link latency are passed in.

        """

    def handle_link_down(self, port):
        del self.neighbours[port]  # removes dictionary element from neighbours that has the value of the variable port
        if self.POISON_MODE == True:
            for i in self.routeTable.keys():
                if self.routeTable[i][1] == port:
                    self.p_reverse[i] = self.routeTable[i]
                    rp = basics.RoutePacket(i, INFINITY)
                    self.send(rp, port=None, flood=True)
                    del self.routeTable[i]
        else:
            for i in self.routeTable.keys():
                if self.routeTable[i][1] == port:
                    del self.routeTable[
                        i]  # removes dictionary element from routeTable that has the value of the variable port

        """
        Called by the framework when a link attached to this Entity does down.
        The port number used by the link is passed in.

        """

    def HandleRoute(self, packet, port):
        total = packet.latency + self.neighbours[port]
        addr = packet.destination
        if (total < INFINITY):
            if ((addr not in self.routeTable) or (self.routeTable[addr][0] > total)):
                pckt = basics.RoutePacket(addr,
                                          total)  # makes packet with destination and cost to get to that destination
                self.routeTable[addr] = [pckt.latency, port, api.current_time()]  # populate routeTable dictionary
                self.send(pckt, port,
                          flood=True)  # updates neighbours with the cost to get to the destination stored in the packet.
                if self.POISON_MODE == True:
                    ppckt = basics.RoutePacket(addr, INFINITY)
                    self.send(ppckt, port, flood=False)
            else:
                if self.routeTable[addr][1] == port:
                    self.routeTable[addr][2] = api.current_time()
                    if total > self.routeTable[addr][0]:
                        self.routeTable[addr][0] = total
                        pckt = basics.RoutePacket(addr, total)
                        self.send(pckt, port, flood=True)
                        if self.POISON_MODE == True:
                            ppckt = basics.RoutePacket(addr,
                                                       INFINITY)  # split horizon and poisoned reverse (advertising route to have a cost of infinity)
                            self.send(ppckt, port, flood=False)
            if addr in self.p_reverse and self.POISON_MODE == True:
                del self.p_reverse[addr]
        elif packet.latency >= INFINITY and self.POISON_MODE == True:
            for i in self.routeTable.keys():
                if (i == addr) and (self.routeTable[i][1] == port):
                    ppckt = basics.RoutePacket(addr, INFINITY)
                    self.send(ppckt, port, flood=True)
                    self.p_reverse[i] = self.routeTable[i]
                    del self.routeTable[i]

    def HandleDiscovery(self, packet, port):
        self.routeTable[packet.src] = [self.neighbours[port], port, -1]
        variable = basics.RoutePacket(packet.src, self.neighbours[port])
        self.send(variable, port, flood=True)

    def handle_rx(self, packet, port):
        """
        Called by the framework when this Entity receives a packet.
        packet is a Packet (or subclass).
        port is the port number it arrived on.
        You definitely want to fill this in.
        """
        if isinstance(packet, basics.RoutePacket):
            HandleRoute(self, packet, port)
        elif isinstance(packet, basics.HostDiscoveryPacket):
            HandleDiscovery(self, packet, port)
        else:
            if (packet.dst in self.routeTable and port != self.routeTable[packet.dst][
                1]):  # checks if destination actually exists and that it isn't directly connected to the current router.
                if self.routeTable[packet.dst][
                    0] <= INFINITY:  # checks to ensure the latency is less than or equal to 16
                    self.send(packet, self.routeTable[packet.dst][
                        1])  # sends packet out on the port corresponding to its intended destination



