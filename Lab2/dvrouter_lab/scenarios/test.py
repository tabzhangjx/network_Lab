import sim
from sim.core import CreateEntity, topoOf
from sim.basics import BasicHost
from hub import Hub
import sim.topo as topo

def create (switch_type = Hub, host_type = BasicHost):
    """
    B-------sbd1-------sbd2-------sbd3------sbd4----------------D
    |\                                                          |
    | \                                                         |
    |  \                                                        |
    sab1\                                                       sdc1
    |    \                                                      |
    |     \                                                     |
    |      \                                                    |
    sab2    sbc1-------------------------------------sbc2       |
    |                                                    \      sdc2
    |                                                     \     |
    |                                                      \    |
    sab3                                                    \   |
    |                                                        \  |
    |                                                         \ |
    |                                                          \|
    A---sac1---sac2---sac3---sac4---sac5---sac6---sac7---sac8---C
    """

    switch_type.create('sbd1')
    switch_type.create('sbd2')
    switch_type.create('sbd3')
    switch_type.create('sbd4')
    switch_type.create('sab1')
    switch_type.create('sab2')
    switch_type.create('sab3')
    switch_type.create('sbc1')
    switch_type.create('sbc2')
    switch_type.create('sdc1')
    switch_type.create('sdc2')
    switch_type.create('sac1')
    switch_type.create('sac2')
    switch_type.create('sac3')
    switch_type.create('sac4')
    switch_type.create('sac5')
    switch_type.create('sac6')
    switch_type.create('sac7')
    switch_type.create('sac8')
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
    topo.link(s1, h5)
    topo.link(s1, h6)