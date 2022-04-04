
def check_balance(checking,savings):
    # add checking and savings together and save it for later
    bank_balance = checking + savings 

    # assign all of the strings
    checking_statement = "Your checking balance is $" + str(checking)
    savings_statment   = "Your savings balance is $" + str(savings)
    total_statement = "Your total balance is $" + str(bank_balance) + "\nHave a great day!\n"

    # print out the statements
    print(checking_statement)
    print(savings_statment)
    print(total_statement)


def process_deposit(deposit,initial_savings_balance): 
    return deposit + initial_savings_balance

# charge a fee if the customer's balance is under the allowed limit
def process_low_balance_fee(fee,limit,checking_balance):
    if checking_balance < limit :
        checking_balance = checking_balance - low_balance_fee
    else:
        pass

    return  checking_balance


##### all of our code outside the function is below 

shay_checking = 95 # this is a comment
shay_savings = 5000 # bank stuff 
shay_savings_deposit = 200

low_balance_fee = 5 
low_balance_limit = 100

# madie_checking = 0
# madie_savings = 40000

jared_checking = 101 
jared_savings = 1

# check_balance(jared_checking,jared_saving)
#check_balance(madie_checking,madie_savings)

shay_savings = process_deposit(shay_savings_deposit,shay_savings)
shay_checking   = process_low_balance_fee(low_balance_fee,low_balance_limit,shay_checking)
check_balance(shay_checking,shay_savings)

jared_checking   = process_low_balance_fee(low_balance_fee,low_balance_limit,jared_checking)
check_balance(jared_checking,jared_savings)