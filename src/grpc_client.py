import grpc

from consts import PORT, SERVER_CERT
from grpc_generated_files import api_pb2, api_pb2_grpc


def main(stub):
    request = api_pb2.ApiRequest(
        name="Shivam",
        message="Hey there!"
    )
    response = stub.ApiEndpoint(request)
    print(response)


if __name__ == "__main__":
    with open(SERVER_CERT, 'rb') as f:
        server_cert = f.read()
    creds = grpc.ssl_channel_credentials(server_cert)
    # the server IP should be in the common name of the certificate
    channel = grpc.secure_channel(f'localhost:{PORT}', creds)
    stub = api_pb2_grpc.ApiStub(channel)
    main(stub)
