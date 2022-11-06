#add
def add(a,b):
    return a + b

#sub
def sub(a,b):
    return a - b

#mull
def mul(a,b):
    return a * b

#div
def div(a,b):
    return a / b

operators={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def calculator():

    num1=float(input("enter the first number :"))
    for oper in operators:
        print(oper)
    calciluation = True

    while calciluation==True:
        operation_symbol=input("Pick an operation :")
        num2=float(input("enter the second number :"))
        calculation_function = operators[operation_symbol]
        answer = calculation_function(num1,num2)
        answer = round(answer,2)

        print(f"{num1} {operation_symbol} {num2} = {answer} ")


        comand=input("Type 'y' to continue and 'n' to start a new calculator :" )
        if comand=="y":
            num1 = answer
        else:
            calciluation = False
            calculator()

calculator()
