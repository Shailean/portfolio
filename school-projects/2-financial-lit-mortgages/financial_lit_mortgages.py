import random
import time

# Create an applicant's financial information
credit_cards = ["Macys", "Chase", "Discover"]
credit_cards2 = ["Capital One", "American Express", "Bank of America"]
loans = ["student loans", "auto loan", "personal loan"]
credit_scores = [440, 570, 600, 620, 410, 550]
income = [45000, 55000, 95000]


# Lists to hold applicant's information
applicant = []
applicant_finances = []
mortgage_front_end_ratio = []
mortgage_back_end_ratio = []
applicant_credit_score = []
completed_recs = []


# Timing of each prompt
def print_sleep(message):
    print(message)
    time.sleep(2)


def print_slow(message):
    print(message)
    time.sleep(4)


# Function that starts the game
def play_game():
    intro()
    applicant_name()
    mortgage_affordability()
    debt_affordability()
    income_assessment()


# Applicant's financial information
def applicant_information():
    applicant_income = random.choice(income)
    applicant_finances.append(applicant_income)
    print_sleep("Income: $" + str(applicant_income))
    applicant_loans = random.randint(300, 501)
    applicant_finances.append(applicant_loans)
    print_sleep("Monthly loan payment: " + "'" + random.choice(loans) + "'" +
                " amounting to: $" + str(applicant_loans))
    applicant_credit_cards = random.randint(50, 501)
    applicant_finances.append(applicant_credit_cards)
    print_sleep("Monthly credit card payments: " + "'"
                + random.choice(credit_cards) + "'" +
                " and " + "'" + random.choice(credit_cards2) +
                "'" + " amounting to: $"
                + str(applicant_credit_cards))


# Game introduction prompts
def intro():
    print_sleep("\nHome ownership is the main pathway to building "
                "wealth that can be passed on to dependents.")
    print_sleep("\nIn this game you are a loan officer at a bank.")
    print_sleep("\nYou are working through some mortgage applications.")
    print_sleep("You need to decide if each applicant will be approved "
                "for a home loan based on their financial situation.")
    print_sleep("\nYour goal is to help them make good financial decisions "
                "that will allow them to be approved for a home loan "
                "(mortgage) that is within their budget.\nYou will start "
                "by choosing an applicant's file.\n")


# Check to ensure that user selects the correct player/applicant name options
def valid_applicant_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_sleep("I don't understand your response.")
    return response


# User selects applicant's name/file
def applicant_name():
    response = valid_applicant_input("Please type the name of the applicant "
                                     "whose file you would like to review:"
                                     "\n\n- DREW,\n- MARIA, or\n- TAYLOR\n\n",
                                     "drew", "maria", "taylor")
    if "drew" in response:
        print_sleep("\nYou have selected Drew. Your goal is to help Drew get "
                    "approved for a mortgage.")
        applicant.append("Drew")
        print_slow("\n--------------------------")
        print_sleep("\nHere are Drew's finances:\n")
        applicant_information()
    elif "maria" in response:
        print_sleep("\nYou have selected Maria. Your goal is to help Maria "
                    "get approved for a mortgage.")
        applicant.append("Maria")
        print_slow("\n--------------------------")
        print_sleep("\nHere are Maria's finances:\n")
        applicant_information()
    elif "taylor" in response:
        print_sleep("\nYou have selected Taylor. Your goal is to help "
                    "Taylor get approved for a mortgage.")
        applicant.append("Taylor")
        print_slow("\n--------------------------")
        print_sleep("\nHere are Taylor's finances:\n")
        applicant_information()


# STEP 1: Is applicant's income sufficient for monthly mortgage pmnt?
def mortgage_affordability():
    # FRONT-END RATIO: Monthly mortgage pmnt should be 28% or less of income?
    # # Intro prompts
    print_slow("\n--------------------------")
    print_slow("\nBanks typically want mortgage payments to be 28 "
               "percent or less of monthly gross income.")
    print_slow("Let's see if " + applicant[0] + "'s income can sustain "
               "a mortgage for the home they'd like to purchase.")
    print_slow("Let's assume that " + applicant[0] + " wants to purchase "
               "a 1-bedroom apartment in your neighborhood. \nWe will use "
               "current rent prices for a 1-bedroom in your area to "
               "determine the monthly mortgage amount.")
    # Validate user input: user selects monthly mortgage amount
    response = valid_mortgage_input("\nSelect a reasonable monthly rent "
                                    "amount:\n$800\n$1500\n$3500\n\n", "800",
                                    "1500", "3500")
    if "800" in response:
        print_sleep("\nYou have selected $800.")
    elif "1500" in response:
        print_sleep("\nYou have selected $1,500.")
    elif "3500" in response:
        print_sleep("\nYou have selected $3,500.")

    # Monthly gross income calculation
    gross_monthly_income = round((applicant_finances[0] / 12))
    allowable_mortgage_pmnt = round((gross_monthly_income * 0.28))
    print_sleep("\nHere is " + applicant[0] + "'s gross monthly income: $"
                + str(gross_monthly_income))
    print_sleep("We calculated this number by dividing the annual gross "
                "income by 12: $" + str(applicant_finances[0]) + " / 12")
    print_sleep("Now we need to calculate the percentage of gross monthly "
                "income that will go towards paying the monthly "
                "mortgage payment:\n")

    # Calculate front-end ratio: Are mortgage payments 28% or less of income?
    if "800" in response:
        front_end_ratio = round(((800/gross_monthly_income))*100)
        mortgage_front_end_ratio.append(front_end_ratio)
    elif "1500" in response:
        front_end_ratio = round(((1500/gross_monthly_income))*100)
        mortgage_front_end_ratio.append(front_end_ratio)
    elif "3500" in response:
        front_end_ratio = round(((3500/gross_monthly_income)*100))
        mortgage_front_end_ratio.append(front_end_ratio)
    print_sleep(str(front_end_ratio) + " percent")

    if front_end_ratio > 28:
        print_sleep("\n- " + applicant[0] + "'s income is too low.")
        print_sleep("\nRemember, banks want this number to be 28 "
                    "percent or less.")
        print_sleep("Based on " + applicant[0] + "'s income, "
                    + applicant[0] + " can only afford a monthly mortgage "
                    "payment of: $" + str(allowable_mortgage_pmnt))
        print_sleep("This is 28 percent " + applicant[0] + "'s income, "
                    "which is the maximum the bank will allow for a "
                    "monthly mortgage payment.")
    else:
        print_sleep("\n- " + applicant[0] + " has sufficient income to "
                    "afford monthly mortgage payments.")


# Ensure that user selects from the provided monthly mortgage payment options
def valid_mortgage_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt)
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_sleep("I don't understand your response.")
    return response


# STEP 2: Is applicant's income sufficient for current monthly debt payments?
def debt_affordability():
    # BACK-END RATIO: Monthly debt payments should be 36% or less of income?
    print_slow("\n--------------------------")
    print_slow("\nLet's take a look at " + applicant[0] + "'s current "
               "monthly debt payments to see if " + applicant[0] +
               " can afford to take on the additional debt of the mortgage.")
    # Calculations
    gross_monthly_income = round((applicant_finances[0] / 12))
    allowable_debt = round((gross_monthly_income * 0.36))

    # Intro
    print_slow("\nBanks consider the percentage of applicants' income that "
               "goes toward debt repayment. "
               "\nBanks typically want total debt payments to be 36 percent "
               "or less of monthly gross income.\n")
    print_slow("- " + applicant[0] + "'s gross monthly income is: $"
               + str(gross_monthly_income))

    # Calculate back-end ratio: Are debt monthly pmnts 36% or less of income?
    current_debts = applicant_finances[1] + applicant_finances[2]
    back_end_ratio = round(((current_debts/gross_monthly_income)*100))
    mortgage_back_end_ratio.append(back_end_ratio)
    print_slow("- " + applicant[0] + " already has $" + str(current_debts) +
               " in loan and credit card monthly payments. "
               "\n- Based on " + applicant[0] + "'s income and current debts, "
               + str(back_end_ratio) + " percent of " + applicant[0] +
               "'s income is going towards monthly debt repayment.")

    if back_end_ratio > 36:
        print_slow("- " + applicant[0] + "'s debt is too high. "
                   + applicant[0] + " can only have $" + str(allowable_debt) +
                   " in current debts.")
    else:
        print_slow("- " + applicant[0] + " has sufficient income to support "
                   "current debts.")


# STEP 3: Check for sufficient income for both front-end and back-end ratios?
def income_assessment():
    if mortgage_front_end_ratio[0] <= 28 and mortgage_back_end_ratio[0] <= 36:
        print_sleep("\nCongratulations! " + applicant[0] + "'s income "
                    "qualifies them for mortgage approval.")
        completed_recs.append("Income meets criteria")
    else:
        print_sleep("\nUnfortunately, " + applicant[0] + "'s income does not"
                    " qualify them for mortgage approval for one or both of "
                    "the following reasons:"
                    "\n1. Insufficient income for the monthly mortgage payment"
                    "\n2. Insufficient income for the current monthly debt "
                    "repayment")
    credit_score_check()


# STEP 4: Credit score high enough for mortgage approval?
def credit_score_check():
    # Intro prompts
    print_sleep("\n--------------------------")
    print_slow("\nBanks also have to run a credit score review in order to see"
               " if applicants meet the minimum credit score criteria. "
               "\nEveryone has 3 credit scores: one from each of the 3 "
               "credit bureaus.\nBanks check all 3 for each applicant and "
               "pick the middle credit score to determine whether the "
               "applicant is trustworthy enough to pay back their debts.")

    # User input
    valid_credit_score_input("\nPress the number 1 to check the middle "
                             "credit score:\n", 1)
    print_sleep("\nProcessing... ")
    print_slow("Please wait...\n")

    # Pulling credit score from list options
    applicant_score = random.choice(credit_scores)
    applicant_credit_score.append(applicant_score)
    print_sleep(applicant_credit_score[0])
    print_sleep("\nUnfortunately, " + applicant[0] + "'s credit score "
                "isn't high enough to qualify for a mortgage. "
                "\nThe minimum credit score the bank will accept is 700.")
    print_sleep("\nWhat would you recommend " + applicant[0] + " do in "
                "order to get approved for a mortgage?")
    recommendation()


# Check to ensure that user selects from the provided credit score options
def valid_credit_score_input(prompt, option1):
    while True:
        response = int((input(prompt)))
        if response == option1:
            break
        else:
            print("I don't understand your response.")
    return response


# STEP 5: User selects recommendations for mortgage approval
def recommendation():
    response = valid_recommendation_input("\nSelect the number that "
                                          "corresponds with the recommendation"
                                          " you'd make to " + applicant[0] +
                                          ":\n1. Increase income\n2. Pay off "
                                          "debt\n", 1, 2)
    if response == 1:
        increase_income()
    elif response == 2:
        debt()


# Check to ensure that user selects from the provided recommendation options
def valid_recommendation_input(prompt, option1, option2):
    while True:
        response = int((input(prompt)))
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_sleep("I don't understand your response.")
    return response


# Increase income recommendation
def increase_income():
    print_sleep("\n--------------------------")
    print_sleep("You've suggested that " + applicant[0] + " work on "
                "increasing income.")
    if "Income meets criteria" in completed_recs:
        print_sleep("\n" + applicant[0] + "'s income already qualifies for "
                    "the mortgage requested. Increasing income will not "
                    "have any meaningful impact.")
    elif "Increase income" in completed_recs:
        print_sleep("\nYou've already brainstormed ideas to increase income "
                    "with " + applicant[0] + ".")
    else:
        print_sleep("\nBrainstorm ideas for " + applicant[0] + " to meet "
                    "the income requirements of the mortgage."
                    "\nAlternatively, " + applicant[0] + " could select a "
                    "less expensive home to purchase that their income "
                    "can support.")
        print_sleep("A note has been added to " + applicant[0] + "'s file "
                    "that " + applicant[0] + " has met with you to discuss "
                    "income and mortgage requirements.")
        completed_recs.append("Increase income")
    recommendation_check()


# Pay off debt recommendation
def debt():
    print_sleep("\n--------------------------")
    print_slow("You've suggested that " + applicant[0] + " work on "
               "reducing debts.")
    if "Pay off debt" in completed_recs:
        print_slow("\nYou've already discussed debt repayment and credit "
                   "scores with " + applicant[0] + ".")
        recommendation_check()
    else:
        print_slow("\nLet's review " + applicant[0] + "'s monthly debt "
                   "payments:\n")
        current_debts = round(applicant_finances[1] + applicant_finances[2])
        print_slow("- " + applicant[0] + " is currently paying $"
                   + str(current_debts) + " towards loans and credit cards.\n "
                   "\nOne of the factors that affect credit scores is the "
                   "amount of debt that someone has. \nAs debt balances get "
                   "paid down credit scores typically increase. \nThis is one"
                   " strategy that " + applicant[0] + " can try to improve "
                   "their chances of getting mortgage approval.")
        print_slow("\nHigh credit scores also have another benefit: the higher"
                   " the credit score, the lower the mortgage interest rate. "
                   "\nA note has been added to " + applicant[0] + "'s file "
                   "that " + applicant[0] + " has met with you to discuss "
                   "credit scores and mortgage requirements.")
        completed_recs.append("Pay off debt")
        recommendation_check()


# Check to see that user has selected all recommendations
def recommendation_check():
    if "Pay off debt" in completed_recs and ("Increase income" in
                                             completed_recs or "Income meets "
                                             "criteria" in completed_recs):
        print_sleep("\n--------------------------")
        print_slow("\nCongratulations! You've helped " + applicant[0] +
                   " understand the financial "
                   "requirements of a mortgage which will move them closer to "
                   "approval.")
        print_sleep("\n--------------------------")
        play_again()
    else:
        print_sleep("\nPlease select a different recommendation.")
        recommendation()


# Offer user the option to play again
def play_again():
    response = valid_play_again_input("\nWould you like to play again?\nYes "
                                      "or No\n\n", "yes", "no")
    applicant.clear()
    applicant_finances.clear()
    mortgage_front_end_ratio.clear()
    mortgage_back_end_ratio.clear()
    applicant_credit_score.clear()
    completed_recs.clear()
    if "yes" in response:
        print_sleep("\nGame restarting...")
        play_game()
    else:
        print("Thanks for playing! See you again soon.\n")


# Check to ensure that user selects from the provided play again options
def valid_play_again_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_sleep("I don't understand your response.")
    return response


play_game()
