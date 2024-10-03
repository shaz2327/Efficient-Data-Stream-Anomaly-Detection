import numpy as np
import time

def data_stream_simulation(seasonal_period=50, noise_level=0.1, anomaly_rate=0.01):
    """
    Simulates a data stream with seasonal variations, noise, and occasional anomalies.
    
    Parameters:
    seasonal_period (int): Number of points to complete one cycle of the seasonal pattern.
    noise_level (float): Amplitude of random noise added to the data.
    anomaly_rate (float): Probability of an anomaly occurring at any data point.
    
    Yields:
    float: Next data point in the stream.
    """
    t = 0
    while True:
        # Generate seasonal pattern with random noise
        value = np.sin(2 * np.pi * (t % seasonal_period) / seasonal_period) + np.random.normal(0, noise_level)
        
        # Inject occasional anomalies
        if np.random.rand() < anomaly_rate:
            value += np.random.choice([5, -5])  # Inject a large deviation
        
        yield value
        t += 1
        time.sleep(0.1)  # Simulate delay between data points