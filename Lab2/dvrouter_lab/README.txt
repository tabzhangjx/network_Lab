dv_router.py: # Add your code here!
scenarios/ contains simple topology(linear or candy).
sim/ is the network simulator. We should use the api and basics, and stay out of the core.

class packet: .src .dst .ttl .trace .outer_color .inner_color
foucs on api.py & basics.py

override(handle_rx, send)
use List store switch/hub-metric
use RoutingUpdate class in basics.py

Step 0: network connection
Step 1: flood=true, build router vector(3*n)
Step 2: override send method
Step 3: ping
   
what's the meaning of latency?

def send (self, packet, port, flood = False):

recursively update:
if the routing vector of A is updated, then A will send its routing vector to all node directly connected with A.

p1.list[p2]=[p3, p4]
p1:source, p2:destination, p3: portNumber, p4: minimumLatency


use latency
set portNumber
update & send RoutingUpdate packet [check]
test with ping






