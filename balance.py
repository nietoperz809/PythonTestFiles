
def calc (bal, pay, interest):
    ubal = bal - pay
    b1 = ubal + interest/12.0 *ubal
    return b1


