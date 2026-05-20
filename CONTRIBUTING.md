# 🤝 Contributing to Omnikit

First off, thank you for considering contributing to Omnikit! It's people like you that make Omnikit such a great tool.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Commit Messages](#commit-messages)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## 🎯 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if possible**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List some examples of how it would be used**

### Adding New Tools

Want to add a new security tool? Great! Please follow these guidelines:

1. **Check if the tool already exists** in the toolkit
2. **Ensure the tool is legal and ethical** to use
3. **Add proper documentation** for the tool
4. **Include error handling** and user-friendly messages
5. **Test thoroughly** on multiple platforms if possible

## 🛠️ Development Setup

1. **Fork the repository**

```bash
git clone https://github.com/YOUR-USERNAME/omnikit.git
cd omnikit
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a new branch**

```bash
git checkout -b feature/your-feature-name
```

## 🔄 Pull Request Process

1. **Update the README.md** with details of changes if applicable
2. **Update the documentation** in the `docs/` folder
3. **Follow the coding standards** outlined below
4. **Test your changes** thoroughly
5. **Update the version number** in `surum.txt` if applicable
6. **Create a Pull Request** with a clear title and description

### Pull Request Template

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe the tests you ran and how to reproduce them

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have tested on multiple platforms (if applicable)
```

## 💻 Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 120 characters
- Use meaningful variable and function names
- Add docstrings to functions and classes

### Example

```python
def scan_port(target_ip, port_number):
    """
    Scan a specific port on the target IP address.
    
    Args:
        target_ip (str): The IP address to scan
        port_number (int): The port number to check
        
    Returns:
        bool: True if port is open, False otherwise
    """
    try:
        # Implementation here
        pass
    except Exception as e:
        print(f"Error scanning port: {e}")
        return False
```

### File Organization

- Place main source files in `src/`
- Place tool modules in `tools/`
- Place documentation in `docs/`
- Place assets (images, etc.) in `assets/`

## 📝 Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```
feat(network): add advanced port scanning feature

Added support for UDP port scanning and service detection.
Includes timeout configuration and verbose output mode.

Closes #123
```

```
fix(brute-force): resolve SSH connection timeout issue

Fixed timeout handling in SSH brute force module.
Now properly handles connection timeouts and retries.

Fixes #456
```

## 🧪 Testing

Before submitting a PR, please test your changes:

1. **Run the main program** and verify it starts correctly
2. **Test your specific feature** thoroughly
3. **Test on different platforms** if possible (Linux, Windows)
4. **Check for any error messages** or warnings

## 📚 Documentation

- Update README.md if you add new features
- Add comments to complex code sections
- Update docs/ folder with detailed documentation
- Include usage examples for new tools

## 🎨 ASCII Art Guidelines

If adding new ASCII art:

- Keep it clean and professional
- Test on different terminal sizes
- Ensure it displays correctly on Windows and Linux
- Use box-drawing characters (╔═╗║╚╝) for consistency

## ❓ Questions?

Feel free to:

- Open an issue for questions
- Join our [Telegram channel](https://t.me/omnikit)
- Contact us on [Discord](https://discord.com/invite/DTN5RSvYvw)

## 🙏 Thank You!

Your contributions make Omnikit better for everyone. We appreciate your time and effort!

---

**Happy Coding! 🚀**
