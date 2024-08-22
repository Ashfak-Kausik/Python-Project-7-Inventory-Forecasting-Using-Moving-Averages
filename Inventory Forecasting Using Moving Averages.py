import numpy as np
import matplotlib.pyplot as plt

def simple_moving_average(data, period):
    return np.convolve(data, np.ones(period)/period, mode='valid')

def exponential_moving_average(data, alpha):
    ema = [data[0]]
    for price in data[1:]:
        ema.append(ema[-1] * (1 - alpha) + price * alpha)
    return ema

# Example demand data
demand = [150, 200, 170, 220, 180, 210, 190, 230, 210, 250]

# Calculate moving averages
sma = simple_moving_average(demand, 3)
ema = exponential_moving_average(demand, 0.3)

# Plotting the results
plt.plot(demand, label='Actual Demand')
plt.plot(range(2, len(sma)+2), sma, label='SMA (3)')
plt.plot(ema, label='EMA (0.3)')
plt.legend()
plt.title('Inventory Forecasting')
plt.xlabel('Time Period')
plt.ylabel('Demand')
plt.show()
