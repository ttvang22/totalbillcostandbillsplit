print "Hello, this system is to help split bills among roommate"

#Define roommate
roommatename1 = raw_input("What is the first roommate name? ")
roommatename2 = raw_input("What is the second roommate name? ")
roommatename3 = raw_input("What is the third roommate name? ")
roommatename4 = raw_input("What is the fourth roommate name? ")

#Define Who is paying
everybody = (roommatename1 , roommatename2 , roommatename3 , roommatename4)
print everybody, "is all the people who are splitting the monthly bill"

#Define All Bills and Cost
mortgage_or_houserent = int(raw_input("Please enter monthly mortgage or house rent bills"))
electricitybill = int(raw_input("Please enter eletricity bills "))
waterbill = int(raw_input("Please enter water bills "))
phonebill = int(raw_input("Please enter phone bills "))
cablebill = int(raw_input("Please enter cable bills "))

print "So your mortgage or rent is", mortgage_or_houserent, "eletricity bill is", electricitybill, "water bill is", waterbill, " phone bill is", phonebill, " and cable bill is", cablebill

total_bill =sum([mortgage_or_houserent, electricitybill, waterbill, phonebill, cablebill])
print "Your total bill will be", total_bill, 'dollars'

#Split Bill
split_bill= total_bill/4

print "Everybody should pay", split_bill, "dollars per roommate this month for bills"

#End
print "I hope I can help ease eveyone monthly bill payment with this program"
