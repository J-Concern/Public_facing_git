import random

#obtain starting variables
expected_interest_rate = float(0.07)
principle_investment = float(100000)
time_of_investment = float(15)
variance_high = 0.20
variance_low = 0.15

def expected_outcome(expected_interest_rate, principle_investment):
    outcome = int(((expected_interest_rate * principle_investment) + principle_investment))
    ytd_return = int(expected_interest_rate * principle_investment)
    print("$ ", outcome)
    return outcome, ytd_return

    
def variance_in_outcome(outcome, variance_high, variance_low):
    n = 0
    variance = random.uniform(variance_low, variance_high)
    print("Random Variance:" ,variance)
    altered_outcome_high = int((outcome * variance) + outcome)
    altered_outcome_low =  int(outcome - (outcome * variance))
    if n == 1:
        altered_outcome_high = altered_outcome_high + (outcome + (altered_outcome_high * variance))
        altered_outcome_low = altered_outcome_low + (outcome + (altered_outcome_high * variance))
    n = n + 1
    return altered_outcome_high, altered_outcome_low

#def graph():

def main(time_of_investment):
    for n in range(0,int(time_of_investment)):
        outcome, ytd_return = expected_outcome(expected_interest_rate, principle_investment)
        altered_outcome_high, altered_outcome_low = variance_in_outcome(outcome, variance_high, variance_low)
        n += 1
        print("High $:",altered_outcome_high, "Low $:", altered_outcome_low)
        outcome = outcome + ytd_return
        print(outcome)



if __name__ == "__main__":
    main(time_of_investment)