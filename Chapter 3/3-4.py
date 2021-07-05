c = 1100 # Speed of sound in ft/sec
m2ft = 5280 # Mile to feet. 1 mile is 5280 ft.

time = float(input("Elapsed time between the flash and the sound of thunder (sec): "))

print("Distance to the lightning (miles): ", c*time/m2ft)