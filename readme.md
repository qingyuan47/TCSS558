# Cloud-Edge Collaborative Inference

This project implements a collaborative inference system that distributes deep neural network (DNN) computations between cloud and edge devices. By strategically partitioning neural networks, the system optimizes performance across different computing environments.

## Project Structure

# Cloud-Edge Collaborative Inference

This project implements a collaborative inference system that distributes deep neural network (DNN) computations between cloud and edge devices. By strategically partitioning neural networks, the system optimizes performance across different computing environments.

## Project Structure

```
Cloud-Edge Collaborative Inference
├── AlexNet.py                    # AlexNet model implementation
├── README.md                     # Project documentation
├── avgpool.pkl                   # Average pooling layer model
├── avgpool_lat.csv               # Average pooling latency data
├── batchnorm.pkl                 # Batch normalization layer model
├── batchnorm_lat.csv             # Batch normalization latency data
├── cloud_api.py                  # Cloud device entry point
├── conv.pkl                      # Convolution layer model
├── conv_lat.csv                  # Convolution latency data
├── deployment.py                 # Deployment phase
├── dw_conv.pkl                   # Depthwise convolution layer model
├── dw_conv_lat.csv               # Depthwise convolution latency data
├── edge_api.py                   # Edge device entry point
├── excel_utils.py                # Excel operations
├── get_datasets_func.py          # Dataset reading process
├── inference_utils.py            # Collaborative inference functionality
├── kernel_flops.py               # FLOPS calculation for kernels
├── linear.pkl                    # Linear layer model
├── linear_lat.csv                # Linear layer latency data
├── maxpool.pkl                   # Max pooling layer model
├── maxpool_lat.csv               # Max pooling latency data
├── monitor_client.py             # Bandwidth monitor client
├── monitor_server.py             # Bandwidth monitor server
├── monitor_test.py               # Bandwidth monitor test service
├── net_utils.py                  # Network utility functions
└── predictor_utils.py            # Predictor functionality
```

## Hardware Configuration

| Device Type | Hardware | CPU Environment | Memory | Storage | Operating System |
|-------------|----------|-----------------|--------|---------|------------------|
| Cloud       | Local PC | 6 cores, 12 processors | 16384MB RAM | 512GB SSD | Windows 11 Home 64-bit (10.0, build 22631) |
| Edge        | Ubuntu VM | 2 cores, 4 processors | 4096MB RAM | 20GB SSD | Ubuntu 16.04.7 LTS |

## Software Environment

| Software | Version |
|----------|---------|
| Python   | 3.9     |
| Anaconda3 | 4.13.0  |
| torch    | 1.9.0   |
| torchvision | 0.10.0 |
| xlrd     | 2.0.1   |
| xlwt     | 1.3.0   |
| pandas   | 1.3.4   |
| numpy    | 1.20.3  |
| apscheduler | 3.9.0 |
| scikit   | 1.3.0   |
| speedtest-cli | 2.1.3 |

## Overview

This project enables collaborative inference between cloud and edge devices:

1. The system dynamically decides how to partition DNN models between edge and cloud devices
2. Bandwidth monitoring tools track network conditions in real-time
3. The predictor module forecasts performance for different partitioning strategies
4. Various utility functions support visualization and data handling

The project includes various model and latency data files:
- Layer-specific models (*.pkl files): conv, dw_conv, linear, avgpool, maxpool, batchnorm
- Corresponding latency measurements (*.csv files): conv_lat, dw_conv_lat, linear_lat, avgpool_lat, maxpool_lat, batchnorm_lat

## Getting Started

### Prerequisites

- Make sure both cloud and edge environments match the specifications in the hardware and software tables above
- Install all required Python packages listed in the software environment table

### Setup

1. Clone the repository to both cloud and edge devices
2. Install dependencies:
   ```
   pip install torch==1.9.0 torchvision==0.10.0 pandas==1.3.4 numpy==1.20.3 apscheduler==3.9.0 scikit-learn==1.3.0 speedtest-cli==2.1.3 xlrd==2.0.1 xlwt==1.3.0
   ```

### Deployment

Run the deployment script to prepare the system:

```
python deployment.py
```

### Running the System

1. Start the cloud server:
   ```
   python cloud_api.py
   ```

2. Start the edge device:
   ```
   python edge_api.py
   ```

## Monitoring Network Conditions

The system includes tools to monitor bandwidth between cloud and edge devices:

1. Start the monitor server:
   ```
   python monitor_server.py
   ```

2. Start the monitor client:
   ```
   python monitor_client.py
   ```

3. Test bandwidth monitoring:
   ```
   python monitor_test.py
   ```

## DNN Models and Layer Analysis

The system supports AlexNet architecture with detailed analysis of different neural network layers:

- Convolutional layers (conv.pkl, conv_lat.csv)
- Depthwise convolutional layers (dw_conv.pkl, dw_conv_lat.csv)
- Linear/fully connected layers (linear.pkl, linear_lat.csv)
- Average pooling layers (avgpool.pkl, avgpool_lat.csv)
- Max pooling layers (maxpool.pkl, maxpool_lat.csv)
- Batch normalization layers (batchnorm.pkl, batchnorm_lat.csv)

The .pkl files contain trained models for predicting layer performance, while the .csv files contain latency measurements for each layer type.

## Contributors

[Your name/team members here]

## License

[Your license information here]
