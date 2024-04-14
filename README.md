# LogfileLVP

![License](https://img.shields.io/badge/License-GPL--3.0-orange.svg) ![Python](https://img.shields.io/badge/Python-v3.12-22558a.svg?logo=python&color=22558a) ![GSEWidgets](https://img.shields.io/badge/GSEWidgets-v0.0.2-teal.svg)

A GUI software for creating experiment run folders and logs.

------------
## Table of Contents

- [Installation](#installation)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

------------
## Installation
There are three ways to install LogfileLVP: by downloading the latest release from GitHub or by setting up the project from source.

### Downloading the Latest Release
To download the latest release: 

```bash
Go to the [releases](https://github.com/GSECARS/LogfileLVP/releases) page of the LogfileLVP repository.  
Download the latest .exe file.  
Run the installer and follow the on-screen instructions.
```

### Setting Up From Source
To use the project from source, follow these steps:

```bash
git clone -b main https://github.com/GSECARS/LogfileLVP.git && cd LogfileLVP
pip install -r requirements.txt
python LogfileLVP.py
```

## Development
To set up the project for development, just clone the repository, install all the requirements, the project and the pre-commit hooks.

```bash
git clone -b main https://github.com/GSECARS/LogfileLVP/git && cd LogfileLVP
pip install -r requirements.txt && pip install -r requirements_dev.txt
pip install -e .
pre-commit install
```

> Pre-commit is a tool that checks your code for any errors before you commit it. It helps maintain the quality of the codebase and reduces the chance of pushing faulty code. When you try to commit your changes, pre-commit will run checks defined in the [.pre-commit-config.yaml](.pre-commit-config.yaml) file. If any of these checks fail, the commit will be aborted.

## Contributing

All contributions to LogfileLVP are welcome! Here are some ways you can help:
- Report a bug by opening an [issue](https://github.com/GSECARS/LogfileLVP/issues).
- Add new features, fix bugs or improve documentation by submitting a [pull request](https://github.com/GSECARS/LogfileLVP/pulls).

Please adhere to the [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow) model when making your contributions! This means creating a new branch for each feature or bug fix, and submitting your changes as a pull request against the main branch. If you're not sure how to contribute, please open an issue and we'll be happy to help you out.

By contributing to LogfileLVP, you agree that your contributions will be licensed under the GNU General Public License Version 3.

[back to top](#table-of-contents)

------------
## License

LogfileLVP is distributed under the GNU General Public License Version 3. You should have received a [copy](LICENSE) of the GNU General Public License Version 3 along with this program. If not, see https://www.gnu.org/licenses/gpl-3.0.html for additional details.