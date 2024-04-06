Sure, I can break down the README content into step-by-step instructions. Here's how you can structure it:

---

# Raspberry Pi Temperature Forecasting with Support Vector Machines

## Introduction

As the Raspberry Pi finds its way into an increasing number of applications, ensuring its proper functioning becomes paramount. One critical aspect of maintaining optimal performance and longevity is monitoring its internal temperature. Due to its compact design and often intensive workloads, the Raspberry Pi is susceptible to overheating, which can lead to performance degradation, hardware damage, and even system failure. Therefore, real-time temperature monitoring is essential for preemptively detecting and mitigating potential issues.

## Project Overview

This project employs Support Vector Machines (SVM), a powerful supervised learning algorithm, for temperature prediction on Raspberry Pi devices. SVM offers the advantage of being able to handle both linear and non-linear data, making it suitable for our task. We experiment with four different kernels: Linear, Polynomial, Radial Basis Function (RBF), and Sigmoid, to accurately predict CPU temperature trends.

## Steps to Deploy and Use

### 1. Data Collection

- Install necessary Python libraries (`psutil`, `gpiozero`) for data collection.

### 2. Model Deployment

- Transfer trained SVM models to the Raspberry Pi for deployment.

### 3. Real-time Monitoring

- Run the provided Python script on the Raspberry Pi for real-time temperature prediction.

## Model Training

### 1. Data Preparation

- Prepare dataset including CPU temperature, CPU utilization, and memory usage metrics.

### 2. Model Training

- Train SVM models with different kernels using scikit-learn.

### 3. Model Evaluation

- Evaluate model performance using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.

## Results

The performance of SVM kernels:

| Kernel   | MAE      | MSE      | R-squared |
|----------|----------|----------|-----------|
| Linear   | 0.725384 | 0.927490 | 0.026445  |
| Poly     | 0.723916 | 0.930851 | 0.022917  |
| RBF      | 0.722619 | 0.932758 | 0.020916  |
| Sigmoid  | 0.756065 | 1.017065 | -0.067579 |

![Real and Predicted Temperature](temp3.jpg)

## Conclusion

Our project underscores the efficacy of SVM for real-time temperature forecasting on Raspberry Pi devices, offering a promising avenue for maintaining optimal device performance and preventing potential overheating-related issues.

## Contributors

- Yash Goyal   (yashgoyal01102003@gmail.com)
- Khush Pandya (khushpandya705@gmail.com)
- Archit Shah  (u21ec127@eced.svnit.ac.in)


Feel free to customize the content according to your project's specifics. Make sure to include any additional instructions or information that might be helpful for users.
