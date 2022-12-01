# One Stop Insurance Company
# Program that allows user input customer information for the purpose of printing
# an insurance policy receipt

# AUTHOR: JONATHAN IVANY
# DATE : 2022 - 11 - 21

from datetime import datetime, timedelta
import FormatValues as Fv


# initialize today's date
Today = datetime.now()


# Sets for validating
ALLOWED_LOWCHAR = set("abcdefghijklmnopqrstuvwxyz")
ALLOWED_UPCHAR = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ALLOWED_NUM = set("1234567890")

# Open default file and read values to assigned variable
f = open('OSICDef.dat', 'r')

POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
LIABILITY_COVER_COST = float(f.readline())
GLASS_COVER_COST = float(f.readline())
RENTAL_COVER_COST = float(f.readline())
HST_RATE = float(f.readline())
M_PROCESS_FEE = float(f.readline())

f.close()

# Initialize loop so multiple claims can be made without ending program or returning to menu
while True:
    print()
    print("    ONE STOP COMPANY INSURANCE COMPANY ")
    print("-"*41)
    print("       Insurance Policy Processing     ")

    print()
    print("="*6, "ENTER CUSTOMERS INFORMATION", "="*6)

    while True:  # Validate first name was entered
        FName = input("First name: ").title()
        if FName == " " or FName == "":
            print("Please enter the Customer's first name.")
        else:
            break

    while True:  # Validate last name was entered
        LName = input("Last name: ").title()
        if LName == " " or LName == "":
            print("Please enter the Customer's last name.")
        else:
            break

    while True:  # Validate Street address was entered
        StAdd = input("Street address: ")
        if StAdd == " " or StAdd == "":
            print("Please enter the Customer's street address.")
            print("Example: ### XXXXXXXX XX |or| 10 Macdonald drive.")
        else:
            break

    while True:  # Validate City was entered
        City = input("City: ")
        if City == " " or City == "":
            print("Please enter City associated with Customer's address.")
        else:
            break

    while True:  # Validate Province was entered in XX format
        Province = input("Province(XX): ").upper()
        if Province == " " or Province == "":
            print("Sorry, you must enter the province. (i.e: NL)")
        elif not set(Province).issubset(ALLOWED_UPCHAR) or not set(Province).issubset(Province):
            print("Please enter valid province in 2 letter format. ie: NL")
        elif len(Province) != 2:
            print("Sorry. Please enter province in a 2 letter format. (i.e: NL)")
        else:
            break

    while True:  # Validate Postal Code in format A1A1A1
        PostCode = input("Postal Code(A1A1A1): ")
        if PostCode == " " or PostCode == "":
            print("Please enter postal code.")
        elif Fv.ValPostal(PostCode) == False:
            print("Postal Code format invalid. Please try again. (Ex: A1B2C3)")
        else:
            break

    while True:  # Validate Phone Number in 10 digit format
        PhoneNum = input("Phone Number: ")
        if Fv.ValDigOnly(PhoneNum) == False:
            print("Enter a 10-digit phone number. Please try again")
        else:
            break


    while True:  # Validate Number of cars was entered as a number for use in calculations
        try:
            NumCar = int(input("Number of cars: "))
            break
        except ValueError:
            print("Please enter numbers only.")



    print()
    print("="*8, "ENTER INSURANCE OPTIONS", "="*8)

    while True:  # Validate option for extra liability coverage
        XtraLiability = input("Extra liability up to $1,000,000? (Y/N): ").upper()
        if XtraLiability == "N":
            XtraLiability = "(No)"
            XtraLiaCost = 0
            break
        elif XtraLiability == "Y":
            XtraLiability = "(Yes)"
            XtraLiaCost = LIABILITY_COVER_COST
            break
        else:
            print()
            print("Options are Y for YES or N for NO")
            print("--------Please Try Again---------")
            print()

    while True:  # Validate option for extra glass coverage
        OptGlassCov = input("Glass coverage? (Y/N): ").upper()
        if OptGlassCov == "N":
            OptGlassCov = "(No)"
            GlassCoverage = 0
            break
        elif OptGlassCov == "Y":
            OptGlassCov = "(Yes)"
            GlassCoverage = GLASS_COVER_COST
            break
        else:
            print()
            print("Options are Y for YES or N for NO")
            print("--------Please Try Again---------")
            print()

    while True:  # Validate option for a rental car
        OptLoanCar = input("Loaner Car? (Y/N): ").upper()
        if OptLoanCar == "N":
            OptLoanCar = "(No)"
            LoanCarCost = 0
            break
        elif OptLoanCar == "Y":
            OptLoanCar = "(Yes)"
            LoanCarCost = RENTAL_COVER_COST
            break
        else:
            print()
            print("Options are Y for YES or N for NO")
            print("--------Please Try Again---------")
            print()

    while True:  # Validate option for payment method
        PayMethod = input("Pay in Full or 8 Monthly Payments? (F/M): ").upper()
        if PayMethod == "F":
            PayMethod = "Full"
            MonthlyPay = False
            break
        elif PayMethod == "M":
            PayMethod = "Monthly"
            MonthlyPay = True
            break
        else:
            print()
            print("Options are M for Monthly or F for Full")
            print("-----------Please Try Again------------")
            print()


    # Calculate cost of premium insurance, discount if customer has more than 1 car
    if NumCar > 1:
        FirstCar = BASIC_PREMIUM
        AddCarCost = (BASIC_PREMIUM - (BASIC_PREMIUM * ADD_CAR_DISCOUNT)) * (NumCar - 1)
        PremInsure = FirstCar + AddCarCost
    else:
        PremInsure = BASIC_PREMIUM

    # Initialize Total extras cost
    TotalExCost = 0

    if XtraLiability == "(Yes)":
        TotalExCost += LIABILITY_COVER_COST * NumCar

    if OptGlassCov == "(Yes)":
        TotalExCost += GLASS_COVER_COST * NumCar

    if OptLoanCar == "(Yes)":
        TotalExCost += RENTAL_COVER_COST * NumCar

    # Total Insurance premium is base premium + all the chosen extras
    TotInsPrem = PremInsure + TotalExCost

    # HST is based off the total insurance premium
    HST = TotInsPrem * HST_RATE

    # Total cost is the hst added to the total insurance premium
    TotalCost = HST + TotInsPrem

    # If customer chooses to pay monthly, the pay is spread over 8 months
    # A monthly process fee is added to the total cost then divided over 8 months
    PayPerMonth = (TotalCost + M_PROCESS_FEE) / 8

    # Custom policy number in format ####-XX (Policy number-Customers First Initials)
    CustPolicyNum = f'{POLICY_NUM}-{FName[0]}{LName[0]}'

    # Print the receipt for customers insurance policy
    print()
    print("             ONE STOP INSURANCE COMPANY")
    print("             ~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              INSURANCE POLICY RECEIPT")
    print()
    print(f"      POLICY #: {CustPolicyNum:>7s}      DATE: {Fv.FDateMFullYear(Today):<15s}")
    print("      ========================================")
    print(f"                 {FName[0:1]:<1s}, {LName:<24s} ")
    print(f"                 {StAdd:<25s}")
    print(f"                 {City},{Province:<2s} {PostCode:<6s}")
    print(f"                 PHONE:  {PhoneNum:>10s}")
    print("      ========================================")
    print("      |    POLICY ADD-ONS    | OPTION | COST |")
    print("      ----------------------------------------")
    print(f"      XTRA LIABILITY COVERAGE:  {XtraLiability:<5s}  {Fv.FDollar2(XtraLiaCost):>7s}")
    print(f"      GLASS COVERAGE:           {OptGlassCov:<5s}  {Fv.FDollar2(GlassCoverage):>7s}")
    print(f"      LOANER CAR COVERAGE:      {OptLoanCar:<5s}  {Fv.FDollar2(LoanCarCost):>7s}")
    print("      ----------------------------------------")
    print(f"      CARS ON POLICY:           ({NumCar:>2d} )")
    print(f"      ADD-ONS TOTAL:                 {Fv.FDollar2(TotalExCost):>9s}")
    print(f"      INSURANCE PREMIUMS:            {Fv.FDollar2(PremInsure):>9s}")
    print("      ----------------------------------------")
    print(f"      TOTAL INSURANCE PREMIUM:      {Fv.FDollar2(TotInsPrem):>10s}")
    print(f"      HST:                           {Fv.FDollar2(HST):>9s}")
    print("      ========================================")
    # If customer chooses to pay monthly display the monthly cost
    # along with the pay period
    if MonthlyPay == True:
        print("                 8 MONTH PAY PERIOD")
        if datetime.today().day >= 25:
            try:
                FirstPay = (Today.replace(day=1) + timedelta(days=62)).replace(day=1)
                EightMonth = (Today.replace(day=1) + timedelta(days=305)).replace(day=1)
            except ValueError:  # January 31 will return last day of February.
                FirstPay = (Today + timedelta(days=62)).replace(day=1) - timedelta(days=1)
                EightMonth = (Today + timedelta(days=305)).replace(day=1) - timedelta(days=1)
        else:
            try:
                FirstPay = (Today.replace(day=1) + timedelta(days=31)).replace(day=1)
                EightMonth = (Today.replace(day=1) + timedelta(days=274)).replace(day=1)
            except ValueError:  # January 31 will return last day of February.
                FirstPay = (Today + timedelta(days=31)).replace(day=1) - timedelta(days=1)
                EightMonth = (Today + timedelta(days=274)).replace(day=1) - timedelta(days=1)

        print(f"      FROM:   {Fv.FDateS(FirstPay)}      TO:   {Fv.FDateS(EightMonth)}")
        print(f"      PER MONTH:                     {Fv.FDollar2(PayPerMonth):>9s}")
        print(f"      TOTAL:                        {Fv.FDollar2(TotalCost):>10s}")
    else:
        print(f"      TOTAL:                        {Fv.FDollar2(TotalCost):>10s}")

    # Open policy file and add customer policy info then close file.
    f = open('Policies.dat', 'a')

    f.write("{}, ".format(str(CustPolicyNum)))
    f.write("{}, ".format(str(FName)))
    f.write("{}, ".format(str(LName)))
    f.write("{}, ".format(str(StAdd)))
    f.write("{}, ".format(str(City)))
    f.write("{}, ".format(str(Province)))
    f.write("{}, ".format(str(PostCode)))
    f.write("{}, ".format(str(PhoneNum)))
    f.write("{}, ".format(str(NumCar)))
    f.write("{}, ".format(str(XtraLiability)))
    f.write("{}, ".format(str(OptGlassCov)))
    f.write("{}, ".format(str(OptLoanCar)))
    f.write("{}, ".format(str(PayMethod)))
    f.write("{}\n ".format(str(Fv.FDollar2(TotalCost))))

    f.close()

    print()
    print("Policy information successfully saved!")
    POLICY_NUM += 1  # Increase policy number by 1 for next policy

    print()
    # User has option to file another claim or return to main menu
    Continue = input("Would you like to make another claim? (Y/N): ").upper()
    if Continue == "Y":
        continue
    elif Continue == "N":
        break
    else:
        print(" Y  for Yes or  N  for No.")

# Open default file, overwrite policy num and format, then close the file
f = open('OSICDef.dat', 'w')

f.write("{}\n".format(str(POLICY_NUM)))
f.write("{}\n".format(str(BASIC_PREMIUM)))
f.write("{}\n".format(str(ADD_CAR_DISCOUNT)))
f.write("{}\n".format(str(LIABILITY_COVER_COST)))
f.write("{}\n".format(str(GLASS_COVER_COST)))
f.write("{}\n".format(str(RENTAL_COVER_COST)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(M_PROCESS_FEE)))

f.close()


