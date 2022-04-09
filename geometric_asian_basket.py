import numpy as np
from scipy.stats import norm


def geometric_asian_option(S, sigma, r, T, K, n, option_type):
    '''
    The function is used to compute the price of a geometric asian option with the closed-form formula
    :param S: The spot price at time = 0, S(0)
    :param sigma: The true volatility
    :param r: The risk-free rate
    :param T: The time to maturity (in years)
    :param K: The strike price
    :param n: The number of observation times for the geometric average
    :param option_type: A character indicating the option type, 'C' for call option, 'T' for put option
    :return: The value of the call/put Geometric Asian Option
    '''
    sigmaSqT = T * sigma ** 2 * (n + 1) * (2 * n + 1) / (6 * n ** 2)
    muT = T* (r - 0.5 * sigma ** 2) * (n + 1) / (2 * n) + 0.5 * sigmaSqT

    d1 = (np.log(S / K)) + (muT + 0.5 * sigmaSqT) / np.sqrt(sigmaSqT)
    d2 = d1 - np.sqrt(sigmaSqT)

    if option_type == 'C':
        return np.exp(-r * T) * (S * np.exp(muT) * norm.cdf(d1, 0.0, 1.0) - K * norm.cdf(d2, 0.0, 1.0))
    else:
        return np.exp(-r * T) * (K * norm.cdf(-d2, 0.0, 1.0) - S * np.exp(muT) * norm.cdf(-d1, 0.0, 1.0))

def geometric_basket_option(S1, S2, sigma1, sigma2, rho, r, T, K, option_type):
    '''
    The function is used to compute the price of a geometric basket option (of 2 assets) with the closed-form formula
    :param S1: The spot price of asset 1 at time = 0, S1(0)
    :param S2: The spot price of asset 2 at time = 0, S2(0)
    :param sigma1: The true volatility of asset 1
    :param sigma2: The true volatility of asset 2
    :param rho: The correlation coefficient of the two assets
    :param r: The risk-free rate
    :param T: The time to maturity (in years)
    :param K: The strike price
    :param option_type: A character indicating the option type, 'C' for call option, 'T' for put option
    :return: The value of the call/put Geometric Basket Option
    '''
    B0 = (S1 * S2) ** 0.5
    sigmaB = np.sqrt(sigma1 ** 2 + 2 * sigma1 * sigma2 * rho + sigma2 ** 2) / 2
    muB = r - 0.5 * (sigma1 ** 2 + sigma2 ** 2) / 2 + 0.5 * sigmaB ** 2

    d1 = (np.log(B0 / K) + (muB + 0.5 * sigmaB ** 2) * T) / (sigmaB * np.sqrt(T))
    d2 = d1 - sigmaB * np.sqrt(T)

    if option_type == 'C':
        return np.exp(-r * T) * (B0 * np.exp(muB * T) * norm.cdf(d1, 0.0, 1.0) - K * norm.cdf(d2, 0.0, 1.0))
    else:
        return np.exp(-r * T) * (K * norm.cdf(-d2, 0.0, 1.0) - B0 * np.exp(muB * T) * norm.cdf(-d1, 0.0, 1.0))
