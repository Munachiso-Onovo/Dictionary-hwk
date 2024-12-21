animals = {"lion":3,"bear":4,"snake":7,"leopard":6,}

animal = input("What animal do want to see?")

print(animal)

if animal in animals:
    print("Here is the animal and its details")
    animal_details = animals[animal]
    print(animal_details)
