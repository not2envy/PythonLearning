#Function created reeuseable
def apply_fee(transactions, threshold, fee_percent=.2):
    #filtered data and transformed it in one line, This is exactly how data pipelines get written.
    return [amount * (1 + fee_percent) for amount in transactions if amount > threshold]


transactions  = [1,25,69,72,54,61,75,83,16]

print(apply_fee(transactions, 60, 0.3))