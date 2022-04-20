from flask import Flask
import ghhops_server as hs
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/spheresFromPt22",
    name = "Spheres from points",
    inputs=[
        hs.HopsPoint("Centers", "C", "Centers", hs.HopsParamAccess.LIST),
        hs.HopsNumber("Radi", "R", "Radi", hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsBrep("Spheres", "S", "Spheres", hs.HopsParamAccess.LIST),
    ],
)
def sphereTest(centers: rg.Point3d, radi):
    spheres = []
    for i in range(len(radi)):
        s = rg.Sphere.ToBrep(rg.Sphere(centers[i], radi[i]))
        spheres.append(s)
    
    return spheres


if __name__== "__main__":
    app.run(debug=True)