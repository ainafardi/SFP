import random 

print("What is your name?")
name= input()

adjectives = ["sly","brave","daring","persuasive","clever","crazy"]
animals = ["fox","frog","cat","wolf","snake","deer"]

codename= random.choice(adjectives) + " " + random.choice(animals)
print(f"{name}, your codename is: {codename}")

num= (random.randint(1,99))
print(f"Your lucky number is: {num}")