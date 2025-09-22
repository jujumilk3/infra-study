#!/bin/bash

# Install NGINX Ingress Controller for Kind
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

# Wait for Ingress Controller to be ready
echo "Waiting for Ingress Controller to be ready..."
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s

echo "NGINX Ingress Controller installed successfully!"
echo ""
echo "To access your application:"
echo "1. Add this line to /etc/hosts:"
echo "   127.0.0.1 mcp-server.local"
echo ""
echo "2. Apply the Kubernetes resources:"
echo "   kubectl apply -f kubernetes/"
echo ""
echo "3. Access the application at:"
echo "   http://mcp-server.local"
