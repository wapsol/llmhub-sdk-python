# Contributing to LLMHub Python SDK

Thank you for your interest in contributing to the LLMHub Python SDK!

## Development Setup

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed development environment setup.

## How to Contribute

### Reporting Issues

- Check existing issues before creating a new one
- Use the issue templates when available
- Provide clear reproduction steps for bugs
- Include Python version and SDK version

### Suggesting Features

- Open an issue with the "enhancement" label
- Describe the use case and expected behavior
- Consider backward compatibility

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Run linting (`black . && isort . && flake8`)
6. Commit your changes (follow commit conventions below)
7. Push to your fork
8. Open a Pull Request

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use Black for code formatting (line length: 100)
- Use isort for import sorting
- Use type hints for all functions
- Write docstrings for public APIs

### Testing

- Write tests for new features
- Maintain test coverage ≥80%
- Use pytest for testing
- Include both unit and integration tests

### Documentation

- Update README.md if adding new features
- Add docstrings to all public methods
- Include examples in docstrings

## Commit Message Convention

Follow conventional commits:

```
feat: add new text generation parameter
fix: correct error handling in embeddings
docs: update README with new examples
test: add tests for document operations
chore: update dependencies
```

## Code Review Process

- All PRs require review before merging
- Address review comments promptly
- Keep PRs focused and small when possible
- Update PR description if scope changes

## Community Guidelines

- Be respectful and inclusive
- Help others in issues and discussions
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md)

## Questions?

- Open a GitHub issue with the "question" label
- Check existing documentation
- Refer to the main LLMHub project: https://github.com/wapsol/llmhub

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
