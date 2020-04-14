from component.MainFunction import Main

def user_option():
    print("")
    print("***Tax Calculator System***")
    print("Please select you condition")
    print("[1] Single/Separated/Divorced/Widowed")
    print("[2] Married")
    print("")
    return(input('Select: '))


def Single_calc():
    sin_inc = int(input("Input your income: $"))

    sin_nci = Main.Single_deduc(sin_inc)

    print("\nYour MPF = $" + str(Main.MPF_calc(sin_inc)))
    print("\nYour net chargeable income = $" + str(sin_nci))

    print("\nYour should pay tax of  = $" + str(Main.Tax_calc(sin_nci)))

    input("\nPress Enter to continue...")

def Joint_calc():
    hus_inc = int(input("Input husband's personal input per year: $"))
    wife_inc = int(input("Input wife's personal input per year: $"))

    hus_nci = Main.Single_deduc(hus_inc)
    wife_nci = Main.Single_deduc(wife_inc)
    joint_nci = Main.Joint_deduc(hus_inc,wife_inc)

    print("\nHusband's MPF = $" + str(Main.MPF_calc(hus_inc)))
    print("Wife's MPF = $" + str(Main.MPF_calc(wife_inc)))

    print("\nHusband's net chargeable income = $" + str(hus_nci))
    print("Husbandls tax = $" + str(Main.Tax_calc(hus_nci)))

    print("\nWife's net chargeable income = $" + str(wife_nci))
    print("Wife's tax = $" + str(Main.Tax_calc(wife_nci)))

    sinTax = Main.Tax_calc(hus_nci) + Main.Tax_calc(wife_nci)

    print("\nPay Tax in Separate way = $" + str(sinTax))

    joiTax = Main.Tax_calc(joint_nci)
    print("Joint net chargeable income = $" + str(joint_nci))
    print("Pay Tax in Joint way = $" + str(joiTax))

    if sinTax<=joiTax:
        print("\nRecommended method = Seperated taxation $"+str(sinTax))
    else:
        print("\nRecommended method = Joint taxation $" + str(joiTax))
    input("\nPress Enter to continue...")

option = user_option()

while option != "0":
    if option == "1":
        Single_calc()
    if option == "2":
        Joint_calc()
    else:
        print("\n!!!!!Please enter a number!!!!!")

    option = user_option()

print('Finished')
