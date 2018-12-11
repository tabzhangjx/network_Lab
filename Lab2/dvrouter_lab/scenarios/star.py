import sim
from sim.core import CreateEntity, topoOf
from sim.basics import BasicHost
from hub import Hub
import sim.topo as topo

def create (switch_type = Hub, host_type = BasicHost):
    """
    h1-----            ---------h2
           \          /
            \        /
             \      /
              \    /
    h3--------- s1 -------------h4
               /  \
              /    \
             /      \
    h5-------        ----------h6
    """

    switch_type.create('s1')

    host_type.create('h1')
    host_type.create('h2')
    host_type.create('h3')
    host_type.create('h4')
    host_type.create('h5')
    host_type.create('h6')


    topo.link(s1, h1)
    topo.link(s1, h2)
    topo.link(s1, h3)
    topo.link(s1, h4)
    topo.link(s1, s5)
    topo.link(s1, s6)