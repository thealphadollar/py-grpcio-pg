import grpc
from concurrent import futures
import time
import api_pb2 as api_pb2
import api_pb2_grpc as api_pb2_grpc
import os

PORT = 8000


class ChatBox(api_pb2_grpc.ApiServicer):
    
    def ApiEndpoint(self, request, context):
        response = api_pb2.ApiResponse()
        response.response = f"Hi, your name is {request.name} and your message is {request.message}"
        return response
    
if __name__=="__main__":
    # creating the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=os.cpu_count()))
    with open('./server.key', 'rb') as f:
        private_key = f.read()
    with open('./server.crt', 'rb') as f:
        certificate = f.read()
    server_creds = grpc.ssl_server_credentials(
        ((private_key, certificate), )
    )
    
    # add the chatbox servicer to the server
    api_pb2_grpc.add_ApiServicer_to_server(ChatBox(), server=server)
    
    # listen
    print(f"Starting to listen on {PORT}")
    server.add_secure_port(f'0.0.0.0:{PORT}', server_creds)
    server.start()
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop()
