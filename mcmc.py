import sorobn as hh
import pandas as pd
import random
import math

###---------------------PART A---------------------###

bn = hh.BayesNet(
    ('C', ['S', 'R']),
    ('S', 'W'),
    ('R', 'W')
)

bn.P['C'] = pd.Series({True: 0.5, False: 0.5})
bn.P['S'] = pd.Series({
    (True, True): 0.1, (True, False): 0.9,
    (False, True): 0.5, (False, False): 0.5
})

bn.P['R'] = pd.Series({
    (True, True): 0.8, (True, False): 0.2,
    (False, True): 0.2, (False, False): 0.8

})
bn.P['W'] = pd.Series({
    (True, True, True): 0.99, (True, True, False): 0.01,
    # (True, False, True): 0.95, (True, False, False): 0.05,
    # (False, True, True): 0.9, (False, True, False): 0.1,
    (True, False, True): 0.9, (True, False, False): 0.1,
    (False, True, True): 0.95, (False, True, False): 0.05,
    (False, False, True): 0.05, (False, False, False): 0.95
})

bn.prepare()
probability_false, probability_true = bn.query('C',  event = {'S': False, 'W': True})


###---------------------PART B---------------------###

Prob_1 = [0.87804878048780487804878048780486, 0.12195121951219512195121951219512] # P(C|-s,r)
Prob_2 = [0.31034482758620689655172413793103, 0.68965517241379310344827586206896] # P(C|-s,-r)
Prob_3 = [0.98630136986301369863013698630137, 0.01369863013698630136986301369863] # P(R|c,-s,w)
Prob_4 = [0.81818181818181818181818181818182, 0.18181818181818181818181818181818] # P(R|-c,-s,w)

# print(probability_true, probability_false)


###---------------------PART D---------------------###

# We want to write a function that will find the probability of C given no sprinker on or wet grass.
def mcmc(n_sample):
    #tempororay variables
    current_C = True
    current_R = True

    #keeps track anytime C is true
    C_true = 0
    C_false = 0

    for i in range(n_sample):
        #checks if number is odd or even, this gives a 50/50
        if i % 2 == 0:
            # if even, checks the current probability of R
            if current_R == True:
                current_prob_C_true = Prob_1[0] # gets True probability of P(C|-s,r)
            else:
                current_prob_C_true = Prob_2[0]# gets True probability of P(C|-s,-r)

            rando = random.random()
            current_C = (rando < current_prob_C_true) # returns True if random number is less than the current probability of C

        else:
            # if odd, checks the current probability of C
            if current_C == True:
                current_prob_R_true = Prob_3[0] # gets True probability of P(R|c,-s,w)
            else:
                current_prob_R_true = Prob_4[0] # gets True probability of P(R|-c,-s,w)

            rando = random.random()
            current_R = (rando < current_prob_R_true) # returns True if random number is less than the current probability of R

        # adds up all True instances of C
        if current_C == True:
            C_true += 1
        
        # along with the False
        else:
            C_false += 1

    probability_hat_true = C_true/n_sample
    probability_hat_false = 1.0 - probability_hat_true # or C_false/n_sample

    return probability_hat_true, probability_hat_false


def main():

    ###---------------------PART B---------------------###

    print("Part A. The sampling probabilities")
    print(f"P(C|-s,r) = <{Prob_1[0]:.4f}, {Prob_1[1]:.4f}>")
    print(f"P(C|-s,-r) = <{Prob_2[0]:.4f}, {Prob_2[1]:.4f}>")
    print(f"P(R|c,-s,w) = <{Prob_3[0]:.4f}, {Prob_3[1]:.4f}>")
    print(f"P(R|-c,-s,w) = <{Prob_4[0]:.4f}, {Prob_4[1]:.4f}>")


    ###---------------------PART C---------------------###

    # calculations for the matrix
    S1S1 = (0.5 * Prob_1[0]) + (0.5 * Prob_3[0])
    S1S2 = (0.5 * 0) + (0.5 * Prob_3[1])
    S1S3 = (0.5 * Prob_1[1]) + (0.5 * 0)
    S1S4 = 0

    S2S1 = (0.5 * 0) + (0.5 * Prob_3[0])
    S2S2 = (0.5 * Prob_2[0]) + (0.5 * Prob_3[1])
    S2S3 = 0
    S2S4 = (0.5 * Prob_2[1]) + (0.5 * 0)

    S3S1 = (0.5 * Prob_1[0]) + (0.5 * 0)
    S3S2 = 0
    S3S3 = (0.5 * Prob_1[1]) + (0.5 * Prob_4[0])
    S3S4 = (0.5 * 0) + (0.5 * Prob_4[1])

    S4S1 = 0
    S4S2 = (0.5 * Prob_2[0]) + (0.5 * 0)
    S4S3 = (0.5 * 0) + (0.5 * Prob_4[0])
    S4S4 = (0.5 * Prob_2[1]) + (0.5 * Prob_4[1])

    print("\nPart B. The transition probability matrix")
    print(f"{'S1'.rjust(10)}{'S2'.rjust(10)}{'S3'.rjust(10)}{'S4'.rjust(10)}")
    print(f"S1    {S1S1:.4f}    {S1S2:.4f}    {S1S3:.4f}    {S1S4:.4f}")
    print(f"S2    {S2S1:.4f}    {S2S2:.4f}    {S2S3:.4f}    {S2S4:.4f}")
    print(f"S3    {S3S1:.4f}    {S3S2:.4f}    {S3S3:.4f}    {S3S4:.4f}")
    print(f"S4    {S4S1:.4f}    {S4S2:.4f}    {S4S3:.4f}    {S4S4:.4f}")


    ###---------------------PART D---------------------###

    # sample points
    n_samples = [10**3, 10**4, 10**5, 10**6]

    print(f"\nPart C. The probability for the query P(C|-s,w)\nExact probability: <{probability_true:.4f}, {probability_false:.4f}>")
    j = 2
    for i in n_samples:
        j += 1
        probability_hat_true, probability_hat_false = mcmc(i)

        # error function
        error = abs((probability_true - probability_hat_true)/probability_true) * 100
        print(f"n = 10 ^ {j}: <{probability_hat_true:.4f}, {probability_hat_false:.4f}>, error = {error:.2f} %")   

main()