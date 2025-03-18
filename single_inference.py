import torch
import torch.nn as nn
import argparse
import time
from AlexNet import AlexNet  # Assuming the AlexNet class is in AlexNet.py

def run_inference(device_type="cpu", inference_type="edge"):
    """
    Run AlexNet inference either entirely on edge or entirely on cloud

    Args:
        device_type (str): "cpu"  for computation device
        inference_type (str): "edge" or "cloud" for logging purposes

    Returns:
        float: Inference latency in milliseconds
    """
    # Set the device
    device = torch.device(device_type)

    # Create AlexNet model
    model = AlexNet(input_channels=3, num_classes=1000)
    model.to(device)
    model.eval()  # Set to evaluation mode

    # Create a sample input (batch_size=1, channels=3, height=224, width=224)
    sample_input = torch.rand(1, 3, 224, 224).to(device)

    # Measure inference time
    start_time = time.time()

    # Disable gradient calculation for inference
    with torch.no_grad():
        output = model(sample_input)

    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000

    print(f"{inference_type.capitalize()}-only inference completed.")
    print(f"Device: {device_type}")
    print(f"Inference latency: {latency_ms:.3f} ms")

    return latency_ms

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run AlexNet inference on a single device")
    parser.add_argument("-d", "--device", type=str, choices=["cpu", "cuda"], default="cpu",
                        help="Device to run inference on (cpu or cuda)")
    parser.add_argument("-t", "--type", type=str, choices=["edge", "cloud"], default="edge",
                        help="Inference type for logging (edge or cloud)")

    args = parser.parse_args()

    run_inference(device_type=args.device, inference_type=args.type)