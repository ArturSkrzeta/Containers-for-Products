def wrap_order(amount):

    if amount > 100:
        return "Max amount is 100!"


    if amount > 15:
        if amount % 9 == 0:
            return(str(int(amount/9)) + " big container(s)")
        elif amount % 9 == 1 or amount % 9 == 2 or amount % 9 == 3:
            return(str(int(amount/9)) + " big container(s) and " + str(1) + " small container")
        elif amount % 9 == 4 or amount % 9 == 5 or amount % 9 == 6:
            return(str(int(amount/9)) + " big container(s) and " + str(1) + " medium container")
        elif amount % 9 > 6:
            return(str(int(amount/9)+1) + " big conainer(s)")

    if amount >= 10:
        if amount % 9 == 1 or amount % 9 == 2 or amount % 9 == 3:
            return ("2 medium containers")
        elif amount % 9 == 4 or amount % 9 == 5 or amount % 9 == 6:
            return ("2 big containers")

    if amount in [7,8,9]:
        return("1 big container")

    if amount in [4,5,6]:
        return("1 medium container")

    if amount in [1,2,3]:
        return("1 small container")

    if amount <= 0:
        return "Amount needs to be greater than 0"


def main():

    assert wrap_order(-1) == "Amount needs to be greater than 0", "Failed when testing amount: -1"
    assert wrap_order(1) == "1 small container", "Failed when testing amount: 1"
    assert wrap_order(19) == "2 big container(s) and 1 small container", "Failed when testing amount: 19"
    assert wrap_order(30) == "3 big container(s) and 1 small container", "Failed when testing amount: 30"
    assert wrap_order(102) == "Max amount is 100!", "Failed when testing amount: 102"

if __name__ == '__main__':
  main()
