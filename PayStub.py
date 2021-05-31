#Paystub
#arya peer
#March 5 2020
#To create a pay stub for an employee of Richmond Television

#declare constants
MONTHLY_PAY=1750
COMMISION_RATE=0.145
INCOME_TAX=0.278

#title
print("------------------------------------------------------")
print("Monthly Paystub For Richmond Hill Television Employees")
print("------------------------------------------------------")

#Request and get info
name=(input("What is your name "))
socialInsuranceNumber=(input("Input your 9 digit Social Insurance Number"))
salesThisMonth=float(input("Total Value of All sales this month"))

#Calculations
commision=(COMMISION_RATE)*(salesThisMonth)
commision=round(commision, ndigits=2)
grossPay=(1750+commision)
grossPay=round(grossPay,ndigits=2)
incomeTaxToBePaid=(grossPay*(INCOME_TAX))
incomeTaxToBePaid=round(incomeTaxToBePaid,ndigits=2)
netPay=(grossPay-incomeTaxToBePaid)
netPay=round(netPay,ndigits=2)
totalNetPay=(12*netPay)
totalNetPay=round(totalNetPay,ndigits=2)


#output
print("\n")
print("---------------------------------------------------------------------------------------")
print("\tMonthly Payslip For: ",name, "Employee of Richmond Television")
print("---------------------------------------------------------------------------------------")
print("Your Social Insurance Number: ",socialInsuranceNumber)

print("{:50s}{:1s}{:12.2f}".format("Sales This Month:","$",salesThisMonth))
print("{:50s}{:1s}{:12.2f}".format("The Base Pay in Your Current Position Is:", "$", MONTHLY_PAY))
print("{:50s}{:1s}{:12.2f}".format("Commission From Sales This Month:", "$", commision))
print("{:50s}{:1s}{:12.2f}".format("Your Gross Pay:", "$", grossPay))
print("{:50s}{:1s}{:12.2f}".format("Income Tax Will Come To:", "$", incomeTaxToBePaid))
print("{:50s}{:1s}{:12.2f}".format("Your Net Pay:", "$", netPay))
print("{:50s}{:1s}{:12.2f}".format("Your Total Net Pay:", "$", totalNetPay))
