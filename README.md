# py-grpcio-pg
A playground to practice creating gRPC microservices using Python

## Source Tutorial

The repository is based on the tutorial [Building a gRPC microservice using Python3 and TLS 1.3 authentication](https://faun.pub/building-a-grpc-microservice-using-python3-and-tls-1-3-authentication-acf8f9abb071) by @timusri on FAUN.

## Basic Setup

0. Install Python 3.4+
0. [optional] Install Pipenv and create a virtual environment.
0. Install dependencies `pip3 install -r requirements.txt`
0. `cd src`

### Running The Server

0. `python3 grpc_server.py`

The server should start on port 8000.

### Running The Client

0. `python3 grpc_client.py`
