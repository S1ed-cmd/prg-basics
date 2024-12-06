#Create a dictionary as in the example below. Do you know what type of value was used in each of the six key-value pairs?

person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
#Displays name
#Displays hobby
#Displays the entire contents of the dictionary
#Changes surname to 'Nowak'
#Changes person's marriage status
#Adds gender: 'male'
#Adds a new hobby: 'bicycle'
#Adds work phone to existing phones: '313131444'
#Displays the entire contents of the dictionary (iterate over dictionary items)
print(person["name"])
print(person['hobby'])
for i,n in person.items():
    if isinstance(n, dict):
        for o,p in n.items():
            print(o,":",p)
    elif isinstance(n, list):
        for item in n:
            print(i,":",item)
    else:
        print(f"{i} : {n}")
person["surname"] ="Nowak"
person["married"] = False
person["gender"] ="Male"
person["hobby"] = ["swimming","excursions","bicycle"]
person["phone"] = {"landline":"123444321","mobile":"777888999","work":"31313144"}
for i,n in person.items():
    if isinstance(n, dict):
        for o,p in n.items():
            print(o,":",p)
    elif isinstance(n, list):
        for item in n:
            print(i,":",item)
    else:
        print(f"{i} : {n}")

