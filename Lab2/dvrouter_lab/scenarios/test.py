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
    host_type.create('ha')
    host_type.create('hb')
    host_type.create('hc')
    host_type.create('hd')


    topo.link(ha, sac1)
    topo.link(sac1, sac2)
    topo.link(sac2, sac3)
    topo.link(sac3, sac4)
    topo.link(sac4, sac5)
    topo.link(sac5, sac6)
    topo.link(sac6, sac7)
    topo.link(sac7, sac8)
    topo.link(sac8, hc)

    topo.link(hb, sbd1)
    topo.link(sbd1, sbd2)
    topo.link(sbd2, sbd3)
    topo.link(sbd3, sbd4)
    topo.link(sbd4, hd)

    topo.link(hd, sdc1)
    topo.link(sdc1, sdc2)
    topo.link(sdc2, hc)

    topo.link(ha, sab1)
    topo.link(sab1, sab2)
    topo.link(sab2, sab3)
    topo.link(sab3, hb)

    topo.link(hb, sbc1)
    topo.link(sbc1, sbc2)
    topo.link(sbc2, hc)