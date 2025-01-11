def f(num1,num2,oper):
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "%":
        return num1 % num2
    elif oper == "**":
        return num1 ** num2
    


print(f(2,3,"+"))
print(f(2,3, "%")) 
print(f(2,3, "**")) 
print(f(2,3, "*")) 
print(f(2,3, "-") )