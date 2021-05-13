import os
import time
from concurrent import futures

import grpc

from consts import PORT, SERVER_CERT, SERVER_PRIVATE_KEY
from grpc_generated_files import api_pb2, api_pb2_grpc


class ChatBox(api_pb2_grpc.ApiServicer):
    
    def ApiEndpoint(self, request, context):
        response = api_pb2.ApiResponse()
        response.response = f"Hi, your name is {request.name} and your message is {request.message}"
        return response
    
if __name__=="__main__":
    # creating the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=os.cpu_count()))
    with open(SERVER_PRIVATE_KEY, 'rb') as f:
        private_key = f.read()
    with open(SERVER_CERT, 'rb') as f:
        certificate = f.read()
    server_creds = grpc.ssl_server_credentials(
        ((private_key, certificate), )
    )
    
    # add the chatbox servicer to the server
    api_pb2_grpc.add_ApiServicer_to_server(ChatBox(), server=server)
    
    # listen
    server.add_secure_port(f'0.0.0.0:{PORT}', server_creds)
    server.start()
    print(f"listening on {PORT}")
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop()
