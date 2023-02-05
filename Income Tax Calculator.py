#Daniel Tiagi
# Assignment 2
# Income tax calculator


#prompt user for their income
income = float(input('what is your income? '))
#prompt for number of dependants
dependants = float(input("How many dependants do you have? "))
#Calculate Income after deductions
postDeductions = (income - (10000 + (3000*dependants)))
#calculate and return income tax
tax = postDeductions*0.2
print("Income tax: " , tax)