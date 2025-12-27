# gRPC Python Example

This example demonstrates a simple gRPC client-server application based on the [official Python quickstart guide](https://grpc.io/docs/languages/python/quickstart/).

## Overview

The example implements a `Greeter` service with two RPC methods:
- `SayHello`: Returns a greeting message
- `SayHelloAgain`: Returns another greeting message

## Files

- `grpc_example.proto` - Protocol Buffer definition file
- `grpcio-example.py` - Complete client/server implementation

## Requirements

```bash
pip install grpcio grpcio-tools
```

## Setup

First, navigate to the python-examples directory and generate the gRPC Python code:

```bash
cd python-examples
python grpcio-example.py setup
```

This generates:
- `grpc_example_pb2.py` - Protocol buffer message classes
- `grpc_example_pb2_grpc.py` - gRPC service classes

Alternatively, you can manually generate with:

```bash
cd python-examples
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. grpc_example.proto
```

This generates:
- `grpc_example_pb2.py` - Protocol buffer message classes
- `grpc_example_pb2_grpc.py` - gRPC service classes

## Running the Example

### Terminal 1 - Start the server

```bash
cd python-examples
python grpcio-example.py server
```

Output:
```
✓ gRPC Server started on port 50051
  Waiting for client connections...
  Press Ctrl+C to stop
```

### Terminal 2 - Run the client

```bash
cd python-examples
python grpcio-example.py client
```

Output:
```
Connecting to gRPC server at localhost:50051...

1. Calling SayHello RPC...
   ✓ Client received: Hello, World!

2. Calling SayHelloAgain RPC...
   ✓ Client received: Hello again, gRPC User!

✓ All RPC calls completed successfully!
```

## Custom Port

Start server on a different port:
```bash
python grpcio-example.py server 50052
```

Connect client to custom port:
```bash
python grpcio-example.py client localhost 50052
```

## Usage

```
python grpcio-example.py setup                - Generate proto files
python grpcio-example.py server [port]        - Start server (default: 50051)
python grpcio-example.py client [host] [port] - Run client (default: localhost:50051)
```

## Notes

- This example uses **insecure channels** for simplicity
- In production, use secure channels with TLS/SSL certificates
- The server runs indefinitely until Ctrl+C is pressed
- Each client invocation makes two RPC calls and exits

## Learn More

- [gRPC Python Documentation](https://grpc.io/docs/languages/python/)
- [Protocol Buffers](https://protobuf.dev/)
- [gRPC Core Concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
