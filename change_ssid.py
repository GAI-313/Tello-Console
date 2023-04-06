from modules.tello import console

drone = console()

drone.send_cmd('ap test 10')
