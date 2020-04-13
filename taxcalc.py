from component.MainFunction import Main

def user_option():
    print("")
    print("***Tax Calculator System***")
    print("Please select you condition")
    print("[1] Single/Separated/Divorced/Widowed")
    print("[2] Married")
    print("")
    return(input('Select: '))


def cal_SncTax():
    single_income = int(input("Please Enter your income: $"))

    single_nci = Main.cal_SncIncome(single_income)

    print("\nYour MPF = $" + str(Main.cal_MPF(single_income)))
    print("\nYour net chargeable income = $" + str(single_nci))

    print("\nYour tax = $" + str(Main.cal_tax(single_nci)))

    input("\nPress Enter to continue...")

def cal_JncTax():
    husband_income = int(input("Please input husband's personal input per year: $"))
    wife_income = int(input("Please input wife's personal input per year: $"))

    husband_nci = Main.cal_SncIncome(husband_income)
    wife_nci = Main.cal_SncIncome(wife_income)
    joint_nci = Main.cal_JncIncome(husband_income,wife_income)

    print("\nHusband's MPF = $" + str(Main.cal_MPF(husband_income)))
    print("Wife's MPF = $" + str(Main.cal_MPF(wife_income)))

    print("\nHusband's net chargeable income = $" + str(husband_nci))
    print("Husbandls tax = $" + str(Main.cal_tax(husband_nci)))

    print("\nWife's net chargeable income = $" + str(wife_nci))
    print("Wife's tax = $" + str(Main.cal_tax(wife_nci)))

    sTax = Main.cal_tax(husband_nci) + Main.cal_tax(wife_nci)

    print("\nSeparate taxation = $" + str(sTax))

    jTax = Main.cal_tax(joint_nci)
    print("Joint net chargeable income = $" + str(joint_nci))
    print("Joint taxation = $" + str(jTax))

    if sTax<=jTax:
        print("\nRecommended method = Seperated taxation $"+str(sTax))
    else:
        print("\nRecommended method = Joint taxation $" + str(jTax))
    input("\nPress Enter to continue...")

option = user_option()

while option != "0":
    if option == "1":
        cal_SncTax()
    if option == "2":
        cal_JncTax()
    else:
        print("\n!!!!!Please enter a number!!!!!")

    option = user_option()

print('Finished')
