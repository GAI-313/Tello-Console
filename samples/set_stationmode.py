from tello import console

drone = console()

ssid="nwi19116g1"
password="nwi19116"

drone.set_ap(ssid, password)
