#1. Create a greeting for your program.
print("\nWelcome to the Band Name Generator.")

#2. Ask the user for the city that they grew up in.
city = input("\nWhat's the name of the city you grew up in?\n")

#3. Ask the user for the name of a pet.
pets_name = input("\nWhat's your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pets_name

#5. Make sure the input cursor shows on a new line:
print(f"\nYour band name could be '{band_name}'!\n\n")