grossIncome=float(input("Enter your gross income: $"))
numberOfDependents=int(input("No of dependents:"))
standardDeduction=10000
dependentDeduction=3000
taxableIncome = grossIncome - standardDeduction - (dependentDeduction * numberOfDependents)
taxableIncome = max(0,taxableIncome)
print("Your taxable income is $",taxableIncome)
taxRate=20
tax=(taxableIncome*taxRate)/100
print("Your tax is $",tax)