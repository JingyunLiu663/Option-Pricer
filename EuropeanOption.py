import numpy as np
import pandas as pd
from scipy.stats import norm
import csv
import matplotlib.pyplot as plt
import math

import datetime

d1 = datetime.date(2018, 7, 5)
d2 = datetime.date(2018, 1, 1)
print((d1 - d2).days)
print((int)('04'))

def Black_Schonles_Formulas_new(S, K, t, T, sigma, r, q, option_type):
    """
    S: spot price
    K: strike price
    t: initial time t = 0, dd/MM/yyyy
    T: time to maturity, dd/MM/yyyy
    r: risk-free interest rate
    q: dividend information and borrowing cost (and other related terms)
    sigma: standard deviation of price of underlying asset
    option_type: either call or put option
    """

    start = t.split('/')
    end = T.split('/')
    day1 = datetime.date((int)(start[2]), (int)(start[1]), (int)(start[0]))
    day2 = datetime.date((int)(end[2]), (int)(end[1]), (int)(end[0]))
    period = abs((int)((day1 - day2).days)) / 365

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * period) / (sigma * np.sqrt(period))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * period) / (sigma * np.sqrt(period))
    if option_type == "C":
        value = (S * np.exp(-q * period) * norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * period) * norm.cdf(d2, 0.0, 1.0))
    else:
        value = (K * np.exp(-r * period) * norm.cdf(-d2, 0.0, 1.0) - S * np.exp(-q * period) * norm.cdf(-d1, 0.0, 1.0))
    return value

def Black_Schonles_Formulas(S, K, t, T, sigma, r, option_type):
    """
    S: spot price
    K: strike price
    t: initial time t = 0
    T: time to maturity
    r: risk-free interest rate
    sigma: standard deviation of price of underlying asset
    option_type: put or call option
    """
    start = t.split('/')
    end = T.split('/')
    day1 = datetime.date((int)(start[2]), (int)(start[1]), (int)(start[0]))
    day2 = datetime.date((int)(end[2]), (int)(end[1]), (int)(end[0]))
    period = abs((int)((day1 - day2).days)) / 365
    print(period)

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * period) / (sigma * np.sqrt(period))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * (period)) / (sigma * np.sqrt(period))

    call = (S * norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * (period)) * norm.cdf(d2, 0.0, 1.0))
    put = (K * np.exp(-r * (period)) * norm.cdf(-d2, 0.0, 1.0) - S * norm.cdf(-d1, 0.0, 1.0))
    if option_type.lower == 'C':
        return call
    else:
        return put