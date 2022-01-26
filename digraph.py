import  networkx as nx 
import matplotlib.pyplot as plt

def signal_transduction_network(nd,size):
    g=nx.DiGraph()
    g.add_edges_from(nd)
    pos=nx.spring_layout(g)
    fig = plt.figure(figsize=size)
    nx.draw_networkx_nodes(g,pos,node_size=100,node_color='yellow')
    nx.draw_networkx_edges(g,pos,edgelist=g.edges(),edge_color='black')
    nx.draw_networkx_labels(g,pos)
    plt.show()
def file_handle(file):
    data = open(file, "r")
    rd=data.read()
    nd=rd.split(",")
    nd1,nd2=nd[0],nd[1]
    node1=nd1.split(" ")
    node2=nd2.split(" ")
    nd_pair=zip(node1,node2)
    nodes=list(nd_pair)
    return nodes



