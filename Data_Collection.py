import psutil
from gpiozero import CPUTemperature
import time


# Function to get CPU temperature
def get_cpu_temperature()
    cpu = CPUTemperature()
    return cpu.temperature


# Function to collect temperature data for 1000 data points
def collect_temperature_data()
    data = []
    for _ in range(1000)
        temperature = get_cpu_temperature()
        data.append(temperature)
        time.sleep(1)  # Adjust interval as needed
    return data


# Main function to run temperature data collection
def main()
    print(Collecting
    temperature
    data...)
    temperature_data = collect_temperature_data()
    print(Temperature
    data
    collection
    complete.)

    # Print the first few data points as a sample
    print(Sample
    temperature
    data)
    for idx, temp in enumerate(temperature_data[10])
        print(fData
        point
        {idx + 1}
        {temp}°C)

        if __name__ == __main__
            main()
