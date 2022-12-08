from modules.tello import console, procon_control

drone = console()
procon = procon_control()

while True:
    res = procon.read()
    print(res)
