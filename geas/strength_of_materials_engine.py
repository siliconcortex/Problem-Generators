from generator import random_handler as ran
from generator import constants_conversions as c
import sympy
import math
import random


x, y, z = sympy.symbols('x y z', real = True)#generic variables


#init_printing(use_unicode=False)
gravity = c.acceleration(9.81, 'mpers2')

#----------Source: Singer and Pytel------------#
class singer_104:
    def __init__(self,*args,**kwargs): 
        diameterInside = c.length(ran.main(100),'mm')
        load = c.force(ran.main(400),'kN')
        stressLimit = c.stress(ran.main(120),'MNperm2')
        self.question = f"""A hollow steel tube with an inside diameter of {diameterInside.mm} mm must carry a tensile load of {load.kN} kN. Determine the outside diameter of the tube if the stress is limited to {stressLimit.MNperm2} MN/m2."""
        equation = sympy.Eq(load.N, stressLimit.Pa * (math.pi/4) * (x**2 - diameterInside.m**2))
        temp = sympy.solveset(equation,x,domain = sympy.Reals)
        temp2 = max(temp.args[0],temp.args[1])
        diameterOutside = c.length(temp2,'m')
        self.answer = f"""{round(diameterOutside.mm,2)} mm"""
        
class singer_105:
    def __init__(self,*args,**kwargs): 
        mass = c.mass(ran.main(800),'kg')
        lengthBar = c.length(ran.main(10),'m')
        lengthBronzeCable = c.length(ran.main(4),'m')
        lengthSteelCable = c.length(ran.main(3),'m')
        stressBronze = c.stress(ran.main(90),'MPa')
        stressSteel = c.stress(ran.main(120),'MPa')
        self.question = f"""A homogeneous {mass.kg} kg bar AB is supported at either
end by a bronze and a steel cable. Calculate the smallest area of each cable if the stress is not to exceed {stressBronze.MPa} MPa in bronze and {stressSteel.MPa} MPa in steel.(Figure P-105)"""
        loadCable = c.force(mass.kg * gravity.mpers2 / 2, 'N')
        areaBronze = c.area(loadCable.N / stressBronze.Pa)
        areaSteel = c.area(loadCable.N / stressSteel.Pa)
        self.answer = f"""{round(areaBronze.mm2,2)} mm2, {round(areaSteel.mm2,2)} mm2"""

class singer_106:
    def __init__(self,*args,**kwargs): 
        diameter = c.length(ran.main(0.6),'inch')
        weight = c.force(ran.main(6000),'lb')
        self.question = f"""The homogeneous bar (shown in Fig. P-106) is
supported by a smooth pin at C and a cable that runs from A to B around the smooth peg at D. Find the stress in the cable if its diameter is {diameter.inch} inch and the bar weighs {weight.lb} lb."""
        equation = sympy.Eq(5*x + 10*(3/math.sqrt(34))*x, 5*weight.N)      
        temp = sympy.solveset(equation,x,domain = sympy.Reals)
        tension = c.force(temp.args[0])
        area = c.area(math.pi * diameter.m**2 / 4)
        stress = c.stress(tension.N / area.m2)
        self.answer = f"""{round(stress.psi,2)} psi"""
        
class singer_107:
    def __init__(self,*args,**kwargs): 
        load = c.force(ran.main(3000),'lb')
        area = c.area(ran.main(0.5),'in2') 
        self.question = f"""A rod is composed of an aluminum section rigidly attached between steel and bronze sections, as shown. Axial loads are applied at the positions indicated. If P = {load.lb} lb and the cross sectional area of the rod is {area.in2} in2, determine the stress in each section. https://lesliecaminadecom.files.wordpress.com/2019/06/43x8vc20i6hr46g5xi86.png"""
        stressSteel = c.stress( 4*load.N / area.m2 )
        stressAluminum = c.stress( 4*load.N / area.m2 )
        stressBronze = c.stress( 3*load.N / area.m2 )
        self.answer = f"""{round(stressSteel.ksi,2)} ksi, {round(stressAluminum.ksi,2)} ksi, {round(stressBronze.ksi,2)} ksi"""

class singer_108:
    def __init__(self,*args,**kwargs): 
        steelLimit = c.stress(ran.main(140),'MPa')
        aluminumLimit = c.stress(ran.main(90),'MPa')
        bronzeLimit = c.stress(ran.main(100),'MPa')
        areaBronze = c.area(200, 'mm2')
        areaAluminum = c.area(400, 'mm2')
        areaSteel = c.area(500, 'mm2')
        self.question = f"""An aluminum rod is rigidly attached between a steel rod and a bronze rod as shown in Fig. P-108. Axial loads are applied at the positions indicated. Find the maximum value of P that will not exceed a stress in steel of 140 MPa, in aluminum of 90 MPa, or in bronze of 100 MPa. https://lesliecaminadecom.files.wordpress.com/2019/06/fp87ftc247319psycxw9.png"""
        pBronze = c.force(bronzeLimit.Pa * areaBronze.m2 / 2, 'N')
        pAluminum = c.force( aluminumLimit.Pa * areaAluminum.m2, 'N')
        pSteel = c.force(steelLimit.Pa * areaSteel.m2 / 5, 'N')
        pMin = c.force(min(pBronze.N, pAluminum.N, pSteel.N), 'N')
        self.answer = f"""{round(pMin.kN,2)} kN"""
        
class singer_109:
    def __init__(self,*args,**kwargs): 
        areaAB = c.area(ran.main(0.4), 'in2')
        areaAC = c.area(ran.main(0.5), 'in2')
        stressLimit = c.stress(ran.main(30), 'ksi')
        angleAB = c.angle(30, 'deg')
        angleAC = c.angle(50, 'deg')
        self.question = f"""Determine the largest weight W that can be supported by two wires shown in Fig. P- 109. The stress in either wire is not to exceed {stressLimit.ksi} ksi. The cross-sectional areas of wires AB and AC are {areaAB.in2} in2 and {areaAC.in2} in2, respectively. https://lesliecaminadecom.files.wordpress.com/2019/06/5xdql28a14u9h4frb4c6.png"""
        maxTensionAB = c.force( stressLimit.Pa * areaAB.m2 )
        maxTensionAC = c.force( stressLimit.Pa * areaAC.m2 )
        weightAB = c.force(
        maxTensionAB.N*math.sin(angleAB.rad) +
        maxTensionAB.N*math.cos(angleAB.rad)*math.tan(angleAC.rad)
        )
        weightAC = c.force(
        maxTensionAC.N*math.cos(angleAC.rad)*math.tan(angleAB.rad) + 
        maxTensionAC.N*math.sin(angleAC.rad)
        )
        safeWeight = c.force(min(weightAC.N , weightAB.N))
        self.answer = f"""{round(safeWeight.kips,2)} kips"""
        
class singer_110:
    def __init__(self,*args,**kwargs): 
        woodStressLimit = c.stress(ran.main(1800), 'psi')
        concreteStressLimit = c.stress(ran.main(650), 'psi')
        woodDiameter = c.length(8, 'in')
        concreteSide = c.length(12, 'in')
        
        self.question = f"""A 12-inches square steel bearing plate lies between an 8-inches diameter wooden post and a concrete footing as shown in Fig. P-110. Determine the maximum value of the load P if the stress in wood is limited to {woodStressLimit.psi} psi and that in concrete to {concreteStressLimit.psi} psi.https://lesliecaminadecom.files.wordpress.com/2019/06/fc2mf3m0yzgi9qpxftu0.png"""
        
        forceWood = c.force( woodStressLimit.Pa * math.pi * woodDiameter.m**2 / 4)
        forceConcrete = c.force( concreteStressLimit.Pa * concreteSide.m**2 )
        
        safeForce = c.force(min(forceWood.N, forceConcrete.N))
        
        self.answer = f"""{round(safeForce.lb,2)} lb"""
        
class singer_115:
    def __init__(self,*args,**kwargs): 
        diameter = c.length(ran.main(20),'mm')
        thickness = c.length(ran.main(25), 'mm')
        G = c.stress(ran.main(350), 'MNperm2')
        
        self.question = f"""What force is required to punch a {diameter.mm}-mm-diameter hole in a plate that is {thickness.mm} mm thick? The shear strength is {G.MNperm2} MN/m2.https://lesliecaminadecom.files.wordpress.com/2019/06/33hg81bobbgb161ve5yd.png"""
        
        force = c.force( G.Pa * math.pi * diameter.m * thickness.m )
        
        self.answer = f"""{round(force.kN,2)} kN"""
        
class singer_116:
    def __init__(self,*args,**kwargs): 
        
        plateStress = c.stress(ran.main(40), 'ksi')
        punchStress = c.stress(ran.main(50), 'ksi')
        # scenario 1
        diameter = c.length(ran.main(2.5), 'in')
        # scenario 2
        thickness = c.length(ran.main(0.25), 'in')

        self.question = f"""As in Fig. 1-11c, a hole is to be punched out of a plate having a shearing strength of {plateStress.ksi} ksi. The compressive stress in the punch is limited to {punchStress.ksi} ksi. (a) Compute the maximum thickness of plate in which a hole {diameter.inch} inches in diameter can be punched. (b) If the plate is {thickness.inch} inch thick, determine the diameter of the smallest hole that can be punched."""
        
        puncherForce = c.force(punchStress.Pa * math.pi * diameter.m**2 / 4)
        thicknessAsk = c.length(puncherForce.N / (plateStress.Pa * math.pi * diameter.m ))
        
        diameterAsk = c.length( 4*plateStress.Pa*thickness.m / (punchStress.Pa)  )
        
        self.answer = f"""{round(thicknessAsk.inch,2)} in, {round(diameterAsk.inch,2)} in"""

class singer_117:
    def __init__(self,*args,**kwargs): 
        load = c.force(ran.main(400), 'kN')
        shearStress = c.stress(ran.main(300), 'MPa')
        
        self.question = f"""Find the smallest diameter bolt that can be used in the clevis shown in Fig. 1-11b if P = {load.kN} kN. The shearing strength of the bolt is {shearStress.MPa} MPa.https://lesliecaminadecom.files.wordpress.com/2019/06/726wetc0kd0dg9hzr334.png"""
        
        diameter = c.length(math.sqrt((4*load.N)/(math.pi * shearStress.Pa)))
        
        self.answer = f"""{round(diameter.mm,2)} mm"""
        
class singer_125:
    def __init__(self,*args,**kwargs): 
        
        diameter = c.length(ran.main(20), 'mm')
        width = c.length(ran.main(110), 'mm')
        plateStress = c.stress(ran.main(120), 'MPa')
        rivetStress = c.stress(ran.main(60), 'MPa')
        
        
        self.question = f"""In Fig. 1-12, assume that a {diameter.mm}-mm-diameter rivet joins the plates that are each {width.mm} mm wide. The allowable stresses are {plateStress.MPa} MPa for bearing in the plate material and {rivetStress.MPa} MPa for shearing of rivet. Determine (a) the minimum thickness of each plate; and (b) the largest average tensile stress in the plates. https://lesliecaminadecom.files.wordpress.com/2019/06/0s8a1drcveflo7p7zq9u.png"""
        
        thickness = c.length(
        (rivetStress.Pa * math.pi * diameter.m) / (4*plateStress.Pa)
        )
        
        stressPlateMax = c.stress(
        (rivetStress.Pa * math.pi * diameter.m**2) / (4*thickness.m*(width.m - diameter.m))
        )
        
        self.answer = f"""{round(thickness.mm,2)} mm, {round(stressPlateMax.MPa,2)} MPa"""

class singer_126:
    def __init__(self,*args,**kwargs): 
        diameter = c.length(0.75,'inch')
        rivetStress = c.stress(ran.main(14), 'ksi')
        plateStress = c.stress(ran.main(18), 'ksi')
        plateWidth = c.length(4,'inch')
        plateThickness = c.length(7/8, 'inch')
        
        self.question = f"""The lap joint shown in Fig. P-126 is fastened by four ¾-in.-diameter rivets. Calculate the maximum safe load P that can be applied if the shearing stress in the rivets is limited to {rivetStress.ksi} ksi and the bearing stress in the plates is limited to {plateStress.ksi} ksi. Assume the applied load is uniformly distributed among the four rivets.https://lesliecaminadecom.files.wordpress.com/2019/06/xepe9ah52y755kbuiy9r.png"""
        
        forceA = c.force(
        rivetStress.Pa * 4 * math.pi * diameter.m**2 / 4
        )
        
        forceB = c.force( plateStress.Pa * 4 * diameter.m * plateThickness.m )
        
        safeLoad = c.force( min (forceA.N, forceB.N)  )
        
        self.answer = f"""{round(safeLoad.kips,2)} kips"""
        
class singer_127:
    def __init__(self,*args,**kwargs): 
        load = c.force(ran.main(14), 'kips')
        shear = c.stress(ran.main(12), 'ksi')
        bearing = c.stress(ran.main(20), 'ksi')
        
        self.question = f"""In the clevis shown in Fig. 1-11b, find the minimum bolt diameter and the minimum thickness of each yoke that will support a load P = {load.kips} kips without exceeding a shearing stress of {shear.ksi} ksi and a bearing stress of {bearing.ksi} ksi.https://lesliecaminadecom.files.wordpress.com/2019/06/irl22zt567obtp1690vl.png"""
        
        diameter = c.length( math.sqrt((2*load.N) / (math.pi * shear.Pa)))
        
        thickness = c.length( (load.N) / (2 * bearing.Pa * diameter.m ))
        
        self.answer = f"""{round(diameter.inch,2)} in, {round(thickness.inch,2)} in"""

class singer_133:
    def __init__(self,*args,**kwargs): 
        diameter = c.length(ran.main(400), 'mm')
        thickness = c.length(ran.main(20), 'mm')
        pressure = c.pressure(ran.main(4.5), 'MNperm2')
        stress = c.stress(ran.main(120), 'MNperm2')
        
        self.question = f"""A cylindrical steel pressure vessel 400 mm in diameter with a wall thickness of 20 mm, is subjected to an internal pressure of 4.5 MN/m2. (a) Calculate the tangential and longitudinal stresses in the steel. (b) To what value may the internal pressure be increased if the stress in the steel is limited to 120 MN/m2?"""
        
        tangential = c.stress( (pressure.Pa * diameter.m) / (2 * thickness.m) )
        
        longitudinal = c.stress( (pressure.Pa * diameter.m ) / (4 * thickness.m) )

        critical = c.stress(min(tangential.Pa, longitudinal.Pa))
        
        pressure = c.pressure((2 * stress.Pa * thickness.m) / (diameter.m))
        
        self.answer = f"""{round(tangential.MPa,2)} MPa, {round(longitudinal.MPa,2)} MPa, {round(pressure.MPa,2)} Mpa"""

class singer_134:
    def __init__(self,*args,**kwargs): 
        diameter = c.length(ran.main(4), 'ft')
        thickness = c.length(ran.main(5/16), 'inch')
        stress = c.stress(ran.main(8000), 'psi')
        
        self.question = f"""The wall thickness of a {diameter.ft}-ft-diameter spherical tank is {thickness.inch} in. Calculate the allowable internal pressure if the stress is limited to {stress.psi} psi."""

        pressure = c.pressure( 4 * stress.Pa * thickness.m / diameter.m )
        
        self.answer = f"""{round(pressure.psi,2)} psi"""
        
class singer_135:
    def __init__(self,*args,**kwargs): 
        pressure = c.pressure(ran.main(1400), 'psi')
        diameter = c.length(ran.main(2), 'ft')
        stress = c.stress(ran.main(12), 'ksi')
        
        
        self.question = f"""Calculate the minimum wall thickness for a cylindrical vessel that is to carry a gas at a pressure of {pressure.ksi} psi. The diameter of the vessel is {diameter.ft} ft, and the stress is limited to {stress.ksi} ksi."""
        
        thickness = c.length( (pressure.Pa * diameter.m ) / (2*stress.Pa))
        
        self.answer = f"""{round(thickness.inch,2)} in"""
        
        
class singer_136:
    def __init__(self,*args,**kwargs): 
        thickness = c.length(ran.main(20), 'mm')
        diameter = c.length(ran.main(450), 'mm')
        length = c.length(ran.main(2), 'm')
        longitudinalStress = c.stress(ran.main(140), 'MPa')
        circumferentialStress = c.stress(ran.main(60), 'MPa')
        
        self.question = f"""A cylindrical pressure vessel is fabricated from steel plating that has a thickness of {thickness.mm} mm. The diameter of the pressure vessel is {diameter.mm} mm and its length is {length.m} m. Determine the maximum internal pressure that can be applied if the longitudinal stress is limited to {longitudinalStress.MPa} MPa, and the circumferential stress is limited to {circumferentialStress.MPa} MPa."""
        
        pressure1 = c.pressure(2 * thickness.m * circumferentialStress.Pa / diameter.m )
        
        pressure2 = c.pressure(4 * thickness.m * longitudinalStress.Pa / diameter.m)
        
        safePressure = c.pressure(min(pressure1.Pa, pressure2.Pa))
        
        self.answer = f"""{round(safePressure.MPa,2)} MPa"""
        
# class singer_137:
    # def __init__(self,*args,**kwargs): 
        
class singer_138:
    def __init__(self,*args,**kwargs): 
        tangentialStress = c.forcePerLength(ran.main(33), 'kipsperft')
        longitudinalStress = c.forcePerLength(ran.main(16), 'kipsperft')
        pressure = c.pressure(ran.main(150), 'psi')
        
        
        self.question = f"""The strength of longitudinal joint in Fig. 1-17 is {tangentialStress.kipsperft} kips/ft, whereas for the girth is {longitudinalStress.kipsperft} kips/ft. Calculate the maximum diameter of the cylinder tank if the internal pressure is {pressure.psi} psi."""
        
        diameter1 = c.length(2*tangentialStress.Nperm / pressure.Pa)
        diameter2 = c.length(4*longitudinalStress.Nperm/ pressure.Pa)
        
        diameterSafe = c.length(min(diameter1.m, diameter2.m))
        
        self.answer = f"""{round(diameterSafe.inch,2)} in"""
        
class singer_141:
    def __init__(self,*args,**kwargs): 
        pressure = c.pressure(ran.main(125), 'psi')
        thickness = c.length(ran.main(1/8), 'inch')
        length = c.length(1.5, 'ft')
        width = c.length(2, 'ft')
        
        
        self.question = f"""The tank shown in Fig. P-141 is fabricated from {thickness.inch}-in steel plate. Calculate the maximum longitudinal and circumferential stress caused by an internal pressure of {pressure.psi} psi.https://lesliecaminadecom.files.wordpress.com/2019/06/v0k26t4bf5m8cknyumkv.png"""
        
        area = c.area( length.m * width.m + (math.pi * length.m**2 / 4) )
        force = c.force(pressure.Pa * area.m2)
        
        longStress = c.stress(force.N / (math.pi * length.m * thickness.m + 2 * width.m * thickness.m))
        
        area2 = c.area( width.m * length.m * 1)
        force2 = c.force( pressure.Pa * area.m2)
        
        circumStress = c.stress( force2.N / (2*thickness.m))
        
        self.answer = f"""{round(longStress.ksi,2)} ksi, {round(circumStress.ksi,2)} ksi"""

class singer_142:
    def __init__(self,*args,**kwargs): 
        pressure = c.pressure(ran.main(3.5), 'MPa')
        diameterOut = c.length(450,'mm')
        thicknessWall = c.length(10,'mm')
        diameterBolt = c.length(ran.main(40), 'mm')
        stressAllowable = c.stress(ran.main(80), 'MPa')
        stressInitial = c.stress(stressAllowable.MPa - ran.main(25), 'MPa')
        
        self.question = f"""A pipe carrying steam at {pressure.MPa} MPa has an outside diameter of 450 mm and a wall thickness of 10 mm. A gasket is inserted between the flange at one end of the pipe and a flat plate used to cap the end. How many {diameterOut.mm}-mm-diameter bolts must be used to hold the cap on if the allowable stress in the bolts is {stressAllowable.MPa} MPa, of which {stressInitial.MPa} MPa is the initial stress? What circumferential stress is developed in the pipe?https://lesliecaminadecom.files.wordpress.com/2019/06/btr10hx2z229k3q9ldfw.png"""
        
        capArea = c.area(math.pi * (diameterOut.m - 2*thicknessWall.m)**2 / 4 )
        force = c.force(pressure.Pa * capArea.m2)
        
        boltArea = c.area(math.pi * diameterBolt.m**2 / 4)
        
        numberBolts = math.ceil(force.N / (boltArea.m2 * (stressAllowable.Pa - stressInitial.Pa)))
        
        circumArea = c.area(1 * (diameterOut.m - 2*thicknessWall.m))
        force2 = c.force(circumArea.m2 * pressure.Pa)
        circumStress = c.stress( force.N / (2*thicknessWall.m))
        
        self.answer = f"""{round(numberBolts,2)} bolts, {round(circumStress.MPa,2)} MPa"""

class singer_206:
    def __init__(self,*args,**kwargs): 
        density = c.density(7850,'kgperm3')
        area = c.area(ran.main(300), 'mm2')
        length = c.length(ran.main(150), 'm')
        load = c.force(ran.main(20), 'kN')
        E = c.stress(200, 'GPa')
        
        self.question = f"""A steel rod having a cross-sectional area of {area.mm2} mm2 and a length of {length.m} m is suspended vertically from one end. It supports a tensile load of {load.kN} kN at the lower end. If the unit mass of steel is {density.kgperm3} kg/m3 and E = {E.MPa} MN/m2, find the total elongation of the rod."""
        
        deformation1 = c.length((load.N * length.m)/(area.m2 * E.Pa))
        deformation2 = c.length((density.kgperm3 * gravity.mpers2 * length.m**2)/(2*E.Pa))
        deformation = c.length(deformation1.m + deformation2.m)
  
        self.answer = f"""{round(deformation.mm,2)} mm"""
        
class singer_207:
    def __init__(self,*args,**kwargs): 
        length = c.length(ran.main(30), 'ft')
        load = c.force(ran.main(500), 'lb')
        stress = c.stress(ran.main(20), 'ksi')
        elongation = c.length(ran.main(0.20), 'in')
        E = c.stress(29e6,'psi')
        
        self.question = f"""A steel wire {length.ft} ft long, hanging vertically, supports a load of {load.lb} lb. Neglecting the weight of the wire, determine the required diameter if the stress is not to exceed {stress.ksi} ksi and the total elongation is not to exceed {elongation.inch} in. Assume E = {E.psi} psi."""
        
        diameter1 = c.length(math.sqrt((4*load.N)/(math.pi*stress.Pa)))
        diameter2 = c.length(math.sqrt((4*load.N*length.m)/(math.pi*elongation.m*E.Pa)))
        
        diameter = c.length(max(diameter1.m, diameter2.m))
        
        self.answer =f"""{round(diameter.inch,2)} in"""
        
class singer_208:
    def __init__(self,*args,**kwargs): 
        
        thickness = c.length(10,'mm')
        width = c.length(80, 'mm')
        tireInsideDiameter = c.length(1500, 'mm')
        wheelOutsideDiameter = c.length(1500 + ran.main(0.5), 'mm')
        mu = ran.main(0.3)
        E = c.stress(200,'GPa')
        
        self.question = f"""A steel tire, {thickness.mm} mm thick, {width.mm} mm wide, and {tireInsideDiameter.mm} mm inside diameter, is heated and shrunk onto a steel wheel {wheelOutsideDiameter.mm} mm in diameter. If the coefficient of static friction is {mu}, what torque is required to twist the tire relative to the wheel? Neglect the deformation of the wheel. Use E = {E.GPa} GPa. https://lesliecaminadecom.files.wordpress.com/2019/06/m483sfqwubz8a41a6n6g.png"""
        area = c.area(width.m * thickness.m)
        deformation = c.length(wheelOutsideDiameter.m - tireInsideDiameter.m)
        tension = c.force(deformation.m * area.m2 * E.Pa / tireInsideDiameter.m)
        
        pressure = c.pressure((2*tension.N)/(width.m*tireInsideDiameter.m))
        
        normal = c.force(pressure.Pa * math.pi * wheelOutsideDiameter.m * width.m)
        
        friction = c.force(mu * normal.N)
        
        torque = c.torque(friction.N * 0.5 * wheelOutsideDiameter.m)
        
        self.answer = f"""{round(torque.kNm,2)} kNm"""
        
class singer_209:
    def __init__(self,*args,**kwargs): 
        area = c.area(ran.main(0.5), 'in2')
        E = c.stress(ran.main(10e6), 'psi')
        
        force1 = c.force(6000, 'lb')
        force2 = c.force(1000, 'lb')
        force3 = c.force(4000, 'lb')
        length1 = c.length(3, 'ft')
        length2 = c.length(5, 'ft')
        length3 = c.length(4, 'ft')
        
        
        self.question = f"""An aluminum bar having a cross-sectional area of {area.in2} in2 carries the axial loads applied at the positions shown in Fig. P-209. Compute the total change in length of the bar if E = {E.psi} psi. Assume the bar is suitably braced to prevent lateral buckling. https://lesliecaminadecom.files.wordpress.com/2019/06/njduqdp2nyhbz2gx28f6.png"""
        
        deformation1 = c.length((force1.N * length1.m)/(area.m2 * E.Pa))
        deformation2 = c.length((force2.N * length2.m)/(area.m2 * E.Pa))
        deformation3 = c.length((force3.N * length3.m)/(area.m2 * E.Pa))
        deformation = c.length(deformation1.m - deformation2.m + deformation3.m)
        
        self.answer = f"""{round(deformation.inch,2)} in"""
        
class singer_211:
    def __init__(self,*args,**kwargs): 
        
        length1 = c.length(1, 'm')
        length2 = c.length(2, 'm')
        length3 = c.length(1.5, 'm')
        
        area1 = c.area(480, 'mm2')
        area2 = c.area(650, 'mm2')
        area3 = c.area(320, 'mm2')
        
        Est = c.stress(200, 'GPa')
        Eal = c.stress(70, 'GPa')
        Ebr = c.stress(83, 'GPa')
        
        stressSteel = c.stress(ran.main(140), 'MPa')
        stressBronze = c.stress(ran.main(120), 'MPa')
        stressAluminum = c.stress(ran.main(80), 'MPa')
        deformation = c.length(ran.main(3.0), 'mm')

        self.question = f"""A bronze bar is fastened between a steel bar and an aluminum bar as shown in Fig. P- 211. Axial loads are applied at the positions indicated. Find the largest value of P that will not exceed an overall deformation of {deformation.mm} mm, or the following stresses: {stressSteel.MPa} MPa in the steel, {stressBronze.MPa} MPa in the bronze, and {stressAluminum.MPa} MPa in the aluminum. Assume that the assembly is suitably braced to prevent buckling. Use Est = {Est.GPa} GPa, Eal = {Eal.GPa} GPa, and Ebr = {Ebr.GPa} GPa. https://lesliecaminadecom.files.wordpress.com/2019/06/eq9xj1csj51g0cpqa8xb.png"""
        
        force1 = c.force(stressSteel.Pa * area1.m2)
        force2 = c.force(stressBronze.Pa * area2.m2 / 2)
        force3 = c.force(stressAluminum.Pa * area3.m2 /2)

        force4 = c.force( deformation.m /( (length1.m/(area1.m2*Est.Pa)) - (length2.m/(area2.m2*Ebr.Pa)) + (length3.m/(area3.m2*Eal.Pa) )) )
        
        force = c.force(min(force1.N, force2.N, force3.N, force4.N))
        
        self.answer = f"""{round(force.kN,2)} kN"""
        
class singer_223:
    def __init__(self,*args,**kwargs): 
        
        xlength = c.length(ran.main(3), 'in')
        ylength = c.length(ran.main(2), 'in')
        zlength = c.length(ran.main(4), 'in')
        
        xforce = c.force(ran.main(48), 'kips')
        yforce = c.force(ran.main(60), 'kips')
        zforce = c.force(ran.main(54), 'kips')
        
        v = 0.3
        E = c.stress(29e6, 'psi')
        
        self.question = f"""A rectangular steel block is {xlength.inch} inches long in the x direction, {ylength.inch} inches long in the y direction, and {zlength.inch} inches long in the z direction. The block is subjected to a triaxial loading of three uniformly distributed forces as follows: {xforce.kips} kips tension in the x direction, {yforce.kips} kips compression in the y direction, and {zforce.kips} kips tension in the z direction. If ν = {v} and E = {E.psi} psi, determine the single uniformly distributed load in the x direction that would produce the same deformation in the y direction as the original loading."""
        
        xstress = c.stress(xforce.N / (ylength.m * zlength.m))
        ystress = c.stress(yforce.N / (xlength.m * zlength.m))
        zstress = c.stress(zforce.N / (ylength.m * xlength.m))
        
        ystrain = (1/E.Pa)*(ystress.Pa - v*(xstress.Pa + zstress.Pa))
        
        xstress2 = c.stress(-v*ystrain*E.Pa)
        
        xforce2 = c.force(xstress.Pa * ylength.m * zlength.m)
        
        self.answer = f"""{round(xforce2.kips,2)} kips (tension)"""
        
class singer_225:
    def __init__(self,*args,**kwargs): 
        thickness = c.length(ran.main(10), 'mm')
        diameter = c.length(ran.main(1.20), 'm')
        pressure = c.pressure(ran.main(1.5), 'MPa')
        v = 0.30
        E = c.stress(200, 'GPa')
        
        self.question = f"""A welded steel cylindrical drum made of a {thickness.mm}-mm plate has an internal diameter of {diameter.m} m. Compute the change in diameter that would be caused by an internal pressure of {pressure.MPa} MPa. Assume that Poisson's ratio is {v} and E = {E.GPa} GPa."""
        
        ystress = c.stress((pressure.Pa * diameter.m)/(4 * thickness.m))
        xstress = c.stress((pressure.Pa * diameter.m)/(2 * thickness.m))
        xstrain = (xstress.Pa/E.Pa) - (v * ystress.Pa/E.Pa)
        deltaDiameter = c.length(xstrain*diameter.m)
            
        self.answer = f"""{round(deltaDiameter.mm,2)} mm"""
        
class singer_226:
    def __init__(self,*args,**kwargs): 
        diameter = c.length(ran.main(2), 'in')
        thickness = c.length(ran.main(0.05), 'in')
        load = c.force(ran.main(3140), 'lb')
        v = 0.30
        
        self.question = f"""A {diameter.inch}-in.-diameter steel tube with a wall thickness of {thickness.inch} inch just fits in a rigid hole. Find the tangential stress if an axial compressive load of {load.lb} lb is applied. Assume ν = {v} and neglect the possibility of buckling."""
        
        ystress = c.stress(load.N / (math.pi * diameter.m * thickness.m))
        xstress = c.stress(v * ystress.Pa)
        
        self.answer = f"""{round(xstress.psi,2)} psi"""
        
class singer_227:
    def __init__(self,*args,**kwargs): 
        
        length = c.length(ran.main(150), 'mm')
        diameter = c.length(ran.main(80), 'mm')
        thickness = c.length(ran.main(3), 'mm')
        pressure = c.pressure(ran.main(4.00), 'MPa')
        v = 1/3
        E = c.stress(83, 'GPa')
        
        self.question = f"""A {length.mm}-mm-long bronze tube, closed at its ends, is {diameter.mm} mm in diameter and has a wall thickness of {thickness.mm} mm. It fits without clearance in an {diameter.mm}-mm hole in a rigid block. The tube is then subjected to an internal pressure of {pressure.MPa} MPa. Assuming ν = 1/3 and E = {E.GPa} GPa, determine the tangential stress in the tube."""
        
        ystress = c.stress((pressure.Pa * diameter.m)/(4 * thickness.m))
        xstress = c.stress(v * ystress.Pa)
        
        self.answer = f"""{round(xstress.MPa,2)} MPa"""
        
class singer_228:
    def __init__(self,*args,**kwargs): 
        
        length = c.length(ran.main(6), 'in')
        diameter = c.length(ran.main(3), 'in')
        thickness = c.length(ran.main(0.10), 'in')
        v = 1/3
        E = c.stress(12e6, 'psi')
        pressure = c.pressure(ran.main(6000), 'psi')
        
        self.question = f"""A {length.inch}-in.-long bronze tube, with closed ends, is {diameter.inch} in. in diameter with a wall thickness of {thickness.inch} in. With no internal pressure, the tube just fits between two rigid end walls. Calculate the longitudinal and tangential stresses for an internal pressure of {pressure.psi} psi. Assume ν = 1/3 and E = {E.psi} psi."""
        
        tstress = c.stress((pressure.Pa * diameter.m)/(2 * thickness.m))
        lstress = c.stress(v * tstress.Pa)
        
        self.answer = f"""{round(lstress.psi,2)} psi, {round(tstress.psi,2)} psi"""

class singer_233:
    def __init__(self,*args,**kwargs): 
        diameter = c.length(ran.main(50), 'mm')
        length = c.length(ran.main(2), 'm')
        thickness = c.length(ran.main(5), 'mm')
        deformation = c.length(ran.main(0.8), 'mm')
        Est = c.stress(200, 'GPa')
        Eiron = c.stress(100, 'GPa')
        
        
        self.question = f"""A steel bar {diameter.mm} mm in diameter and {length.m} m long is surrounded by a shell of a cast iron {thickness.mm} mm thick. Compute the load that will compress the combined bar a total of {deformation.mm} mm in the length of {length.m} m. For steel, E = {Est.GPa} GPa, and for cast iron, E = {Eiron.GPa} GPa."""
        
        ironForce = c.force( 
        deformation.m * (math.pi/4) * ((diameter.m + 2*thickness.m)**2 - diameter.m**2) * Eiron.Pa / length.m)

        steelForce = c.force(
        deformation.m * (math.pi/4) * diameter.m**2 * Est.Pa / length.m )
        
        force = c.force(ironForce.N + steelForce.N)
        
        self.answer = f"""{round(force.kN,2)} kN"""
        
class singer_234:
    def __init__(self,*args,**kwargs): 
        diameter = c.length(ran.main(200), 'mm')
        load = c.force(ran.main(300), 'kN')
        concretestress = c.stress(ran.main(6), 'MPa')
        steelstress = c.stress(ran.main(120), 'MPa')
        Eco = c.stress(14, 'GPa')
        Est = c.stress(200, 'GPa')
        self.question = f"""A reinforced concrete column {diameter.mm} mm in diameter is designed to carry an axial compressive load of {load.kN} kN. Determine the required area of the reinforcing steel if the allowable stresses are {concretestress.MPa} MPa and {steelstress.MPa} MPa for the concrete and steel, respectively. Use Eco = {Eco.GPa} GPa and Est = {Est.GPa} GPa."""
        stressconcrete_maxsteel = c.stress(steelstress.Pa * Eco.Pa / Est.Pa)
        
        if stressconcrete_maxsteel.Pa < concretestress.Pa:
            concreteOK = c.stress(stressconcrete_maxsteel.Pa)
            steelOK = c.stress(steelstress.Pa)
        else:
            stresssteel_maxconcrete = c.stress(concretestress.Pa * Est.Pa / Eco.Pa)
            concreteOK = c.stress(concretestress.Pa)
            steelOK = c.stress(stresssteel_maxconcrete.Pa)   
        steelarea = c.area(
        (load.N - concreteOK.Pa * (math.pi / 4) * diameter.m**2) / 
        (steelOK.Pa - concreteOK.Pa)
        )
        self.answer = f"""{round(steelarea.mm2,2)} mm^2"""

class singer_235():
    def __init__(self):
        timber_side_length = c.length(ran.main(8), 'inch')
        plate_width = c.length(timber_side_length.inch, 'inch')
        #plate_thickness = t
        #axial_load = c.force(ran.main(300), 'kips')
        thickness = c.length(ran.main(365)/1000, 'inch')
        max_timber_stress = c.stress(ran.main(1200), 'psi')
        max_steel_stress = c.stress(ran.main(20), 'ksi')
        E_timber = c.stress(1.5e6, 'psi')
        E_steel = c.stress(29e6, 'psi')

        #check what forces will timber and steel individually max out.
        #when stress_timber = 1200 psi
        stress_steel_at_max_timber_stress = c.stress(E_steel.Pa * max_timber_stress.Pa / E_timber.Pa, 'Pa')

        steel_okay = max_steel_stress.Pa < stress_steel_at_max_timber_stress.Pa

        stress_timber_at_max_steel_stress = c.stress( E_timber.Pa * max_steel_stress.Pa / E_steel.Pa, 'Pa')

        timber_okay = max_timber_stress.Pa < stress_timber_at_max_steel_stress.Pa

        print('steel okay', steel_okay)
        print('timber okay', timber_okay)


        if timber_okay:
            stress_steel = c.stress(max_steel_stress.Pa, 'Pa')
            stress_timber = c.stress((1.5/29) * stress_steel.Pa, 'Pa')

        if steel_okay:
            stress_timber = c.stress(max_timber_stress.Pa, 'Pa')
            stress_steel = c.stress((29/1.5) * stress_timber.Pa, 'Pa')

        area_timber = c.area(timber_side_length.inch**2, 'in^2')

        axial_load = c.force(stress_steel.Pa * 4 * plate_width.m * thickness.m + stress_timber.Pa * area_timber.m2, 'N')

        

        self.question = f"""A timber column {timber_side_length.inch:4.4} in x {timber_side_length.inch:4.4} in cross section, in reinforced on each side by a steel plate {plate_width.inch:4.4} in wide and 't' inches thick. Determine the thickness 't' so that the column will support an axial load of {axial_load.kips:4.4} kips without exceeding a maximum timber stress of {max_timber_stress.psi:4.4} psi or a maximum steel stress of {max_steel_stress.ksi:4.4} ksi. The moduli of elasticity are {E_timber.psi:4.4} psi for timber and {E_steel.psi:4.4} psi for steel."""
        self.answer  = f"""{thickness.inch:4.4} inches"""

class singer_236():
    def __init__(self):
        copper_area = c.area(ran.main(900), 'mm2')
        copper_E = c.stress(120, 'GPa')
        copper_allowable_stress = c.stress(ran.main(70), 'MPa')
        copper_length = c.length(ran.main(160), 'mm')
        steel_area = c.area(ran.main(1200), 'mm2')
        steel_E = c.stress(200, 'GPa')
        steel_allowable_stress = c.stress(140, 'MPa')
        steel_length = c.length(ran.main(240), 'mm')

        ratio_copper_steel = (steel_length.m / steel_E.Pa) / (copper_length.m / copper_E.Pa )
        #10 * copper_stress = 9 *  steel_stress
        copper_stress_at_steel_max_stress = c.stress( ratio_copper_steel * steel_allowable_stress.Pa)

        copper_okay = copper_stress_at_steel_max_stress.Pa < copper_allowable_stress.Pa

        steel_stress_at_copper_max_stress = c.stress( (1/ratio_copper_steel) * copper_allowable_stress.Pa)

        steel_okay = steel_stress_at_copper_max_stress.Pa < steel_allowable_stress.Pa

        print('copper okay', copper_okay)
        print('steel okay', steel_okay)

        if copper_okay:
            steel_stress = steel_allowable_stress
            copper_stress = copper_stress_at_steel_max_stress
        if steel_okay:
            copper_stress = copper_allowable_stress
            steel_stress = steel_stress_at_copper_max_stress

        force = c.force( 2 * copper_stress.Pa * copper_area.m2 + steel_stress.Pa * steel_area.m2 )
        mass = c.mass(force.N / gravity.mpers2)

        self.question = f"""A rigid horizontal block of mass M is supported by three symmetrically spaced rods, two copper rods at each end of length {copper_length.mm:4.4} mm and a single steel rod at the center of length {steel_length.mm:4} mm. Each copper rod has an area of {copper_area.mm2:4.4} mm^2; E = {copper_E.GPa:4.4} GPa; and the allowable stress is {copper_allowable_stress.MPa:4.4} MPa. The steel rod has an area of {steel_area.mm2:4.4} mm^2; E = {steel_E.GPa:4.4} GPa; and the allowable stress is {steel_allowable_stress.MPa:4.4} MPa. Determine the largest mass M which can be supported."""

        self.answer = f"""{mass.kg:4.4} kg"""

class singer_238():
    def __init__(self):
        weight_load = c.force(ran.main(40), 'kips')
        steel_length = c.length(ran.main(3), 'feet')
        steel_area = c.area(ran.main(1), 'in2')
        steel_E = c.stress(29e6, 'psi')
        bronze_area = c.area(ran.main(1.5), 'in2')
        bronze_E = c.stress(12e6, 'psi')

        #condition steel_load = 2 * bronze_load
        bronze_load = c.force(weight_load.N/5)
        steel_load = c.force(bronze_load.N * 2)

        #deformation is equal in both rods
        equation_1 = sympy.Eq(
            ((bronze_load.N * x) / (bronze_area.m2 * bronze_E.Pa)), 
            ((steel_load.N * steel_length.m) / (steel_area.m2 * steel_E.Pa)) 
            )
        bronze_length = c.length(sympy.solveset(equation_1, x).args[0])
        print('bronze length: REFERENCE: 3.72 ft, :', bronze_length.ft, 'ft')

        #second condition 
        #steel_stress = 2 * bronze_stress
        equation_2 = sympy.Eq(
            (4 * steel_area.m2  * x + bronze_area.m2 * x),
            weight_load.N
            ) 

        bronze_stress = c.stress(sympy.solveset(equation_2, x).args[0])
        print('bronze stress (REF: 7.27 ksi)', bronze_stress.ksi, 'ksi')
        steel_stress = c.stress( bronze_stress.Pa * 2)

        equation_3 = sympy.Eq(
            (bronze_stress.Pa * x / bronze_E.Pa) , 
            (steel_stress.Pa * steel_length.m / steel_E.Pa)
            )

        bronze_length_2 = c.length(sympy.solveset(equation_3, x).args[0])
        print('bronze length 2 (REF: 2.48 ft)', bronze_length.ft, 'ft')

        self.question = f"""A horizontal beam with weight {weight_load.kips:4.4} kips is hung by three rods one copper rod at the center and a steel rod on each end. The two steel rods on each end have a length of {steel_length.ft:4.4} ft , and an area of {steel_area.in2:4.4} in^2, and E = {steel_E.psi:4.4} psi. For the bronze bar, the area is {bronze_area.in2:4.4} in^2 and E = {bronze_E.psi:4.4} psi. Determine a) the length of the bronze bar so that the load on each steel bar is twice the load on the bronze bar, and b) the length of the bronze bar that will make the steel stress twice the bronze stress."""
        self.answer = f"""{bronze_length.ft:4.4} ft, {bronze_length_2.ft:4.4} ft"""

class singer_239():
    def __init__(self):
        try_again = True
        while try_again:
            aluminum_length = c.length(ran.main(249.90), 'mm')
            initial_difference = c.length(ran.main(0.1), 'mm')
            steel_length = c.length(aluminum_length.mm + initial_difference.mm, 'mm')
            load = c.force(ran.main(400), 'kN')
            steel_area = c.area(ran.main(1200), 'mm2')
            steel_E = c.stress(200, 'GPa')
            aluminum_area = c.area(ran.main(2400), 'mm2')
            aluminum_E = c.stress(70, 'GPa')

            #condition
            #steel_deformation = aluminum_deformation + initial_difference
            #Let x  = steel_stress, Let y = aluminum_stress
            equation_1 = sympy.Eq(
                (x * steel_length.m / steel_E.Pa),
                (y * aluminum_length.m / aluminum_E.Pa) + initial_difference.m
                )

            equation_2 = sympy.Eq(
                (2 * x * steel_area.m2 + y * aluminum_area.m2) ,
                load.N
                )

            equations = [equation_1, equation_2]

            aluminum_stress = c.stress(
                sympy.linsolve(equations, x, y).args[0][0]
                )

            steel_stress = c.stress(
                sympy.linsolve(equations, x, y).args[0][1]
                )
            print('linear equations', equations)
            print('solutions', sympy.linsolve(equations, x, y))
            if aluminum_stress.Pa > 0 and steel_stress.Pa > 0:
                try_again = False


        print('stress aluminum (REF: 22.48 MPa)', aluminum_stress.MPa, 'MPa')

        self.question = f"""A horizontal rigid platform has negligible mass and rests on two steel bars on each of its ends, each vertical bar has a length of {steel_length.mm:4.4} mm long. A vertical center bar is aluminum and is {aluminum_length.mm:4.4} mm and just barely touching the bar. Compute the stress in the aluminum bar after the center load P = {load.kN:4.4} kN has been applied. For each steel bar, the area is {steel_area.mm2:4.4} mm^2 and E = {steel_E.GPa:4.4} GPa. For the aluminum bar, the area is {aluminum_area.mm2:4.4} mm^2 and E = {aluminum_E.GPa:4.4} GPa."""
        self.answer = f"""{aluminum_stress.MPa:4.4} MPa"""

class singer_240():
    def __init__(self):
        eyebar_length = c.length(ran.main(4), 'inch')
        eyebar_width = c.length(ran.main(1), 'inch')
        pin_diameter = c.length(ran.main(7/8), 'inch')
        centerline_spacing = c.length(ran.main(30), 'ft')
        middle_bar_centerline_difference = c.length(ran.main(0.045), 'inch')
        steel_E = c.stress(29e6, 'psi')

        #conditions
        #middle_load = 2 * outer_load
        #outer_deformation + middle_deformation = difference
        #Let x = outer_load, 
        equation_1 = sympy.Eq(
            ((x * centerline_spacing.m)  / (eyebar_length.m * eyebar_width.m * steel_E.Pa)) + ((2 * x * (centerline_spacing.m - middle_bar_centerline_difference.m))/(eyebar_width.m * eyebar_length.m * steel_E.Pa)),
            middle_bar_centerline_difference.m
            )

        outer_load = c.force(sympy.solveset(equation_1).args[0])
        middle_load = c.force(outer_load.N * 2)
        pin_shearing_stress = c.stress(middle_load.N / (2 * (1/4) * math.pi * (pin_diameter.m)**2))

        print('shearing stress (REF: 8038.54 psi)', pin_shearing_stress.psi, 'psi')

        self.question = f"""Three steel eye bars, each {eyebar_length.inch:4.4} inch by {eyebar_width.inch:4.4} inch section, are to be assembled by driving rigid {pin_diameter.inch:4.4} inch diameter drift pins through holes drilled in the ends of the bars. The center-line spacing between the holes is {centerline_spacing.ft:4.4} ft in the two outer bars, but {middle_bar_centerline_difference.inch:4.4} inch shorter in the middle bar. Find the shearing stress developed in the drip pins. Neglect local deformation at the holes."""
        self.answer  =f"""{pin_shearing_stress.psi:4.4} psi"""

class singer_241():
    def __init__(self):
        try_again = True
        while try_again:
            wire_area = c.area(ran.main(0.05), 'in2')
            weight = c.force(ran.main(1500), 'lb')
            wire_1_length = c.length(ran.main(74.98), 'ft')
            wire_1_2_difference = c.length(ran.main(0.01), 'ft')
            wire_2_length = c.length(wire_1_length.ft + wire_1_2_difference.ft, 'ft')
            wire_2_3_difference = c.length(ran.main(0.01), 'ft')
            wire_3_length = c.length(wire_2_length.ft + wire_2_3_difference.ft, 'ft')

            #stress in longest wire
            #bring all shorter wires to the length of the longest wire
            steel_E = c.stress(29e6, 'psi')
            equation_1 = sympy.Eq(
                (wire_3_length.m - wire_1_length.m),
                (x * wire_1_length.m) / (wire_area.m2 * steel_E.Pa)
                )
            wire_1_force_at_wire_3_length = c.force(sympy.solveset(equation_1, x).args[0])
            equation_2 = sympy.Eq(
                (wire_3_length.m - wire_2_length.m),
                (x * wire_2_length.m) / (wire_area.m2 * steel_E.Pa)
                )
            wire_2_force_at_wire_3_length = c.force(sympy.solveset(equation_2, x).args[0])

            equation_4 = sympy.Eq(
                    (wire_2_length.m - wire_1_length.m),
                    (x * wire_1_length.m) / (wire_area.m2 * steel_E.Pa)
                    )
            wire_1_force_at_wire_2_length = c.force(sympy.solveset(equation_4, x).args[0])

            print('weight', weight.lb, 'lb')
            print('wire 1 force at wire 3 length', wire_1_force_at_wire_3_length.lb, 'lb')
            print('wire 2 force at wire 3 length', wire_2_force_at_wire_3_length.lb, 'lb')
            print('wire 1 force at wire 2 length', wire_1_force_at_wire_2_length.lb, 'lb')

            print('generating', type(self))
            if weight.N > (wire_1_force_at_wire_3_length.N + wire_2_force_at_wire_3_length.N):
                print(weight.lb, ' > ', wire_1_force_at_wire_3_length.lb, ' + ' ,wire_2_force_at_wire_3_length.N)
                equation_3 = sympy.Eq(
                    3*x + wire_1_force_at_wire_3_length.N + wire_2_force_at_wire_3_length.N, weight.N 
                    )
                wire_3_force = c.force(sympy.solveset(equation_3, x).args[0])
                wire_2_force = c.force(wire_3_force.N + wire_2_force_at_wire_3_length.N)
                wire_1_force = c.force(wire_3_force.N + wire_1_force_at_wire_3_length.N)
                try_again = False



            elif (wire_1_force_at_wire_2_length.N < weight.N < (wire_1_force_at_wire_3_length.N + wire_2_force_at_wire_3_length.N)):
                print(wire_1_force_at_wire_2_length.lb,' < ',weight.lb, ' < ', wire_1_force_at_wire_3_length.lb, ' + ' ,wire_2_force_at_wire_3_length.N)

                wire_3_force = c.force(0)

                equation_4 = sympy.Eq(
                    (wire_2_length.m - wire_1_length.m),
                    (x * wire_1_length.m) / (wire_area.m2 * steel_E.Pa)
                    )
                wire_1_force_at_wire_2_length = c.force(sympy.solveset(equation_4, x).args[0])

                equation_5 = sympy.Eq(
                    2 * x + wire_1_force_at_wire_2_length.N, 
                    weight.N
                    )
                wire_2_force = c.force(sympy.solveset(equation, x).args[0])
                wire_1_force = c.force(wire_2_force.N + wire_1_force_at_wire_2_length.N)
                try_again = False

            elif wire_1_force_at_wire_2_length.N > weight.N:
                print(wire_1_force_at_wire_2_length.lb,' > ',weight.lb)
                wire_1_force = c.force(weight.N)
                wire_2_force = c.force(0)
                wire_3_force = c.force(0)
                try_again = False
            else:
                try_again = True

        print('these next numbers should be equal', weight.N, wire_1_force.N + wire_2_force.N + wire_3_force.N)

        wire_3_stress = c.stress(wire_3_force.N / wire_area.m2)
        wire_2_stress = c.stress(wire_2_force.N / wire_area.m2)
        wire_1_stress = c.stress(wire_1_force.N / wire_area.m2)
        print('wire stresses (wire1, wire2, wire3): ', wire_1_stress.psi, wire_2_stress.psi, wire_3_stress.psi)

        self.question = f"""Three steel wires, each {wire_area.in2:4.4} in^2 in area, area used to lift a load W = {weight.lb:4.4} lb. Their unstressed lengths are {wire_1_length.ft:4.4} ft, {wire_2_length.ft:4.4} ft and {wire_3_length.ft:4.4} ft. What stress exists in each wire?"""
        self.answer = f"""{wire_1_stress.psi:4.4} psi, {wire_2_stress.psi:4.4} psi, {wire_3_stress.psi:4.4} psi"""


class singer_244():
    def __init__(self):
        cross_section_area = c.area(ran.main(500), 'mm2')
        load_1 = c.force(ran.main(25), 'kN')
        load_2 = c.force(ran.main(50), 'kN')
        section_AB_length = c.length(ran.main(0.60))
        section_BC_length = c.length(ran.main(1.2))
        section_CD_length = c.length(ran.main(0.9))
        total_length = c.length(section_AB_length.m + section_BC_length.m + section_CD_length.m)

        reaction_A_load_1 = c.force(load_1.N * (section_BC_length.m + section_CD_length.m) / total_length.m)
        reaction_A_load_2 = c.force(load_2.N * (section_CD_length.m/total_length.m))
        reaction_A = c.force(reaction_A_load_1.N + reaction_A_load_2.N)
        force_section_BC = c.force(reaction_A.N - load_1.N)

        stress_section_BC = c.stress( force_section_BC.N / cross_section_area.m2)

        self.question = f"""A homogeneous horizontal bar with cross sectional area of {cross_section_area.mm2:4.4} mm^2 is attached to rigid supports at each end. It is divided into three sections AB, BC, and CD from left to right. It carries the axial load P1 = {load_1.kN:4.4} kN to the right at point B and P2 = {load_2.kN:4.4} kN to the right at point C. Determine the stress in segment BC."""
        self.answer = f"""{stress_section_BC.MPa:4.4} MPa""" 

class singer_245():
    def __init__(self):
        aluminum_length = c.length(ran.main(15), 'inch')
        steel_length = c.length(ran.main(10), 'inch')
        aluminum_area = c.area(ran.main(1.25), 'in2')
        steel_area = c.area(ran.main(2.0), 'in2')
        aluminum_E = c.stress(10e6, 'psi')
        steel_E = c.stress(29e6, 'psi')
        load = c.force(ran.main(50), 'kips')

        #Let x = Reaction A (leftmost), y = Reaction B, rightmost
        equation_1 = sympy.Eq(
            ((x * aluminum_length.m) / (aluminum_area.m2 * aluminum_E.Pa)),
            ((y * steel_length.m)/(steel_area.m2 * steel_E.Pa))
            )

        equation_2 = sympy.Eq(
            x,
            load.N - y
            )
        equations = [equation_1, equation_2]
        reaction_A = c.force(sympy.linsolve(equations, x, y).args[0][0])
        reaction_B = c.force(sympy.linsolve(equations, x, y).args[0][1])

        steel_force = reaction_B
        aluminum_force = reaction_A
        steel_stress = c.stress(steel_force.N / steel_area.m2)
        aluminum_stress = c.stress(aluminum_force.N / aluminum_area.m2)

        self.question = f"""A horizontal composite bar is firmly attached to unyielding supports. It is composed of two sections; an aluminum section with a length of {aluminum_length.inch:4.4} in. with a cross sectional area of {aluminum_area.in2:4.4} in^2, and a steel section with a length of {steel_length.inch:4.4} in. and a cross sectional area of {steel_area.in2:4.4} in^2. A force of {load.kips:4.4} kips is applied between the aluminum and steel sections in the direction towards the steel section. Compute the stress in the aluminum and steel sections respectively. E_steel = {steel_E.psi:4.4} psi, E_aluminum = {aluminum_E.psi:4.4} psi"""
        self.answer  = f"""{aluminum_stress.psi:4.4} psi, {steel_stress.psi:4.4} psi"""

class singer_247():
    def __init__(self):
        #aluminum section
        aluminum_area = c.area(ran.main(900), 'mm2')
        aluminum_E = c.stress(70, 'GPa')
        aluminum_length = c.length(ran.main(500), 'mm')

        #steel section
        steel_area = c.area(ran.main(2000),'mm2')
        steel_E = c.stress(200, 'GPa')
        steel_length = c.length(ran.main(250), 'mm')

        #bronze section
        bronze_area = c.area(ran.main(1200), 'mm2')
        bronze_E = c.stress(83, 'GPa')
        bronze_length = c.length(ran.main(350), 'mm')

        #loads
        load_1 = c.force(ran.main(150), 'kN')
        load_2 = c.force(ran.main(90), 'kN')

        equation_1 = sympy.Eq(
            ((x * aluminum_length.m)/(aluminum_area.m2 * aluminum_E.Pa)),
            (((load_1.N - x) * steel_length.m)/(steel_area.m2 * steel_E.Pa)) + 
            (((load_1.N + load_2.N - x) * bronze_length.m)/(bronze_area.m2 * bronze_E.Pa))
            )

        reaction_A = c.force(sympy.solveset(equation_1, x).args[0])

        aluminum_force = c.force(reaction_A.N)
        steel_force = c.force(load_1.N - aluminum_force.N)
        bronze_force = c.force(load_1.N + load_2.N - aluminum_force.N)

        aluminum_stress = c.stress(aluminum_force.N / aluminum_area.m2)
        steel_stress = c.stress(steel_force.N / steel_area.m2)
        bronze_stress = c.stress(bronze_force.N / bronze_area.m2)

        print('REFERENCE: 86.22 MPa, 36.20 MPa, 135.33 MPa')
        print(aluminum_stress.MPa, steel_stress.MPa, bronze_stress.MPa)

        self.question = f"""A horizontal composite bar is composed of three sections attached end to end. The first section is an aluminum section of length {aluminum_length.mm:4.4} mm, area of {aluminum_area.mm2:4.4} mm^2 and E = {aluminum_E.GPa:4.4} GPa. The middle section is a steel section of length {steel_length.mm:4.4} mm, area of {steel_area.mm2:4.4} mm^2 and E = {steel_E.GPa:4.4} GPa. The third section is a bronze section with length {bronze_length.mm:4.4} mm, area of {bronze_area.mm2:4.4} mm^2 and E = {bronze_E.GPa:4.4} GPa. A {load_1.kN:4.4} kN force is applied between the aluminum and steel sections in the direction towards the aluminum section and another {load_2.kN:4.4} kN force is applied between the steel and bronze section in the direction towards the steel section. Calculate the stresses in the aluminum, steel, and bronze sections respectively."""
        self.answer = f"""{aluminum_stress.MPa:4.4} MPa, {steel_stress.MPa:4.4} MPa, and {bronze_stress.MPa:4.4} MPa"""


#problems 249 to 257 are really complicated

class singer_261():
    def __init__(self):
        rod_area = c.area(ran.main(0.25), 'in2')
        temperature_initial = c.temperature(ran.main(70), 'F')
        load_initial = c.force(ran.main(1200), 'lb')
        temperature_final = c.temperature(ran.main(0), 'F')
        alpha = 6.5e-6 #per degree Fahrenheit
        steel_E = c.stress(29e6, 'psi')

        stress_final = c.stress(
            (alpha * steel_E.psi * (abs(temperature_final.F - temperature_initial.F)) + (load_initial.lb / rod_area.in2)), 'psi')

        equation_1 = sympy.Eq(
            (alpha * (x - temperature_initial.F)),
            (load_initial.lb / (rod_area.in2 * steel_E.psi))
            )

        temperature_zero_stress = c.temperature(sympy.solveset(equation_1, x).args[0], 'F')

        self.question = f"""A steel rod of cross-sectional area {rod_area.in2:4.4} in^2 is stretched between two fixed points. The tensile load at {temperature_initial.F:4.4} degF is {load_initial.lb:4.4} lb. What will be the stress at 0 degF? At what temperature will the stress be zero? Assume alpha = {alpha:4.4} in / in degF , and E = {steel_E.psi} psi."""
        self.answer = f"""{stress_final.ksi:4.4} ksi, {temperature_zero_stress.F:4.4} degF"""

        
        
        
        
        
        
        
        
        
        
        