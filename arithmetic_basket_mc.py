import numpy as np
from scipy.stats import norm
import geometric_asian_basket as geo


def arithmetic_basket_option(S1, S2, sigma1, sigma2, rho, r, T, K, option_type, m=100000, control_method='arith', CI=0.95):
    '''
    The function is used to compute the price of an arithmatic basket option (of 2 assets) with Monte Carlo Simulation
    :param S1: The spot price of asset 1 at time = 0, S1(0)
    :param S2: The spot price of asset 2 at time = 0, S2(0)
    :param sigma1: The true volatility of asset 1
    :param sigma2: The true volatility of asset 2
    :param rho: The correlation coefficient of the two assets
    :param r: The risk-free rate
    :param T: The time to maturity (in years)
    :param K: The strike price
    :param option_type: A character indicating the option type, 'C' for call option, 'T' for put option
    :param m:  The number of paths in the Monte Carlo simulation
    :param control_method: The control variate method (Default: 'arith' for arithmetic asian option with standard MC,
                                                        'geo' for geometric asian option with standard MC,
                                                        'control' for arithmetic asian MC with control variate)
    :param CI: The confidence level (1 - alpha), presented in float format, by default, CI=0.95
    :return: The 95% confidence interval (by default) of the option price
    '''
    # set the random seed to be 42 to reproduce the results
    np.random.seed(42)
    arithPayoff = []
    geoPayoff = []
    for i in range(m):
        rand1 = np.random.standard_normal()
        rand2 = np.random.standard_normal()
        drift1 = np.exp((r - 0.5 * sigma1 ** 2) * T + sigma1 * np.sqrt(T) * rand1)
        # the correlation between the 2 assets has to be taken into consideration:
        drift2 = np.exp((r - 0.5 * sigma2 ** 2) * T + sigma2 * np.sqrt(T) * (rho * rand1 + np.sqrt(1 - rho ** 2) * rand2))
        basket = [S1 * drift1, S2 * drift2]
        arithMean = np.mean(basket)
        geoMean = np.exp(0.5 * sum(np.log(basket)))
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
        geoExpected = geo.geometric_basket_option(S1=S1, S2=S2, sigma1=sigma1, sigma2=sigma2, rho=rho, r=r, T=T, K=K, \
                                         option_type=option_type)
        theta = np.cov(arithPayoff, geoPayoff) / np.var(geoPayoff)
        target = []
        for i in range(len(arithPayoff)):
            target.append(arithPayoff[i] + theta * (geoExpected - geoPayoff[i]))
    target_mean = np.mean(target)
    target_std = np.std(target)
    ci_lower = target_mean - norm.ppf(1 - (1 - CI) / 2, loc=0, scale=1) * target_std / np.sqrt(m)
    ci_upper = target_mean + norm.ppf(1 - (1 - CI) / 2, loc=0, scale=1) * target_std / np.sqrt(m)
    return target_mean, ci_lower, ci_upper



