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
├── predictor_utils.py            # Predictor functionality
└── single_inference.py           # Single-device inference (edge-only or cloud-only)
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

## Running Instructions

### 1. Cloud-Edge Collaborative Inference:

On Cloud Device:
```
python cloud_api.py -i 10.0.0.130 -p 9999 -d cpu
```
Parameters:
- `-i`: IP address the server will listen on
- `-p`: Port number the server will listen on
- `-d`: Device to use for computation

On Edge Device:
```
python edge_api.py -i 10.0.0.130 -p 9999 -d cpu -t alex_net
```
Parameters:
- `-i`: IP address of the cloud server
- `-p`: Port number of the cloud server
- `-d`: Device to use for computation
- `-t`: Model type to use

### 2. Cloud-Only Inference:
For running inference entirely on the cloud:
```
python single_inference.py -d cpu -t cloud
```
Parameters:
- `-d`: Device type
- `-t`: Set to "cloud" for cloud-only inference

### 3. Edge-Only Inference:
For running inference entirely on the edge:
```
python single_inference.py -d cpu -t edge
```
Parameters:
- `-d`: Device type
- `-t`: Set to "edge" for edge-only inference