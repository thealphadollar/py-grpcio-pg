import grpc
import api_pb2
import api_pb2_grpc
import time
from grpc_server import PORT


def main(stub):
    request = api_pb2.ApiRequest(
        name="Shivam",
        message="Hey there!"
    )
    response = stub.ApiEndpoint(request)
    print(response)
    
if __name__=="__main__":
    with open('./server.crt', 'rb') as f:
        server_cert = f.read()
    creds = grpc.ssl_channel_credentials(server_cert)
    channel = grpc.secure_channel('localhost:8000', creds)
    stub = api_pb2_grpc.ApiStub(channel)
    main(stub)