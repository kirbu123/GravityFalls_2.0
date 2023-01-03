import vpython as vp
vp.scene.title = "Modeling the motion of planets with the gravitational force"
vp.scene.height = 600
vp.scene.width = 800

planet1 = vp.sphere(pos=vp.vector(1, 0, 0), radius=0.05, color=vp.color.green, mass=100, momentum=vp.vector(0, 30, 0), make_trail=True)

planet2 = vp.sphere(pos=vp.vector(0, 3, 0), radius=0.075, color=vp.vector(0.0, 0.82, 0.33), mass=200, momentum=vp.vector(-35, 0, 0), make_trail=True)

planet3 = vp.sphere(pos=vp.vector(0, -4, 0), radius=0.1, color=vp.vector(0.58, 0.153, 0.68), mass=1000, momentum=vp.vector(40, 50, 0), make_trail=True)




def gravitationalForce(p1, p2):
	G = 1 #real-world value is : G = 6.67e-11
	rVector = p1.pos - p2.pos
	rMagnitude = vp.mag(rVector)
	rHat = rVector / rMagnitude
	F = - rHat * G * p1.mass * p2.mass / rMagnitude**2
	return F


t = 0
dt = 0.0001 #The step size. This should be a small number

while (True):
    vp.rate(500)
    # Calculte the force using gravitationalForce function
    planet1.force = gravitationalForce(planet1, planet2) + gravitationalForce(planet1, planet3)
    planet2.force = gravitationalForce(planet2, planet1) + gravitationalForce(planet2, planet3)
    planet3.force = gravitationalForce(planet3, planet1) + gravitationalForce(planet3, planet2)

    # Update momentum, position and time
    planet1.momentum = planet1.momentum + planet1.force * dt
    planet2.momentum = planet2.momentum + planet2.force * dt
    planet3.momentum = planet3.momentum + planet3.force * dt

    planet1.pos = planet1.pos + (planet1.momentum / planet1.mass) * dt
    planet2.pos = planet2.pos + (planet2.momentum / planet2.mass) * dt
    planet3.pos = planet3.pos + (planet3.momentum / planet3.mass) * dt

    t += dt