from modules.tello import console

drone = console(langage="us")

drone.takeoff()
drone.forward(100)
drone.land()