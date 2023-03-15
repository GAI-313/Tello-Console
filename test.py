from modules.tello import console

drone = console(language="jp", recv=False)

while True:
    print(drone.get_imu(),
            drone.get_tof(),
            drone.get_height(),
            drone.get_battery(),
            drone.get_flighttime(),
            drone.get_speed())
