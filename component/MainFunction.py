class Main(object):
    def cal_MPF(income):
        if income < 7100*12:
            mpf = 0
        elif income >= 30000*12:
            mpf = 1500*12
        else:
            mpf = income*0.05
        return mpf

    def cal_tax(nt):
        sRate = 0.15
        sTax = nt * sRate

        pRate = 0.02
        pTax = 0
        nci_per_year = 50000
        while nt > 0:
            if nt > nci_per_year:
                pTax = pTax + nci_per_year * pRate
                pRate += 0.04
                nt = nt - nci_per_year
                if pRate > 0.14:
                    pTax = pTax + nt * 0.17
                    break
            else:
                pTax = pTax + nt * pRate
                break

        if pTax >= sTax:
            tax = sTax
        else:
            tax = pTax
        return tax

    def chk_Tax(nt):
        sRate = 0.15
        sTax = nt * sRate

        pRate = 0.02
        pTax = 0
        nci_per_year = 50000
        while nt > 0:
            if nt > nci_per_year:
                pTax = pTax + nci_per_year * pRate
                pRate += 0.04
                nt = nt - nci_per_year
                if pRate > 0.14:
                    pTax = pTax + nt * 0.17
                    break
            else:
                pTax = pTax + nt * pRate
                break

        if pTax >= sTax:
            return 1
        else:
            return 2

    #net changeable income with separate taxation
    def cal_SncIncome(income):
        basic_allowance = 132000
        netIncome = income - Main.cal_MPF(income)
        check = Main.chk_Tax(income)
        if check == 1:
            nci = netIncome
            return nci
        elif netIncome>basic_allowance:
            nci = netIncome - basic_allowance
            return nci
        else:
            return 0

    #net changeable income with joint taxation
    def cal_JncIncome(husband_income, wife_income):
        basic_allowance = 132000*2
        husband_netIncome = husband_income - Main.cal_MPF(husband_income)
        wife_netIncome = wife_income - Main.cal_MPF(wife_income)
        joint_netIncome = husband_netIncome + wife_netIncome
        chk_husband = Main.chk_Tax(husband_netIncome)
        chk_wife = Main.chk_Tax(wife_netIncome)
        if chk_husband == 1:
            nci = joint_netIncome
            return nci
        elif chk_wife == 1:
            nci = joint_netIncome
            return nci
        elif joint_netIncome > basic_allowance:
            nci = joint_netIncome - basic_allowance
            return nci
        else:
            return 0
