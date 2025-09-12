# Sample MCP Server

A simple MCP (Model Context Protocol) server implementation with Docker and Kubernetes support.

## Docker Build

```bash
# Build Docker image
docker build -t mcp-server:latest .

# Run with Docker
docker run -p 8000:8000 -e MCP_SERVER_MODE=streamable-http mcp-server:latest
```

## Kind commands

```bash
# Create a Kind cluster with the specified configuration
kind create cluster --config=./kind-export-mapping-cluster-config.yaml --name kind-local

# Load Docker image into Kind cluster
kind load docker-image mcp-server:latest --name kind-local
```
