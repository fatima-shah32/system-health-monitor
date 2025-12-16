# Linux System Health Monitoring Tool

## Description
Python automation script to monitor system health on CentOS Linux.

## Features
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Log generation

## Technologies
- Python
- CentOS Linux
- psutil
- Git

## How to Run
pip3 install -r requirements.txt
python3 monitor.py

## Docker Usage

Build image:
docker build -t system-health-monitor .

Run container:
docker run -v $(pwd):/app system-health-monitor

Push to Docker Hub:
docker tag system-health-monitor:latest <username>/system-health-monitor:1.0
docker push <username>/system-health-monitor:1.0
