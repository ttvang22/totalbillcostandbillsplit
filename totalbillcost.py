#Define Name and Income (+)
name = raw_input("Hello, What is your name?")
print "Nice, Thank You", name

#Beginning
print "Lets begin, please try to be as accurate as you can."

#Adding information on personal bills
my_income = input("Please add just your monthly income here ")
print "This is your total monthly income", my_income, "dollars"

other_income = input("Please add other income, if you have any such as child support, second jobs, wife or husband income, etc")
print 'This is your other income', other_income, "dollars"

total_income = my_income + other_income
print name, "your total monthly income will be, ", total_income, "dollars"

#This is based on Savings
print "From the wise word of Warren Buffet, Don't save what is left after Spending, But spend what is left after saving"

print "Lets begin by saving money first before spending what is left, assuming you are will to save or not"

savings_to_bank= total_income * .20
print "Transfer", savings_to_bank, "to the savings account, your welcome"

leftover_income= total_income - total_income * .20
print "This is what is left after savings", leftover_income, "dollar."

#Total Cost of Bill/Liability (-)
print name, "now, lets begin with your monthly bills, please be as accurate as you can"

mortgage_or_houserent = int(raw_input("Pleas enter your monthly houserent bills"))
print "This is your mortgage or house rent", mortgage_or_houserent, "dollars"

auto_loan_carpayment = int(raw_input("Please enter your carpayment bills"))
print "This is your car payment", auto_loan_carpayment, "dollars"

personal_creditcard = int(raw_input("Please enter your creditcard bills "))
print "This is your personal credit card", personal_creditcard, "dollars"

personal_carinsurance = int(raw_input("Please enter your carinsurance bills "))
print "This is your auto car insurance ", personal_carinsurance, "dollars"

studentloan = int(raw_input("Please enter your studentloan bills"))
print "This is your student loan", studentloan, "dollars"

electricitybill = int(raw_input("Please enter your eletricity bills"))
print "This is your eletricity bill", electricitybill, "dollars"

waterbill = int(raw_input("Please enter your water bills"))
print "This is your water bill" , waterbill, "dollars"

phonebill = int(raw_input("Please enter your phone bills"))
print "This is your phone bill", phonebill, "dollars"

cablebill = int(raw_input("Please enter your cable bills"))
print "This is your cable bill", cablebill, "dollars"

gasbill = int(raw_input("How much for gas"))
print "This is your gas bill", gasbill, "dollars"

grocery = int(raw_input ("How much for food"))
print "This is your grocery", grocery, "dollars"

#The Bill Math
total_bill = sum([mortgage_or_houserent, auto_loan_carpayment, personal_creditcard, personal_carinsurance, studentloan, electricitybill, waterbill, phonebill, cablebill])
print name, "Your total bill will be ", total_bill, "dollars"

fun_money = leftover_income - total_bill
print name, "Your fun money will be at", fun_money, "dollars"

print "Thank You", name, "I hope you enjoy this"
