# Description: A program that creates insurance invoices and stores them to a data file.
# By: Will Oldford
# Date Created: 07-26-23

# Libraries:
import datetime

# Required Variables/Constants:
f = open('OSCIDef.dat','r')
POLICY_NUM = int(f.readline())
COST_BASIC_PREMIUM = float(f.readline())
ADD_CAR_RATE = float(f.readline())
COST_LIABILITY_COV = float(f.readline())
COST_GLASS_COV = float(f.readline())
COST_LOANER_COV = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())

f.close()

while True:
    # Inputs:
    fName = input("Enter Costumer's First Name: ").title()
    lName = input("Enter Costumer's Last Name: ").title()
    address = input("Enter Costumer's Home Adress: ").title()
    city = input("Enter Costumer's City of Residence: ")
    province = input("Enter Costumer's Province of Residence (i.e. NL): ")

    provinces = ["AB","BC","MB","NB","NL","NT","NS","NU","ON","PE","QC","SK","YT"]
    valProvince = False
    while valProvince == False:
        for i in provinces:
            if i == province:
                valProvince = True
        if valProvince != True:
            print()
            print("ERROR: MUST ENTER VALID PROVINCE")
            print()
            province = input("Enter Costumer's Province of Residence (i.e. NL): ")

    postCode = input("Enter Costumer's Postal Code: ")
    phoneNum = input("Enter Costumer's Phone Number: ")
    numCar = int(input("Enter Number of Cars Being Insured: "))
    liability = input("Extra Liability up to $1,000,000 (Y/N)? ").title()
    while True:
        if liability != "Y" and liability != "N":
            print()
            print("ERROR: MUST ENTER (Y/N)")
            print()
            liability = input("Extra Liability up to $1,000,000 (Y/N)? ").title()
        else:
            break

    glassCov = input("Optional Glass Coverage (Y/N): ").title()
    while True:
        if glassCov != "Y" and glassCov != "N":
            print()
            print("ERROR: MUST ENTER (Y/N)")
            print()
            glassCov = input("Optional Glass Coverage (Y/N): ").title()
        else:
            break
    loanerCar = input("Optional Loaner Car (Y/N): ").title()
    while True:
        if loanerCar != "Y" and loanerCar != "N":
            print()
            print("ERROR: MUST ENTER (Y/N)")
            print()
            loanerCar = input("Optional Loaner Car (Y/N): ").title()
        else:
            break

    paymentType = input("Enter Payment Type (Full/Monthly): ").title()

    # Calculations:
    insurPrem = COST_BASIC_PREMIUM + ((numCar - 1)* (COST_BASIC_PREMIUM * ADD_CAR_RATE))
    totExtra = 0
    if liability == "Y":
        totExtra += (COST_LIABILITY_COV * numCar)

    if glassCov == "Y":
        totExtra += (COST_GLASS_COV * numCar)

    if loanerCar == "Y":
        totExtra += (COST_LOANER_COV * numCar)

    totInsurPrem = insurPrem + totExtra
    totHST = totInsurPrem * HST_RATE
    totCost = totHST + totInsurPrem

    monthlyPayments = (totCost + PROCESSING_FEE) / 8
    currDate = datetime.datetime.now()
    currDate = currDate.strftime('%m-%d-%Y')
    firstPayDate = f"{currDate[0]}{(int(currDate[1])+1)}-01-{currDate[6:]}"

    # Reciept:
    print()
    print()
    print(f"       One Stop Insurance Company      ")
    print(f"            Invoice Reciept            ")
    print()
    print(f" ------------------------------------- ")
    print(f" Invoice Date: {currDate}")
    print()
    print(f" Client Name and Adress:")
    print()
    print(f" {fName} {lName}")
    print(f" {address}")
    print(f" {city}, {province} {postCode}")
    print()
    print(f" Phone: {phoneNum} ")
    print()
    print(f" Payment Type:                   {paymentType}")
    print(f" Number of Car's:                {numCar}")
    print(f" Liability Coverage:             {liability}")
    print(f" Glass Coverage:                 {glassCov}")
    print(f" Loaner Car Coverage:            {loanerCar}")
    print(f"                          ----------")
    print(f" Insurance Premiums:             {f'${insurPrem:,.2f}':>10s}")
    print(f" Extra charges:                  {f'${totExtra:,.2f}':>10s}")
    print(f" Total Insurance Premiums:       {f'${totInsurPrem:,.2f}':>10s}")
    print(f"                          ----------")
    print(f" Total HST:                      {f'${totHST:,.2f}':>10s}")
    print(f" Total Cost:                     {f'${totCost:,.2f}':>10s}")
    print()
    if paymentType == "Monthly":
        print(f"                          ----------")
        print(f" Monthly Total:                  {f'${monthlyPayments:,.2f}':>10s}")
        print(f" Total Number of Month's:          8")
        print(f" Date of First Payment:            {firstPayDate}")
    print(f" ------------------------------------- ")
    print()

    # Data Collection:

    print("Saving Policy Information...(0%)")
    f = open("Policies.dat","a")

    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(str(currDate)))
    f.write("{}, ".format(str(fName)))
    f.write("{}, ".format(str(lName)))
    f.write("{}, ".format(str(address)))
    f.write("{}, ".format(str(city)))
    f.write("{}, ".format(str(province)))
    print("Saving Policy Information...(50%)")
    f.write("{}, ".format(str(postCode)))
    f.write("{}, ".format(str(phoneNum)))
    f.write("{}, ".format(str(numCar)))
    f.write("{}, ".format(str(liability)))
    f.write("{}, ".format(str(glassCov)))
    f.write("{}, ".format(str(loanerCar)))
    f.write("{}, ".format(str(paymentType)))
    f.write("{}".format(str(totInsurPrem)))
    f.write("\n")

    f.close()

    print("Saving Policy Information...(100%)")
    print()
    print("Policy information processed and saved")
    print()

    POLICY_NUM += 1
    


    cont = input("Would You Like To Enter Another Invoice (Y/N) ?").title()
    if cont == "N":
        break

f = open("OSCIDef.dat","w")

f.write("{}\n".format(str(POLICY_NUM)))
f.write("{}\n".format(str(COST_BASIC_PREMIUM)))
f.write("{}\n".format(str(ADD_CAR_RATE)))
f.write("{}\n".format(str(COST_LIABILITY_COV)))
f.write("{}\n".format(str(COST_GLASS_COV)))
f.write("{}\n".format(str(COST_LOANER_COV)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(PROCESSING_FEE)))

f.close()




