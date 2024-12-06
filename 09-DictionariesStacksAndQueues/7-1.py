prod = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
total_sum = sum(prod.values())
for n,b in prod.items():
    print(f"{n}:{b}")
print(total_sum)    
