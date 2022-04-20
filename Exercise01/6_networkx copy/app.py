from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createGraph",
    name = "Create Graph",
    inputs=[
        hs.HopsInteger("Count X", "X", "Number of node in X", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Count Y", "Y", "Number of node in Y", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Layout", "L", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 0),


    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def createGraph(X, Y, layout):

    G = geo.createGridGraph(X, Y)
    GW = geo.addRandomWeights(G)

    nodes = geo.getNodes(GW, layout)
    edges = geo.getEdges(GW, layout) 

    return nodes, edges



@hops.component(
    "/lesMiserablesGraph",
    name = "Create Graph",
    inputs=[],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST),
    ]
)
def lesMiserables():

    nodes, edges = geo.lesMiserablesGeo()

    return nodes, edges


@hops.component(
    "/lesMiserablesGraphW",
    name = "Create Graph",
    inputs=[],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST),
       hs.HopsInteger("Weights","W","List of Weights ", hs.HopsParamAccess.LIST),    
    ]
)
def lesMiserables():

    nodes, edges = geo.lesMiserablesGeo()
    w = geo.lesMiserablesW()

    return nodes, edges, w


@hops.component(
    "/RhinoNx",
    name = "Create Graph",
    inputs=[
        hs.HopsPoint("Points", "P", "List of points", hs.HopsParamAccess.LIST),
        hs.HopsInteger("Connections", "C", "Tree of connections per node", hs.HopsParamAccess.TREE),
        hs.HopsInteger("Layout", "L", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 1),
    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def rhinoNx(pnt, con, layout):

    G = geo.graphFromPt(pnt, con)

    nodes = geo.getNodes(G, layout)
    edges = geo.getEdges(G, layout) 

    return nodes, edges


@hops.component(
    "/RhinoNxList",
    name = "Create Graph",
    inputs=[
        hs.HopsPoint("Points", "P", "List of points", hs.HopsParamAccess.LIST),
        hs.HopsInteger("Connections", "C", "Tree of connections per node", hs.HopsParamAccess.LIST),
        hs.HopsInteger("Sublist", "S", "Partition list size", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("Layout", "L", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 1),
    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def rhinoNx(pnt, con, part, layout):

    G = geo.graphPtList(pnt, con, part)

    nodes = geo.getNodes(G, layout)
    edges = geo.getEdges(G, layout) 

    return nodes, edges




if __name__== "__main__":
    app.run(debug=True)