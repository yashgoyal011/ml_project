import psutil
from gpiozero import CPUTemperature
import pickle
import pandas as pd

# Load SVM models trained with different kernels
svm_models = {}
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
for kernel in kernels:
    with open(f'svr_model_{kernel}.pkl', 'rb') as f:
        svm_models[kernel] = pickle.load(f)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def get_cpu_temperature():
    cpu = CPUTemperature()
    return cpu.temperature

# Collect data for CPU and memory usage
data = []
for _ in range(1):
    cpu_usage = get_cpu_usage()
    mem_usage = get_memory_usage()
    data.append([cpu_usage, mem_usage])

# Predict temperature for each SVM model
for kernel, model in svm_models.items():
    print(f'Predictions for {kernel} kernel:')
    for idx, sample_data in enumerate(data):
        temperature_prediction = model.predict([sample_data])
        cpu_temp = get_cpu_temperature()
        print(f'Sample {idx+1}: CPU Temp: {cpu_temp}°C,
        Temperature prediction: {temperature_prediction[0]}°C')
\end{verbatim}
