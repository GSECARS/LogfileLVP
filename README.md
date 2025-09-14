# LogfileLVP

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A GUI software for creating experiment run folders, viewing live plots of EPICS PVs and collecting EPIC PV logs.

## 📋 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [📖 Usage](#-usage)
- [🛠️ Development](#️-development)
- [👥 Contributing](#-contributing)
- [📄 License](#-license)

## 🚀 Quick Start

### Installation using Anaconda/Miniconda environment
1. **Prerequisites**: Ensure [Anaconda/Miniconda](https://docs.conda.io/en/latest/miniconda.html) is installed

2. **Create Environment**:
   ```bash
   conda create -n logfilelvpENV python=3.13
   conda activate logfilelvpENV
   ```

3. **Install LogfileLVP**:
   ```bash
   pip install logfilelvp
   ```

4. **Verify Installation**:
   ```bash
   logfilelvp --help
   ```

### Installation from source
To use the project from source, follow these steps:

```bash
git clone -b main https://github.com/GSECARS/LogfileLVP.git && cd LogfileLVP
pip install -e .
logfilelvp --help
```

## 📖 Usage

### Command Line Interface

After installation, LogfileLVP provides a unified `logfilelvp` command with multiple modes:

```bash
# Show all available commands
logfilelvp --help

# Create desktop icon
logfilelvp --make-icon help
```

### GUI
```bash
logfilelvp --gui
# or short form:
logfilelvp -g
```

## 🛠️ Development
To set up the project for development, just clone the repository, install all the requirements, the project and the pre-commit hooks.

```bash
git clone -b development https://github.com/GSECARS/LogfileLVP/git && cd LogfileLVP
pip install -e ".[dev]"
pre-commit install
```

> Pre-commit is a tool that checks your code for any errors before you commit it. It helps maintain the quality of the codebase and reduces the chance of pushing faulty code. When you try to commit your changes, pre-commit will run checks defined in the [.pre-commit-config.yaml](.pre-commit-config.yaml) file. If any of these checks fail, the commit will be aborted.

## 👥 Contributing

All contributions to LogfileLVP are welcome! Here are some ways you can help:
- Report a bug by opening an [issue](https://github.com/GSECARS/LogfileLVP/issues).
- Add new features, fix bugs or improve documentation by submitting a [pull request](https://github.com/GSECARS/LogfileLVP/pulls).

Please adhere to the [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow) model when making your contributions! This means creating a new branch for each feature or bug fix, and submitting your changes as a pull request against the main branch. If you're not sure how to contribute, please open an issue and we'll be happy to help you out.

By contributing to LogfileLVP, you agree that your contributions will be licensed under the MIT License.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.