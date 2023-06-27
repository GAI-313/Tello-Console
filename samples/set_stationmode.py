from modules.tello import console

drone = console()

ssid=""
password=""

drone.set_ap(ssid, password)
