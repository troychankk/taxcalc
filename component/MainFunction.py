class Main(object):
    def MPF_calc(inc):
        if inc < 7100*12:
            mpf = 0
        elif inc >= 30000*12:
            mpf = 1500*12
        else:
            mpf = inc*0.05
        return mpf

    def Tax_calc(nt):
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

    def Tax_chk(nt):
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

    #net changeable inc with separate taxation
    def Single_deduc(inc):
        basic_allow = 132000
        netinc = inc - Main.MPF_calc(inc)
        check = Main.Tax_chk(inc)
        if check == 1:
            nci = netinc
            return nci
        elif netinc > basic_allow:
            nci = netinc - basic_allow
            return nci
        else:
            return 0

    #net changeable inc with joint taxation
    def Joint_deduc(hus_inc, wife_inc):
        basic_allow = 132000*2
        hus_net = hus_inc - Main.MPF_calc(hus_inc)
        wife_net = wife_inc - Main.MPF_calc(wife_inc)
        joint_netinc = hus_net + wife_net
        chk_hus = Main.Tax_chk(hus_net)
        chk_wife = Main.Tax_chk(wife_net)
        if chk_hus == 1:
            nci = joint_netinc
            return nci
        elif chk_wife == 1:
            nci = joint_netinc
            return nci
        elif joint_netinc > basic_allow:
            nci = joint_netinc - basic_allow
            return nci
        else:
            return 0
