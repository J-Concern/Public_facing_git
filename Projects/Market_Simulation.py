import random
from matplotlib import pyplot as plt

#obtain starting variables
expected_interest_rate = float(0.07)
principle_investment = float(100000)
current_investment = principle_investment
time_of_investment = float(15)
variance_high = .2
variance_low = .15
outcome_low = 0
outcome_high = 0

#function to obtain yearly baseline monetary output and year to date return
def expected_outcome(expected_interest_rate, current_investment):
    interest_gained = expected_interest_rate * current_investment
    current_investment = int(current_investment + interest_gained)
    print("$:",current_investment)
    return current_investment

#function to find a variance from a random number given
def variance_in_outcome(variance_high, variance_low, outcome_high, outcome_low, principle_investment, expected_interest_rate, n = False):
    variance = random.uniform(variance_low, variance_high)
    outcome_modifier_low = expected_interest_rate - (expected_interest_rate *variance)
    outcome_modifier_high = expected_interest_rate + (expected_interest_rate * variance)
    if n == False:
        outcome_low = outcome_modifier_low * principle_investment
        outcome_high = outcome_modifier_high * principle_investment
        n = True
        return outcome_high, outcome_low
    outcome_high = outcome_high +(outcome_high * outcome_modifier_high)
    outcome_low = outcome_low + (outcome_low * outcome_modifier_low)
    return outcome_high, outcome_low


outcome_high, outcome_low = variance_in_outcome(variance_high, variance_low, outcome_high, outcome_low, principle_investment, expected_interest_rate)

variance_in_outcome(variance_high, variance_low, outcome_high, outcome_low, principle_investment, expected_interest_rate)




#main loop
def main(time_of_investment, n=0):
   outcome_high, outcome_low = variance_in_outcome(variance_high, variance_low, outcome_high, outcome_low, principle_investment, expected_interest_rate)
   current_investment = expected_outcome(expected_interest_rate, current_investment)
   while n < time_of_investment:
    print(outcome_high, outcome_low)
    print(current_investment)
    n=n+1


if __name__ == "__main__":
    main(time_of_investment, n=0)