#Daniel Tiagi
# Assignment 2
# Income tax calculator



#prompt user for their income
income = float(input('Enter the gross income: '))
#prompt for number of dependants
dependants = float(input("Enter the number of dependents: "))
#Calculate Income after deductions
postDeductions = (income - (10000 + (3000*dependants)))
#calculate and return income tax
tax = postDeductions*0.2
print("Income tax: " , tax)
