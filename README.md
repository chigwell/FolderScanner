[![PyPI version](https://badge.fury.io/py/FolderScanner.svg)](https://badge.fury.io/py/FolderScanner)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/FolderScanner)](https://pepy.tech/project/FolderScanner)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)


# FolderScanner

`FolderScanner` is a Python package that enables efficient scanning of directory structures, applying ignore rules similar to `.gitignore`, and chunking file contents for processing. It's designed to handle large datasets and is ideal for pre-processing tasks in data analysis or machine learning pipelines.

## Features

- Recursively scans specified directories.
- Applies ignore patterns to skip specified files and directories.
- Chunks file contents and yields them with their paths for efficient processing.

## Installation

To install `FolderScanner`, simply use pip:

```bash
pip install FolderScanner
```

## Usage

Import and use `FolderScanner` in your Python projects as follows:

```python
from folder_scanner import scan_directory

core_folder = '/path/to/your/projects'
ignore_patterns = ['.git', '.dockerignore', '*.log', 'tmp/*']

for file_chunk in scan_directory(core_folder, ignore_patterns):
    print(file_chunk)
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest features on the [GitHub issues page](https://github.com/chigwell/FolderScanner/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

