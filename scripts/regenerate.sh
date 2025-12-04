#!/bin/bash
set -e

echo "Regenerating client from OpenAPI spec..."
openapi-generator-cli generate \
  -i openapi-spec.yaml \
  -c openapi-config.yaml \
  -o generated/

echo "Formatting generated code..."
black generated/ || true
isort generated/ || true

echo "✓ Regeneration complete"
