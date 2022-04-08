import numpy as np
import pandas as pd
from scipy.stats import norm
import csv
import matplotlib.pyplot as plt

import datetime

d1 = datetime.date(2018, 3, 20)
d2 = datetime.date(2018, 1, 7)
print((d1 - d2).days)

def Black_Schonles_Formulas_new(S, K, t, T, r, sigma, q, option_type):
    """
    S: spot price
    K: strike price
    t: initial time t = 0
    T: time to maturity
    r: risk-free interest rate
    q: dividend information and borrowing cost (and other related terms)
    sigma: standard deviation of price of underlying asset
    option_type: either call or put option
    """
    T = 24
    t = 16
    period = (T - t) / 365
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * period) / (sigma * np.sqrt(period))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * period) / (sigma * np.sqrt(period))
    value = 0
    if option_type.lower() == "c":
        value = (S * np.exp(-q * period) * norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * period) * norm.cdf(d2, 0.0, 1.0))
    else:
        value = (K * np.exp(-r * period) * norm.cdf(-d2, 0.0, 1.0) - S * np.exp(-q * period) * norm.cdf(-d1, 0.0, 1.0))
    return value