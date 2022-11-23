print("WELCOME TO TREASURE ISLAND")

print("Your missin is to find the treasure")

direction = input("Which direction are you going ? RIGHT or LEFT")

direction_convert = direction.lower()

if direction_convert == "right" :
      print("Wow! congratulation to next level")
   
else:
    print(" Fall into a hole GAME OVER")

swin = input("Do you swim or wait for boat ? SWIM or WAIT")

swim_convert = swin.lower()

if swim_convert == "wait":
 print("Wow! Smart dude")

else :
 print("Attack by corcodile GAME OVER")

choose_color = input("Choose Treasure color : BLUE , RED or YELLOW")

choose_color_covert = choose_color.lower()

if choose_color_covert == "red":
 print("You WON")

elif choose_color_covert == "yellow":
 print("You are eaten by beast You LOSS")
elif choose_color_covert == "blue":
 print("You are burn by fire You LOSS")

else:
 print("You chose a door that doesn't exist. Game Over.")



