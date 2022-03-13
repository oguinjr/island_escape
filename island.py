def island_escape():
	island = []
	main_land = ['fox','chicken', 'grain']
	boat = []
	def all_dead():
		print("You left all the animals to eat each other up.")
		print("You die of starvation.")
		print("........")
		print("Hit enter to start over.")
		input()
		island_escape()

	def dead_chicken():
		if 'fox' and 'chicken' in main_land:
			print("You left the fox to eat the chicken.")
			print("I hope you enjoy eating your grain!")
			print("Hit enter to start over.")
			input()
			island_escape()
		elif 'fox' and 'chicken' in island:
			print("You left the fox to eat the chicken.")
			print("I hope you enjoy eating your grain!")
			print("Hit enter to start over.")
			input()
			island_escape()

	def no_grain():
		if 'chicken' and 'grain' in main_land:
			print("You left the chicken to eat all the grain.")
			print("Good luck growing crops!")
			print("Hit enter to start over.")
			input()
			island_escape()
		elif 'chicken' and 'grain' in island:
			print("You left the chicken to eat all the grain.")
			print("Good luck growing crops!")
			print("Hit enter to start over.")
			input()
			island_escape()

	def set_sail():
		print("Hit enter to set sail.")
		input()
		dead_chicken()
		no_grain()
	print("""You need to escape from the mainland to a nearby island with your\n
	fox, chicken, and a bag of seed. You have a boat, but it can only hold you and one\n
	other item or animal. Make it to the island to survive.\n
	One quick caveat however, the fox can never be left alone with the chicken, and the\n
	chicken can never be left alone with the seed.\n
	GOOD LUCK!
	""")

	while island != ['fox', 'chicken', 'grain']:
		if not boat:
			print("You are at the mainland")
			print("Press Enter to continue.")
			input()
			print("Do you want to take an animal or item with you across the river? Please type y or n")
			choice = input('>')
			if choice == 'y':
				for x in main_land:
					print(x)
				print("Of the animals or items listed type the name which you would like to set sail with.")
				choice = input('>')
				main_land.remove(choice)
				boat.append(choice)
				print(f"The boat has {boat} and the mainland has {main_land}.")
				set_sail()


			elif choice == 'n':
				print(f"The boat is empty and the mainland is left with {main_land}.")
				if 'fox' and 'chicken' and 'grain' in main_land:
					all_dead()
				else:
					set_sail()

		else:
			print(f"Do you want to:")
			print(f"a. Drop off the {boat} and leave alone?")
			print("or")
			if len(main_land) == 2:
				swap_first = main_land[0]
				swap_second = main_land[1]
				boat_first = boat[0]
				print(f"b. swap the {boat_first} for the {swap_first}")
				print(f"c. swap the {boat_first} for the {swap_second}")
				choice = input('>')
			elif len(main_land) == 1:
				swap_first = main_land[0]
				boat_first = boat[0]
				print(f"b. swap the {boat_first} for the {swap_first}")
				choice = input('>')

			if choice == 'a':
				boat_first = boat[0]
				main_land.append(boat_first)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the mainland has {main_land}.")
				set_sail()

			elif choice == 'b':
				main_first = main_land[0]
				boat_first = boat[0]
				boat.append(main_first)
				main_land.remove(main_first)
				main_land.append(boat_first)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the mainland has {main_land}.")
				set_sail()
			elif choice == 'c':
				main_second = main_land[1]
				boat_first = boat[0]
				boat.append(main_second)
				main_land.remove(main_second)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the mainland has {main_land}.")
				set_sail()

		if not boat:
			print("You are at the island.")
			Print("Press Enter to continue.")
			input()
			print("Do you want to take an animal or item with you across the river? Please type y or n")
			choice = input('>')
			if choice == 'y':
				if not island:
					print("There is nothing here to take")
				else:
					for x in island:
						print(x)
					print("Of the animals or items listed type the name which you would like to set sail with.")
					choice = input('>')
					island.remove(choice)
					boat.append(choice)
					print(f"The boat has {boat} and the island has {island}.")
					set_sail()

			elif choice == 'n':
				print(f"The boat is empty and the island is left with {island}.")
				if 'fox' and 'chicken' and 'grain' in island:
					all_dead()
				else:
					set_sail()

		else:
			print("You are at the island.")
			Print("Press Enter to continue.")
			input()
			print(f"Do you want to:")
			print(f"a. Drop off the {boat} and leave alone?")
			print("or")
			if len(island) == 2:
				swap_first = island[0]
				swap_second = island[1]
				boat_first = boat[0]
				print(f"b. swap the {boat_first} for the {swap_first}")
				print(f"c. swap the {boat_first} for the {swap_second}")
				choice = input('>')
			elif len(island) == 1:
				swap_first = island[0]
				boat_first = boat[0]
				print(f"b. swap the {boat_first} for the {swap_first}")
				choice = input('>')

			if choice == 'a':
				boat_first = boat[0]
				island.append(boat_first)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the island has {island}.")
				set_sail()
			elif choice == 'b':
				island_first = island[0]
				boat_first = boat[0]
				boat.append(island_first)
				island.remove(island_first)
				island.append(boat_first)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the island has {island}.")
				set_sail()
			elif choice == 'c':
				island_second = island[1]
				boat_first = boat[0]
				boat.append(island_second)
				island.remove(island_second)
				boat.remove(boat_first)
				print(f"The boat now has {boat} and the mainland has {island}.")
				set_sail()

	else:
		print(f"Congradulations, you've crossed the river with {island[0]}, {island[1]}, and {island[2]}.")
		input()
		quit()

island_escape()
