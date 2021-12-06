import maya.cmds as cmds
import random
import math

#cmds.listAttr('polyPlane1')

if 'myWin' in globals():
    if cmds.window(myWin, exists=True):
        cmds.deleteUI(myWin, window=True)

myWin = cmds.window(title="Terrain Generator")

### PLANE  ##
cmds.frameLayout(collapsable=True, label='Creer un terrain plat')
###user set width and depth
largeT = cmds.floatSliderGrp('PlaneWidth', label='Largeur', field=True, min=5, max=40, value=20)
longT = cmds.floatSliderGrp('PlaneLong', label='Longueur', field=True, min=5, max=40, value=20)
#user set subDiv's
subLar = cmds.intSliderGrp('SdWidth', label='Subdivision Largeur', field=True, min=5, max=40, value=10)
subLong = cmds.intSliderGrp('SdLong', label='Subdivision Longueur', field=True, min=5, max=40, value=10)

cmds.columnLayout()
cmds.button(label='Creer Terrain', command='createPlane()')
cmds.button(label='Supprimer Terrain', command='cmds.delete()')

cmds.setParent('..')
cmds.setParent('..')

### HEXAGONE ##
cmds.frameLayout(collapsable=True, label='Creer un terrain hexagonal')
###user set width and depth
heightHexa = cmds.floatSliderGrp('HeightHexa', label='Hauteur du socle', field=True, min=0.5, max=3, value=1)
longHexa = cmds.intSliderGrp('length', label='Quantite en longueur', field=True, min=5, max=24, value=7)
largeHexa = cmds.intSliderGrp('Width', label='Quantite en largeur', field=True, min=5, max=24, value=7)

cmds.optionMenu('hexagone', label='Type Hexagone')
for item in range(6):
    cmds.menuItem(item)

cmds.columnLayout()
cmds.button(label='Creer Hexagone', command='createPlane()')
cmds.button(label='Supprimer Hexagone', command='cmds.delete()')

cmds.setParent('..')
cmds.setParent('..')


## Modifications to terrain
cmds.frameLayout(collapsable=True, label='Modifications')
montAmp = cmds.floatSliderGrp('MontAmp', label='Amplitude', field=True, min=1, max=3, value=1)
mound = cmds.button(label='Creer monticule', command=('creerMont()'), en=True)


cmds.setParent('..')
cmds.setParent('..')

## colouring of hte terrain presets
cmds.frameLayout(collapsable=True, label='Colour Plane')
cmds.rowLayout( numberOfColumns=5)
cmds.button(label='Executer', command=('colourDesert()'))
cmds.optionMenu('hexagone', label='Type de terre')
for item in range(7):
    cmds.menuItem(item)

#for personal colour selection
cmds.colorSliderGrp('planeColour', label='Colour', rgb=(1.0,1.0,1.0))
cmds.button(label='SetColour', command=('colourChoice()'))

cmds.setParent('..')
cmds.setParent('..')

#this function is creates a fractal subdivision simulation of the diamond square algorithm
cmds.frameLayout(collapsable=True, label='Fractal Modifications')
cmds.columnLayout()
fbutton = cmds.button(label='Ajouter Fractal Noise', command=('addNoise()'), en=True)

cmds.setParent('..')
cmds.setParent('..')

#smooth function for hill looking terrains
cmds.frameLayout(collapsable=True, label='Smooth Plane')
smooth = cmds.button(label='Smooth', command=('smoothPlane()'))
cmds.attrFieldSliderGrp('lanneLong', label='Lingueur', min=5, max=40)

cmds.setParent('..')
cmds.setParent('..')


cmds.showWindow(myWin)


getlargeT = cmds.floatSliderGrp(largeT, q=True, v=True)
getlongT = cmds.floatSliderGrp(longT, q=True, v=True)
getsubLar = cmds.intSliderGrp(subLar, q=True, v=True)
getsubLong = cmds.intSliderGrp(subLong, q=True, v=True)
getheightHexa = cmds.floatSliderGrp(heightHexa, q=True, v=True)
getlongHexa =  cmds.intSliderGrp(longHexa, q=True, v=True)
getlargeHexa = cmds.intSliderGrp(largeHexa, q=True,v=True)


def setTerrain(largeur, longueur):
    cmds.setAttr('pPlane1.translateX',largeur)
    cmds.setAttr('pPlane1.translateY', longueur)

cmds.floatSliderGrp(largeT, e=True, dc=lambda x: setTerrain(getlargeT, getlongT))

    # def boolSwitch(self):
    #     if(cmds.objExists('myRef')):
    #     print 'myRef Exists\n'
    #     cmds.delete('myRef')

    #     cmds.select(terrainMesh)
    #     cmds.delete()

    #     mod = False
    #     mound = cmds.button(label='Create Mounds', command=('creerMont()'), en=True)
    #     ditch = cmds.button(label='Create Ditchs', command=('creerFosse()'), en=True)
    #     count = 0

    #    global PWidth
    #     PWidth = cmds.intSliderGrp('PlaneWidth', q=True, v=True)
    #     global PDepth
    #     PDepth = cmds.intSliderGrp('PlaneDepth', q=True, v=True)
    #     global SubWidth
    #     SubWidth = cmds.intSliderGrp('SdWidth', q=True, v=True)
    #     global SubDepth
    #     SubDepth = cmds.intSliderGrp('SdDepth', q=True, v=True)

    #     height = cmds.intSliderGrp('MoundAmp', q=True, v=True)

    #     #step 1 : create a poplygonal mesh
###########################################
###########################################
##### T E R R A I N  G E N E R A T O R ####
###########################################
###########################################

# class Terrain:
#     #initializing globals for access in all functions
#     def __init__(self):
#         self.vCount = 0
#         self.fCount = 0
#         self.terrainMesh = 'Nothing'
#         self.SubWidth = 0
#         self.SubDepth = 0
#         self.tallness = 0
#         self.count = 0
#         self.mod = False
#         self.PWidth = 0
#         self.PDepth = 0
#         self.bCount = 0

#     ## this function is to handle the UI enable and disable options
#     ## depending on if the object has deleted or a new scene is created

#     ##################
#     ###CREATE PLANE###
#     ##################
#     def createPlane(self, planeName = 'perturbedMesh'):

#         self.terrainMesh = planeName
#         cmds.polyPlane(w=PWidth*2, h=PDepth*2, sx=SubWidth, sy=SubDepth, n=self.terrainMesh)

#         #step 2 obtain the vertex and face count so we can then lop through the verticies and faces

#         self.vCount = cmds.polyEvaluate(v=True)
#         self.fCount = cmds.polyEvaluate(f=True)


#     ###################
#     ### CREATE HILL ###
#     ###################
#     def creerMont(self):

#         cmds.disable(build)

#         for face in xrange(0,self.fCount,3):
#             noise = self.perlin(face)

#             ##if noise returns a 1 then we will print ONE, this is for debugging as it only happens when the result is = 0, which shouldnt happen
#             if(noise == 1):
#                 print 'ONE'
#             ##if the noise returns a 2 then
#             if(noise == 2):
#                 print 'Two'
#                 #gather a list of the faces nearby verticies
#                 vtxLst = cmds.polyInfo(self.terrainMesh + '.f[' + str(face) + ']', faceToVertex=True)
#                 vtxIdx = str(vtxLst[0]).split()
#                 #select a vertex randomly
#                 loc = random.randint(2,5);
#                 vtx = vtxIdx[loc]
#                 #select that vertex
#                 cmds.select(terrainMesh+'.vtx['+vtx+']')
#                 #randomly creates a value between 0.0 and 1.0 to devide by
#                 rn = random.random()
#                 tmpValueY = height#*(math.sin(face/rn))

#                 #This control makes sure all values are positive or nothing will happen
#                 if(tmpValueY < 0):
#                     tmpValueY = 0.0
#                 #moves the location of the vertex vertically
#                 cmds.move(0.0, tmpValueY, 0.0, r=True)

#             #if the noise is returned with 3, do the same thing as if noise is 2, but a different random iterator to devide by, which will create larger hills
#             if(noise == 3):
#                 print 'three'


#     ####################
#     ### CREATE DITCH ###
#     ####################
#     #function works seperatly then the above create hill
#     #this is because I am still experimenting with how the perlion noise function works before applying the algorithm here as awell
#     #this one is a simulation random uniform selection that is similar to the results of perlin noise, but not particularly running the perling noise funtion
#     def creerFosse(self):
#         height = cmds.intSliderGrp('MoundAmp', q=True, v=True)
#         cmds.disable(build)
#         for face in xrange(0,fCount,3):
#             noise = perlin(face)

#             ##if noise returns a 1 then we will print ONE, this is for debugging as it only happens when the result is = 0, which shouldnt happen
#             if(noise == 1):
#                 print 'ONE'
#             ##if the noise returns a 2 then
#             if(noise == 2):
#                 print 'Two'

#             #if the noise is returned with 3, do the same thing as if noise is 2, but a different random iterator to devide by, which will create larger hills
#             if(noise == 3):
#                 print 'three'
#                 #gather a list of the faces nearby verticies
#                 vtxLst = cmds.polyInfo(terrainMesh + '.f[' + str(face) + ']', faceToVertex=True)
#                 vtxIdx = str(vtxLst[0]).split()
#                 #select a vertex randomly
#                 loc = random.randint(2,5);
#                 vtx = vtxIdx[loc]
#                 #select that vertex
#                 cmds.select(terrainMesh+'.vtx['+vtx+']')
#                 #randomly creates a value between 0.0 and 1.0 to devide by
#                 rn = random.random()
#                 tmpValueY = height#*(math.sin(face/rn))

#                 #This control makes sure all values are positive or nothing will happen
#                 if(tmpValueY < 0):
#                     tmpValueY = 0.0
#                 #moves the location of the vertex vertically
#                 cmds.move(0.0, -tmpValueY, 0.0, r=True)

#     ################
#     ###PolySmooth###
#     ################
#     def smoothPlane(self):
#         cmds.select(self.terrainMesh)
#         #checking to make sure the poly count isnt too large
#         self.vCount = cmds.polyEvaluate(v=True)
#         self.fCount = cmds.polyEvaluate(f=True)

#         #if(fCount < 2500):
#         cmds.polySmooth(n=self.terrainMesh)
#         #gotta reset the global count
#         self.vCount = cmds.polyEvaluate(v=True)

#         self.fCount = cmds.polyEvaluate(f=True)

#     ####################
#     ###COLOUR TERRAIN###
#     ####################
#     ###    Choice    ###
#     ####################
#     def colourChoice():
#         rgb = cmds.colorSliderGrp('planeColour', q=True, rgbValue=True)
#         colourSurface(rgb[0],rgb[1],rgb[2])

#     ####################
#     ###COLOUR TERRAIN###
#     ####################
#     ###   Function   ###
#     ####################
#     def colourSurface(r,g,b):

#         nsTmp = 'Plane' + str(random.randint(1000,9999))    #makes it easier to keep track of object we are creating witihin this function

#         cmds.namespace(add=nsTmp)
#         cmds.namespace(set=nsTmp)

#         myShader = cmds.shadingNode('lambert', asShader=True, name='blckMat')

#         cmds.setAttr(nsTmp+':blckMat.color', r, g, b, typ='double3')
#         cmds.select(self.terrainMesh)

#         cmds.hyperShade(assign=(nsTmp+':blckMat'))

#         cmds.namespace(removeNamespace=':'+nsTmp, mergeNamespaceWithParent=True) #now can leave the namespace


#     ##############################
#     #### RANDOM FRACTAL NOISE ####
#     ##############################
#     def addNoise(self):
#         #disable the other commands when the noise is modified to the terrain
#         mod = True

#         #subdivide the facet
#         cmds.polyTriangulate(self.terrainMesh ,ch=False)

#         # ensure that the whole mesh is selected
#         cmds.select(self.terrainMesh)
#         ##recalculations of the global variables
#         self.vCount = cmds.polyEvaluate(v=True)
#         self.fCount = cmds.polyEvaluate(f=True)


#         #fractal subdivisde ggoes through every face
#         for face in range (1, self.fCount):
#             facetNum = str(face)
#             #select the face
#             cmds.select(self.terrainMesh+'.f['+facetNum+']')

#             #get vertex list and select one
#             vtxLst = cmds.polyInfo(self.terrainMesh + '.f[' + str(face) + ']', faceToVertex=True)
#             vtxIdx = str(vtxLst[0]).split()

#             vtxB = cmds.getAttr(self.terrainMesh + '.vt[' + vtxIdx[2] + ']')

#             print(vtxB)
#             #create some random values to be aded at the random location
#             tmpValueX = random.uniform(-0.2, 0.2)
#             tmpValueY = random.uniform(-0.3, 0.3)
#             tmpValueZ = random.uniform(-0.2, 0.2)

#             #moves the vertex to add some noise to the terrain
#             cmds.move(tmpValueX, tmpValueY, tmpValueZ, r=True)

#         #counting to make sure that the function doesnt calculate too many faces
#         count = count + 1

#         #if count gets to twice
#         #disables the button to prevent the script from calculating for a large period of time
#         if(count == 3):
#             cmds.disable(fbutton)

#         #disables the mound and ditch commands when the face count increases because the results are ugly
#         if (mod == True):
#             cmds.disable(mound)
#             cmds.disable(ditch)
#             cmds.disable(build)


#     ######################
#     #### PERLIN NOISE ####
#     ######################
#     def perlin(self, sdface):
#         #PERLIN GRID DEFINITION
#         #going throuhg each face and extracting its verticies so that I can apply perlin noise
#         vtxLst = cmds.polyInfo(self.terrainMesh + '.f[' + str(self.face) + ']', faceToVertex=True)
#         vtxIdx = str(vtxLst[0]).split()

#         #grab the faces veticies
#         vtxA = cmds.getAttr(self.terrainMesh + '.vt[' + vtxIdx[2] + ']')
#         vtxB = cmds.getAttr(self.terrainMesh + '.vt[' + vtxIdx[3] + ']')
#         vtxC = cmds.getAttr(self.terrainMesh + '.vt[' + vtxIdx[4] + ']')
#         vtxD = cmds.getAttr(self.terrainMesh + '.vt[' + vtxIdx[5] + ']')

#         #get the x y z values of each
#         newvtxA = vtxA[0]
#         vtxAx = newvtxA[0]
#         vtxAy = newvtxA[1]
#         vtxAz = newvtxA[2]

#         newvtxB = vtxB[0]
#         vtxBx = newvtxB[0]
#         vtxBy = newvtxB[1]
#         vtxBz = newvtxB[2]

#         newvtxC = vtxC[0]
#         vtxCx = newvtxC[0]
#         vtxCy = newvtxC[1]
#         vtxCz = newvtxC[2]

#         newvtxD = vtxD[0]
#         vtxDx = newvtxD[0]
#         vtxDy = newvtxD[1]
#         vtxDz = newvtxD[2]

#         #gathering random input point for each gradient calculation
#         inputx = random.uniform(-1.0,1.0)
#         inputy = random.uniform(-1.0,1.0)
#         inputz = random.uniform(-1.0,1.0)

#         #getting gradient positions for 4 surrounding points, only extracting x and z here as the transformation to y happens depending on a if it is a ditch or hill
#         ax0 = vtxAx - int(vtxAx)
#         ax1 = ax0 + 1.0
#         ay0 = vtxAy - int(vtxAy)
#         ay1 = ay0 + 1.0

#         bx0 = vtxBx - int(vtxBx)
#         bx1 = bx0 + 1.0
#         by0 = vtxBy - int(vtxBy)
#         by1 = by0 + 1.0

#         cx0 = vtxCx - int(vtxCx)
#         cx1 = cx0 + 1.0
#         cy0 = vtxCy - int(vtxCy)
#         cy1 = cy0 + 1.0


#         dx0 = vtxDx - int(vtxDx)
#         dx1 = cx0 + 1.0
#         dy0 = vtxDy - int(vtxDy)
#         dy1 = cy0 + 1.0

#         #calculating gradient with Dot Product
#         gradA = self.gradient(ax0,ax1,ay0,ay1, inputx,inputy)
#         gradB = self.gradient(bx0,bx1,by0,by1, inputx,inputy)
#         gradC = self.gradient(cx0,cx1,cy0,cy1, inputx,inputy)
#         gradD = self.gradient(dx0,dx1,dy0,dy1, inputx,inputy)

#         #calcualte linear distance of vectors
#         distA = self.distance(vtxAx,vtxAy,vtxAz)
#         distB = self.distance(vtxBx,vtxBy,vtxBz)
#         distC = self.distance(vtxCx,vtxCy,vtxCz)
#         distD = self.distance(vtxDx,vtxDy,vtxDz)


#         #dot Product
#         dpA = (distA[0] * gradA[0]) + (distA[1] * gradA[1])# + (distA[2] * gradA[2])
#         dpB = (distB[0] * gradB[0]) + (distB[1] * gradB[1])# + (distB[2] * gradB[2])
#         dpC = (distC[0] * gradC[0]) + (distC[1] * gradC[1])# + (distC[2] * gradC[2])
#         dpD = (distD[0] * gradD[0]) + (distD[1] * gradD[1])# + (distD[2] * gradD[2])

#         #INTERPOLATION
#         val = self.lerp(self.lerp(self.lerp(dpA,dpB),self.lerp(dpB,dpC)), self.lerp(self.lerp(dpC,dpD),self.lerp(dpD,dpA)))

#         #depending on the if the interpolation result is greater than or less than zero or equal
#         #noise will be returned in either 1 2 or 3, which decides the amplitude of the hill at this location
#         if(val > 0.1):
#             noise = 2
#         elif(val < 0.1):
#             noise = 3
#         else:
#             noise = 1

#         return noise


#     ###calculate linear distance
#     def distance(self,x,y,z):
#         #apply a random value to be tested to location of
#         ix = x * random.uniform(-1.0,1.0)
#         iy = x * random.uniform(-1.0,1.0)
#         iz = x * random.uniform(-1.0,1.0)

#         #calculate the distance of the vector
#         vecX = ix - x
#         vecY = iy - y
#         vecZ = iz - z

#         vector = [0.0,0.0,0.0]
#         vector[0] = vecX
#         vector[1] = vecY
#         vector[2] = vecZ

#         return vector

#     #calculate gradient
#     def gradient(self, gx0,gx1,gy0,gy1, inputx, inputy):
#         gx = (gx0 - gx1) * inputx
#         gy = (gy0 - gy1) * inputx

#         g = [gx,gy]

#         return g

#     #interpolation values that changes the way the values will be outputted based on cosin and a random input
#     def lerp(self,a,b):
#             #create random input value
#             w = random.uniform(0.0,1.0)

#             #creates a value related to radians so it can be applied to the cosin value
#             ft = w * 3.1415927

#             f = (1.0 - math.cos(ft)) * 0.5

#             val = a*(1-f) + b*f

#             return val
