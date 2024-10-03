from data_stream_sim import data_stream_simulation
from visualization import real_time_plot

if __name__ == "__main__":
    # Create a data stream generator
    stream = data_stream_simulation(seasonal_period=50, noise_level=0.1, anomaly_rate=0.01)
    
    # Start the real-time plot
    real_time_plot(stream, window_size=50, threshold=3)