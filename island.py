def all_dead():
	if 'fox' in main_land:
		if 'chicken' in main_land:
			if 'grain' in main_land:
				print("You left all the animals to eat each other up.")
				print("You die of starvation.")
				print("........")
				print("Hit enter to quit.")
				input()
				exit(0)

def dead_chicken_main():
	if 'fox' in main_land:
		if 'chicken' in main_land:
				print("You left the fox to eat the chicken.")
				print("I hope you enjoy eating your grain!")
				print("Hit enter to quit.")
				input()
				exit(0)

def dead_chicken_island():
	if 'fox' in island:
		if 'chicken' in island:
			print("You left the fox to eat the chicken.")
			print("I hope you enjoy eating your grain!")
			print("Hit enter to quit.")
			input()
			exit(0)

def no_grain_main():
	if 'chicken' in main_land:
		if 'grain' in main_land:
			print("You left the chicken to eat the grain.")
			print("I hope you enjoy growing no crops!")
			print("Hit enter to quit.")
			input()
			exit(0)

def no_grain_island():
	if 'chicken' in island:
		if 'grain' in island:
			print("You left the chicken to eat the grain.")
			print("I hope you enjoy growing no crops!")
			print("Hit enter to quit.")
			input()
			exit(0)

def set_sail():
	dead_chicken_main()
	dead_chicken_island()
	no_grain_main()
	no_grain_island()
	print("Hit enter to set sail.")
	input()

island = []
main_land = ['fox','grain','chicken']
boat = []
line_break = print("------------------------------------------------------------------")
def island_escape():
	print("""You need to escape from the mainland to a nearby island with your\n
	--------------------------------------------------------------------------\n
	fox, chicken, and a bag of seed. You have a boat, but it can only hold you\n
	--------------------------------------------------------------------------\n
	and one other item or animal. Make it to the island to survive.\n
	--------------------------------------------------------------------------\n
	One quick caveat however, the fox can never be left alone with the chicken,\n
	--------------------------------------------------------------------------\n
	and the chicken can never be left alone with the seed.\n
	GOOD LUCK!
	""")

	while island != ['fox', 'chicken', 'grain']:
		if not boat:
			print("You are at the mainland")
			print("Press Enter to continue.")
			input()
			print("Do you want to take an animal or item with you across the river? Please type y or n")
			print("-----------------------------------------------------------")
			choice = input('>')
			if choice == 'y':
				print("-------------------------------------------------------")
				for x in main_land:
					print(x)
				print("-----------------------------------------------------------")
				print("Of the animals or items listed type the name which you would like to set sail with.")
				choice = input('>')
				main_land.remove(choice)
				boat.append(choice)
				print("-----------------------------------------------------------")
				print(f"The boat has {boat} and the mainland has {main_land}.")
				print("-----------------------------------------------------------")
				set_sail()
				print("-----------------------------------------------------------")




			elif choice == 'n':
				print(f"The boat is empty and the mainland is left with {main_land}.")
				if 'fox' and 'chicken' and 'grain' in main_land:
					all_dead()
				else:
					set_sail()
			else:
				print("Maybe you typed something wrong?")
				break

		else:
			print(f"Do you want to:")
			print("-----------------------------------------------------------")
			if len(main_land) == 2:
				swap_first = main_land[0]
				swap_second = main_land[1]
				boat_first = boat[0]
				print(f"a. Drop off the {boat} and leave alone?")
				print(f"b. swap the {boat_first} for the {swap_first}")
				print(f"c. swap the {boat_first} for the {swap_second}")
				print("-----------------------------------------------------------")
				choice = input('>')
				print("-----------------------------------------------------------")
			elif len(main_land) == 1:
				swap_first = main_land[0]
				boat_first = boat[0]
				print(f"a. Drop off the {boat} and leave alone?")
				print(f"b. swap the {boat_first} for the {swap_first}")
				print("-----------------------------------------------------------")
				choice = input('>')
				print("-----------------------------------------------------------")
			else:
				print(f"a. Drop off the {boat} and leave alone?")
				print("-----------------------------------------------------------")
				choice = input('>')
				print("-----------------------------------------------------------")

			if choice == 'a':
				boat_first = boat[0]
				main_land.append(boat_first)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the mainland has {main_land}.")
				set_sail()
				print("-----------------------------------------------------------")

			elif choice == 'b':
				main_first = main_land[0]
				boat_first = boat[0]
				boat.append(main_first)
				main_land.remove(main_first)
				main_land.append(boat_first)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the mainland has {main_land}.")
				print("-----------------------------------------------------------")
				set_sail()
			elif choice == 'c':
				main_second = main_land[1]
				boat_first = boat[0]
				boat.append(main_second)
				main_land.remove(main_second)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the mainland has {main_land}.")
				print("-----------------------------------------------------------")
				set_sail()

		if not boat:
			print("You are at the island.")
			print("Press Enter to continue.")
			input()
			if not island:
				print("What are you doing? You shouldnt have made it here")
				print("-----------------------------------------------------------")
			else:
				print("Do you want to take an animal or item with you across the river? Please type y or n")
				print("-----------------------------------------------------------")
			choice = input('>')
			if choice == 'y':
				print("-----------------------------------------------------------")
				for x in island:
					print(x)
					print("-----------------------------------------------------------")
					print("Of the animals or items listed type the name which you would like to set sail with.")
				choice = input('>')
				island.remove(choice)
				boat.append(choice)
				print("-----------------------------------------------------------")
				print(f"The boat has {boat} and the island has {island}.")
				print("-----------------------------------------------------------")
				set_sail()

			elif choice == 'n':
				print("-----------------------------------------------------------")
				print(f"Just messing around I see.")
				print("-----------------------------------------------------------")
				set_sail()

		else:
			print("You are at the island.")
			print("Press Enter to continue.")
			input()
			print("-----------------------------------------------------------")
			print(f"Do you want to:")
			print("-----------------------------------------------------------")
			if len(island) == 2:
				swap_first = island[0]
				swap_second = island[1]
				boat_first = boat[0]
				print(f"a. Drop off the {boat} and leave alone?")
				print(f"b. swap the {boat_first} for the {swap_first}")
				print(f"c. swap the {boat_first} for the {swap_second}")
				print(f"z. Keep the {boat} and head back to mainland")
				print("-----------------------------------------------------------")
				choice = input('>')
				print("-----------------------------------------------------------")
			elif len(island) == 1:
				swap_first = island[0]
				boat_first = boat[0]
				print(f"a. Drop off the {boat} and leave alone?")
				print(f"b. swap the {boat_first} for the {swap_first}")
				print(f"z. Keep the {boat_first} and head back to mainland")
				print("-----------------------------------------------------------")
				choice = input('>')
				print("-----------------------------------------------------------")
			else:
				print(f"a. Drop off the {boat} and leave alone?")
				print(f"z. Keep the {boat} and head back to mainland")
				print("-----------------------------------------------------------")
				choice = input('>')
				print("-----------------------------------------------------------")

			if choice == 'a':
				boat_first = boat[0]
				island.append(boat_first)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the island has {island}.")
				if 'grain' in island:
					if 'fox' in island:
						if 'chicken' in island:
							print("-----------------------------------------------------------")
							print('you won!')
							print("-----------------------------------------------------------")

							exit(0)
				else:
					set_sail()
			elif choice == 'b':
				island_first = island[0]
				boat_first = boat[0]
				boat.append(island_first)
				island.remove(island_first)
				island.append(boat_first)
				boat.remove(boat_first)
				print("-----------------------------------------------------------")
				print(f"The boat now has {boat} and the island has {island}.")
				print("-----------------------------------------------------------")

				set_sail()
			elif choice == 'c':
				island_second = island[1]
				boat_first = boat[0]
				boat.append(island_second)
				island.remove(island_second)
				boat.remove(boat_first)
				print("-----------------------------------------------------------")
				print(f"The boat now has {boat} and the mainland has {island}.")
				print("-----------------------------------------------------------")

				set_sail()
			else:
				print("Alright then, back to the mainland")

	else:
		print(f"Congradulations, you've crossed the river with {island[0]}, {island[1]}, and {island[2]}.")
		input()
		quit()

island_escape()
