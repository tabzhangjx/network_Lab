class router:
	'class a router, including datas and methods'

	#data
  name='R'
  num_ports=0
  ports=[]
  item=[]
  route_table=[]

	#method
	def __init__(self, name):
    self.name=name
    num_ports=0
    ports=[]
    item=[]
    item.append(name)
    item.append(0)
    item.append(0)
    route_table=[]
    route_table.append(item)

  def update_routing(self, update_routing_packet):
    for i in update_routing_packet:
      flag = 0
      for j in route_table:
        if i[1]==j[1]:
          same_con(i, j)
          flag=1
          break
      if flag==0:
        diff_con(i, j)
        

  def send_urp(self):
    return route_table


  def send_data(self):
    return "ping"

  def show_route_table(self):
    for i in route_table:
      print(i)

class net_w:
  'set of routers'

  num_routers=0
  router_set=[]


	def __init__(self, name):
    self.name = name
    num_routers=0
    router_set=[]

  def creat_router(self, name):


  def delete_router():


