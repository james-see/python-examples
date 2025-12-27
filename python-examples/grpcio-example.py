#!/usr/bin/env python3
"""
gRPC Python Example
Based on: https://grpc.io/docs/languages/python/quickstart/

This example demonstrates a simple gRPC client-server application using
the Greeter service from the official gRPC Python quickstart.

Requirements:
    pip install grpcio grpcio-tools

Setup:
    Before running, generate the gRPC Python code from the proto file:
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. python-examples/grpc_example.proto

To run:
    1. Start the server: python grpcio-example.py server
    2. In another terminal, run the client: python grpcio-example.py client

Note: This example uses insecure channels for simplicity. In production,
use secure channels with TLS/SSL certificates.
"""

import sys
import os
import grpc
from concurrent import futures
import time
import subprocess

# Check if proto files are generated, if not, generate them
if not os.path.exists('python-examples/grpc_example_pb2.py'):
    print("Generating gRPC Python code from proto file...")
    try:
        subprocess.run([
            sys.executable, '-m', 'grpc_tools.protoc',
            '-I.', '--python_out=.', '--grpc_python_out=.',
            'python-examples/grpc_example.proto'
        ], check=True)
        print("Generated successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Error generating proto files: {e}")
        print("Make sure grpcio-tools is installed: pip install grpcio-tools")
        sys.exit(1)

# Import generated proto classes
try:
    from python-examples import grpc_example_pb2
    from python-examples import grpc_example_pb2_grpc
except ImportError:
    # Try alternative import path
    try:
        sys.path.insert(0, 'python-examples')
        import grpc_example_pb2
        import grpc_example_pb2_grpc
    except ImportError:
        print("Error: Failed to import generated gRPC modules.")
        print("Please ensure the proto files are generated correctly.")
        sys.exit(1)


# Server implementation
class Greeter(grpc_example_pb2_grpc.GreeterServicer):
    """Implementation of the Greeter service."""
    
    def SayHello(self, request, context):
        """Responds to a HelloRequest with a HelloReply."""
        print(f"Server received: {request.name}")
        return grpc_example_pb2.HelloReply(message=f"Hello, {request.name}!")
    
    def SayHelloAgain(self, request, context):
        """Another greeting method."""
        print(f"Server received again: {request.name}")
        return grpc_example_pb2.HelloReply(message=f"Hello again, {request.name}!")


def serve(port=50051):
    """Start the gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_example_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"✓ gRPC Server started on port {port}")
    print("  Waiting for client connections...")
    print("  Press Ctrl+C to stop\n")
    
    try:
        while True:
            time.sleep(86400)  # One day
    except KeyboardInterrupt:
        print("\n\nShutting down server...")
        server.stop(0)
        print("Server stopped.")


def run_client(host='localhost', port=50051):
    """Run the gRPC client."""
    print(f"Connecting to gRPC server at {host}:{port}...")
    
    # Create a channel
    with grpc.insecure_channel(f'{host}:{port}') as channel:
        # Create a stub (client)
        stub = grpc_example_pb2_grpc.GreeterStub(channel)
        
        # Make a call to SayHello
        try:
            print("\n1. Calling SayHello RPC...")
            response = stub.SayHello(grpc_example_pb2.HelloRequest(name='World'))
            print(f"   ✓ Client received: {response.message}")
            
            # Make another call to SayHelloAgain
            print("\n2. Calling SayHelloAgain RPC...")
            response = stub.SayHelloAgain(grpc_example_pb2.HelloRequest(name='gRPC User'))
            print(f"   ✓ Client received: {response.message}")
            
            print("\n✓ All RPC calls completed successfully!\n")
            
        except grpc.RpcError as e:
            print(f"\n✗ RPC failed: {e.code()} - {e.details()}\n")
            print("  Make sure the server is running: python grpcio-example.py server")
            sys.exit(1)


def print_usage():
    """Print usage instructions."""
    print("""
gRPC Python Example
===================

This demonstrates a basic gRPC client-server application based on the
official Python quickstart guide.

Setup (first time only):
    Generate the gRPC Python code from the proto file:
    
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. python-examples/grpc_example.proto

Usage:
    python grpcio-example.py setup          - Generate proto files
    python grpcio-example.py server [port]  - Start the gRPC server (default: 50051)
    python grpcio-example.py client [host] [port]  - Run the gRPC client

Examples:
    # Setup (only needed once)
    python grpcio-example.py setup
    
    # Start server on default port
    python grpcio-example.py server
    
    # Start server on custom port
    python grpcio-example.py server 50052
    
    # Run client (connect to localhost:50051)
    python grpcio-example.py client
    
    # Run client with custom host/port
    python grpcio-example.py client localhost 50052

Demo:
    Terminal 1: python grpcio-example.py server
    Terminal 2: python grpcio-example.py client
""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'setup':
        print("Generating gRPC Python code from proto file...")
        try:
            subprocess.run([
                sys.executable, '-m', 'grpc_tools.protoc',
                '-I.', '--python_out=.', '--grpc_python_out=.',
                'python-examples/grpc_example.proto'
            ], check=True)
            print("✓ Generated successfully!")
            print("\nYou can now run:")
            print("  python grpcio-example.py server")
            print("  python grpcio-example.py client")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error generating proto files: {e}")
            sys.exit(1)
    elif command == 'server':
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 50051
        serve(port)
    elif command == 'client':
        host = sys.argv[2] if len(sys.argv) > 2 else 'localhost'
        port = int(sys.argv[3]) if len(sys.argv) > 3 else 50051
        run_client(host, port)
    else:
        print(f"Unknown command: {command}")
        print_usage()
        sys.exit(1)
