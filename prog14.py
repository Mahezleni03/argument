def total_cal(bill_amt,tip_perc):
    total = bill_amt + (1 + 0.01 * tip_perc)
    total = round(total,2)
    print("Please pay", total)

total_cal(150,20)