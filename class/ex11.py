#EX 11

#Get inputs
print("How old are you?", end='\t')
age = input()
print("How tall are you?", end= '\t')
height = input()
print("How much do you weigh?", end='\t')
weight = input()

#display results
print(f"\nSo, you're {age} old, {height} tall, and weigh {weight}.")

print("\n\nNow let's solve some 4th grade math problems:\n")
#Get inputs
print("How many watermelons did Bertha buy?",end='\t')
watermelons = int(input())
print("How much did each watermelon cost?", end='\t$')
price = float(input())
#calculate total amount spent
spent = watermelons * price
#display inputs, price displayed to two decimal points
print(f"\nBetha bought {watermelons} watermelons for $%.2f each." % (price))
#display amount spent to two decimal points
print("Bertha spent $%.2f" % (spent))
