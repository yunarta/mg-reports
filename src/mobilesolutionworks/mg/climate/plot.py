from matplotlib import pyplot as plt

from .data import realtime_data, data_from_yesterday
from scipy.ndimage import uniform_filter1d


def _create_plots(times, temperatures, humidities, window_size=5):
    temperatures = uniform_filter1d(temperatures, size=window_size)
    humidities = uniform_filter1d(humidities, size=window_size)

    plt.figure(figsize=(15, 7.5), dpi=72)
    plt.plot(times, temperatures, marker="o", label="Temperature", color="red")
    plt.title("Temperature")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.ylim(20, 35)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("temperature.svg", dpi=72)

    plt.figure(figsize=(15, 7.5), dpi=72)
    plt.plot(times, humidities, marker="o", label="Humidity", color="blue")
    plt.title("Humidity")
    plt.xlabel("Time")
    plt.ylabel("Humidity (%)")
    plt.ylim(40, 100)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("humidity.svg", dpi=72)

def realtime():
    times, temperatures, humidities = realtime_data()
    _create_plots(times, temperatures, humidities)


def archive():
    times, temperatures, humidities = data_from_yesterday()
    _create_plots(times, temperatures, humidities)
