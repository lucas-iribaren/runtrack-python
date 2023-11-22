def calcule(num1, operator,num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2

print(calcule(1,"+",1))
print(calcule(5,"-",2))
print(calcule(12,"*",4))
print(calcule(7,"/",3))
print(calcule(10,"%",5))
