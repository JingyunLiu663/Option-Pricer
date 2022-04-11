import numpy as np
from scipy.stats import norm
import geometric_asian_basket as geo


def arithmetic_asian_option(S, sigma, r, T, K, n, option_type, m=100000, control_method='arith', \
                            CI=0.95):
    '''
    The function is used to compute the price of an arithmatic asian option with Monte Carlo Simulation
    :param S: The spot price at time = 0, S(0)
    :param sigma: The true volatility
    :param r: The risk-free rate
    :param T: The time to maturity (in years)
    :param K: The strike price
    :param n: The number of observation times for the average spot price
    :param m:  The number of paths in the Monte Carlo simulation
    :param option_type: A character indicating the option type, 'C' for call option, 'T' for put option
    :param control_method: The control variate method (Default: 'arith' for arithmetic asian option with standard MC,
                                                        'geo' for geometric asian option with standard MC,
                                                        'control' for arithmetic asian MC with control variate)
    :param CI: The confidence level (1 - alpha), presented in float format, by default, CI=0.95
    :return: The 95% confidence interval (by default) of the option price
    '''
    # set the random seed to be 42 to reproduce the results
    global target
    np.random.seed(42)
    arithPayoff = []
    geoPayoff = []
    drift = np.exp((r - 0.5 * sigma ** 2) * T / n)
    for i in range(m):
        Spath = []
        growthFactor = drift * np.exp(sigma * np.sqrt(T / n) * np.random.standard_normal())
        Spath.append(S * growthFactor)
        for j in range(1, n):
            growthFactor = drift * np.exp(sigma * np.sqrt(T / n) * np.random.standard_normal())
            Spath.append(Spath[-1] * growthFactor)
        arithMean = np.mean(Spath)
        geoMean = np.exp(1.0 / n * sum(np.log(Spath)))
        if option_type == 'C':
            arithPayoff.append(np.exp(-r * T) * max(arithMean - K, 0))
            geoPayoff.append(np.exp(-r * T) * max(geoMean - K, 0))
        else:
            arithPayoff.append(np.exp(-r * T) * max(K - arithMean, 0))
            geoPayoff.append(np.exp(-r * T) * max(K - geoMean, 0))
    if control_method == 'geo':
        target = geoPayoff
    elif control_method == 'arith':
        target = arithPayoff
    elif control_method == 'control':
        geoExpected = geo.geometric_asian_option(S=S, sigma=sigma, r=r, T=T, K=K, n=n, option_type=option_type)
        theta = np.cov(arithPayoff, geoPayoff) / np.var(geoPayoff)
        target = []
        for i in range(len(arithPayoff)):
            target.append(arithPayoff[i] + theta * (geoExpected - geoPayoff[i]))
    target_mean = np.mean(target)
    target_std = np.std(target)
    ci_lower = target_mean - norm.ppf(1 - (1 - CI) / 2, loc=0, scale=1) * target_std / np.sqrt(m)
    ci_upper = target_mean + norm.ppf(1 - (1 - CI) / 2, loc=0, scale=1) * target_std / np.sqrt(m)
    return target_mean, ci_lower, ci_upper


