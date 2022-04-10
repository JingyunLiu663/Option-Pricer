import numpy as np


def binomial_tree_american_option(S, sigma, r, T, K, N, option_type):
    '''
    The function is used to compute the price of an american option with a binomial tree
    :param S: The spot price at time = 0, S(0)
    :param sigma: The true volatility
    :param r: The risk-free rate
    :param T: The time to maturity (in years)
    :param K: The strike price
    :param N: The number of steps
    :param option_type: A character indicating the option type, 'C' for call option, 'T' for put option
    :return: The value of the call/put American Option with N steps
    '''
    t = T / N
    u = np.exp(sigma * np.sqrt(t))
    d = 1.0 / u
    p = (np.exp(r * t) - d) / (u - d)
    
    # stock tree can be represented using nodes(i, j) and initial stock price S_0
    # S_{i, j} = S_0 * (u ** j) * (d ** (i - j))

    # initialise stock prices at maturity
    S_T = S * d ** (np.arange(N, -1, -1)) * u ** (np.arange(0, N + 1, 1)) # length = N + 1
    # option payoff array
    if option_type == 'C':
        payoff = np.maximum(0, S_T - K)
    else:
        payoff = np.maximum(0, K - S_T)
    # recursion backwards
    for i in np.arange(N - 1, -1, -1):
        # S_t is the array for stock price at the i-th step
        S_t = S * d ** (np.arange(i, -1, -1)) * u ** (np.arange(0, i + 1, 1)) # length = i + 1
        payoff[0:i + 1] = np.exp(-r * t) * (p * payoff[1:i + 2] + (1 - p) * payoff[0: i + 1]) # length = i + 2
        payoff = payoff[:-1] # trim the payoff array to have the same length as the S_t array
        if option_type == 'C':
            payoff = np.maximum(payoff, S_t - K)
        else:
            payoff = np.maximum(payoff, K - S_t)
    return payoff[0]


