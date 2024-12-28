
superhero = ["batman","superman","wonder woman","iornman","blackpanther"]
print(superhero)

hero = input("append superhero: ")

superhero.append(hero)
print(superhero)

hero = input("remove superhero: ")

if hero in superhero:
    superhero.remove(hero)
    print("superhero is in the listd!")
else: 
    print("YOU DON MESS UP SON, NOW YOU HAVE A ONE WAY TICKET TO THE PRINCIEAL'S OFFICE!!")
print(superhero)