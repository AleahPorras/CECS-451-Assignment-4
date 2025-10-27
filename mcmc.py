import sorobn as hh
import pandas as pd


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
    (True, False, True): 0.9, (True, False, False): 0.1,
    (False, True, True): 0.95, (False, True, False): 0.05,
    (False, False, True): 0.05, (False, False, False): 0.95
})

bn.prepare()
probability = bn.query('C',  event = {'S': False, 'W': True})
print(probability)

# We want to write a function that will find the probability of C given no sprinker on or wet grass.
def mcmc(n):
    #tempororay variables
    temp_C = True
    temp_R = True

    current_C = None
    current_R = None


    pass

def main():
    Prob_1 = [0.87804, 0.12195]
    Prob_2 = [0.31035, 0.68965]
    Prob_3 = [0.98630, 0.01369]
    Prob_4 = [0.81818, 0.18182]

    print("Part A. The sampling probabilities")
    print(f"P(C|-s,r) = <{Prob_1[0]:.4f}, {Prob_1[1]:.4f}>")
    print(f"P(C|-s,-r) = <{Prob_2[0]:.4f}, {Prob_2[1]:.4f}>")
    print(f"P(R|c,-s,w) = <{Prob_3[0]:.4f}, {Prob_3[1]:.4f}>")
    print(f"P(R|-c,-s,w) = <{Prob_4[0]:.4f}, {Prob_4[1]:.4f}>")

    S1S1 = 0.9322
    S1S2 = 0.0069
    S1S3 = 0.0610
    S1S4 = 0
    S2S1 = 0.4932
    S2S2 = 0.1620
    S2S3 = 0
    S2S4 = 0.3449
    S3S1 = 0.4390
    S3S2 = 0
    S3S3 = 0.4701
    S3S4 = 0.0909
    S4S1 = 0
    S4S2 = 0.1552
    S4S3 = 0.4091
    S4S4 = 0.4358

    print("\nPart B. The transition probability matrix")
    print(f"{'S1'.rjust(10)}{'S2'.rjust(10)}{'S3'.rjust(10)}{'S4'.rjust(10)}")
    print(f"S1 {str(S1S1).rjust(9)}{str(S1S2).rjust(10)}{str(S1S3).rjust(10)}{str(S1S4).rjust(8)}")
    print(f"S2 {str(S2S1).rjust(9)}{str(S2S2).rjust(10)}{str(S2S3).rjust(8)}{str(S2S4).rjust(13)}")
    print(f"S3 {str(S3S1).rjust(9)}{str(S3S2).rjust(8)}{str(S3S3).rjust(13)}{str(S3S4).rjust(10)}")
    print(f"S1 {str(S4S1).rjust(7)}{str(S4S2).rjust(13)}{str(S4S3).rjust(10)}{str(S4S4).rjust(10)}")

    print("\nPart C. The probability for the query P(C|-s,w)")
    # for i in n_power:
    #     print(f"n = 10 ^ {i}: <{...}, {...}>, error = {...} %")   

main()