# command = input("> ")
car_state = "stop"
started = False
command = ""
print("Welcome to the car game! If you need help, type 'help'")

# while car_state != "quit":
while True:
  command = input("> ").lower()
  if command == "help":
    # print("start - to start the car \nstop - to stop the car \nquit - to exit \n\n")
    print("""
start - to start the car
stop - to stop the car
quit - to exit
    
    """)
  # elif command == "start" and car_state != "start":
  #   car_state = "start"
  #   print("Starting the car, here we go!")
  elif command == "start":
    if started:
      print("Hey, the car has already started! Enter a different command (or type 'help' for more help)")
    else: 
      started = True
      print("Starting the car, here we go!")
  # elif command == "start" and car_state == "start":
  #   print("Hey, the car has already started! Enter a different command (or type 'help' for more help)")
  elif command == "stop":
    if not started:
      print("We're already stopped! Enter a different command (or type 'help' for more help)")
    else:
      started = False
      print("Stopping the car, please keep all hands and feet inside the vehicle")
  # elif command == "stop" and car_state == "stop":
  #   print("We're already stopped! Enter a different command (or type 'help' for more help)")
  elif command == "quit":
    print("Goodbye!")
    break
  else:
    print("I don't recognize that command... type 'help' for instructions")
# else: 
#   print("Goodbye!")