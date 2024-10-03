from collections import deque
import numpy as np

def z_score_anomaly_detection(data_point, window, threshold=1.8):
    """
    Detects anomalies based on the Z-Score method.
    
    Parameters:
    data_point (float): Incoming data point.
    window (deque): A moving window storing the recent data points.
    threshold (float): Z-Score threshold to flag anomalies.
    
    Returns:
    bool: True if an anomaly is detected, False otherwise.
    """
    # Append data point to the window
    if len(window) < window.maxlen:
        window.append(data_point)
        return False
    
    mean = np.mean(window)
    std_dev = np.std(window)
    
    if std_dev == 0:
        return False  # Avoid division by zero
    
    z_score = (data_point - mean) / std_dev
    window.append(data_point)  # Append after calculation to maintain window
    
    # Return True if the z-score exceeds the threshold
    return abs(z_score) > threshold
