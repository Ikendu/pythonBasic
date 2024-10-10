start = False
stop = False
help = False

while True:
    operate = (input("Select operations: (start, stop, speed, quit, help) ")).lower()
    if operate == "quit":
        print("Car is stopping... Operations stopped")
        print("Thank you for using our service")
        break
    elif operate == "start" and start == False:
        start = True
        stop = False
        print("Car is starting...")
    elif operate == "start" and start == True:
            print("Car has already started")
    elif operate == "stop" and stop == False:
        stop = True
        start = False
        print("Car is stopping...")
    elif operate == "stop" and stop == True:
        print("Car has already been stopped")
    elif operate == "speed" and start == True:
        print("Car is increasing spped")
    elif operate == "speed" and start == False:
        print("You can speed with starting the car")
    elif operate == "help":
        print("""
        To start the Car: Press "start"
        To stop the Car:  Press "stop"
        To speed up:      Press "speed"
        Press "quit" to stop operations
        """)
    else:
        print("Wrong Key Selected, Press 'quit' to stop Operations")


