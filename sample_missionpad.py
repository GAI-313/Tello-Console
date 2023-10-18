from modules.tello import console
import traceback

drone = console()

drone.missionpad_detection(1)
#drone.missionpad_detection_setting(2)

try:
    drone.takeoff()
    #drone.up(50)
    drone.missionpad_go(0,0,50,20,3)
    #drone.missionpad_jump(0,100,0,20,0,4,3)

    #drone.land()
except:
    traceback.print_exc()
    drone.land()
