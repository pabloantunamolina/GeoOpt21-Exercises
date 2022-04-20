import rhino3dm as rg
import networkx as nx
import random

def createGridGraph(x, y):

    M = nx.grid_2d_graph(x,y)
    return M


def addRandomWeights(G):

    NG = nx.Graph()
    for u,v,data in G.edges(data=True):
        #w = data['weight'] if 'weight' in data else 1.0
        w = random.randint(1,10)
        if NG.has_edge(u,v):
            NG[u][v]['weight'] += w
        else:
            NG.add_edge(u, v, weight=w)
    
    return NG

def getNodes(G, layout = 1):

    if layout == 0 : lay =  nx.kamada_kawai_layout(G)
    elif layout == 1 : lay =  nx.circular_layout(G)
    elif layout == 2 : lay =  nx.shell_layout(G)
    elif layout == 3 : lay =  nx.spiral_layout(G)
    else: lay = nx.planar_layout(G)

    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)

    return nodes


def getEdges(G, layout = 1):

    if layout == 0 : lay =  nx.kamada_kawai_layout(G)
    elif layout == 1 : lay =  nx.circular_layout(G)
    elif layout == 2 : lay =  nx.shell_layout(G)
    elif layout == 3 : lay =  nx.spiral_layout(G)
    else: lay = nx.planar_layout(G)

    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    return edges


def lesMiserablesGeo():

    G = nx.les_miserables_graph()
    G_layout = nx.layout.fruchterman_reingold_layout(G)

    nodes = []
    for d in G_layout.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)

    edges = []
    for e in G.edges:
        p1 = rg.Point3d(G_layout[e[0]][0], G_layout[e[0]][1], 0)
        p2 = rg.Point3d(G_layout[e[1]][0], G_layout[e[1]][1], 0)
        line = rg.LineCurve(p1, p2)
        edges.append(line)
    
    return nodes, edges


def lesMiserablesW():

    G = nx.les_miserables_graph()

    cent_degree = dict(nx.degree(G))
    weight = list(cent_degree.values())
    
    return weight


def graphFromPt(pnt, con):

    G = nx.Graph()
    num = [x for x in range(len(pnt))]
    G.add_nodes_from(num)
    edges = []
    for i in range(len(pnt)):
        for j in range(len(con[i])):
            a = pnt[i]
            b = con[i][j]
            e = (a, b)

            edges.append(e)

    G.add_edges_from(edges)

    return G


def graphPtList(pnt, con, part):

    G = nx.Graph()
    num = [x for x in range(len(pnt))]
    G.add_nodes_from(num)

    con_split = [con[i:i+part] for i in range(0, len(con), part)]

    edges = []
    for i in num:
        for j in range(len(con_split[i])):
            a = pnt[i]
            b = con_split[i][j]
            e = (a, b)

            edges.append(e)

    G.add_edges_from(edges)

    return G


l = [1,2,3,4,5,6,7,8,9]
chunks = [l[x:x+3] for x in range(0, len(l), 3)]
print(chunks)

"""
G = createGridGraph(3,3)
GW = addRandomWeigrhs(G)

nodes = getNodes(G)
edges = getEdges(G)
"""


