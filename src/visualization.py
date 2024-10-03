import matplotlib.pyplot as plt
from collections import deque
from anomaly_detection import z_score_anomaly_detection

def real_time_plot(data_stream, window_size=50, threshold=3):
    """
    Visualizes the data stream and highlights anomalies in real-time.
    
    Parameters:
    data_stream (generator): The data stream simulation function.
    window_size (int): Size of the moving window for anomaly detection.
    threshold (float): Z-Score threshold for anomaly detection.
    """
    plt.ion()
    fig, ax = plt.subplots()
    
    window = deque(maxlen=window_size)
    x_data, y_data = [], []
    anomaly_x, anomaly_y = [], []
    
    for t, data_point in enumerate(data_stream):
        # Check for anomalies
        is_anomaly = z_score_anomaly_detection(data_point, window, threshold)
        
        # Append data points for plotting
        x_data.append(t)
        y_data.append(data_point)
        
        if is_anomaly:
            anomaly_x.append(t)
            anomaly_y.append(data_point)
        
        # Update the plot
        ax.clear()
        ax.plot(x_data, y_data, label="Data Stream")
        ax.scatter(anomaly_x, anomaly_y, color='r', label="Anomaly", zorder=5)
        ax.legend()
        plt.draw()
        plt.pause(0.01)
        
        # Limit data displayed to avoid overcrowding
        if len(x_data) > 500:
            x_data.pop(0)
            y_data.pop(0)
