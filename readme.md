# My Exe Embedder

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/your-username/my-exe-embedder/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/your-username/my-exe-embedder)](https://github.com/your-username/my-exe-embedder/issues)
[![GitHub stars](https://img.shields.io/github/stars/your-username/my-exe-embedder)](https://github.com/your-username/my-exe-embedder/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/your-username/my-exe-embedder)](https://github.com/your-username/my-exe-embedder/network)

My Exe Embedder is a lightweight tool designed to embed data and files securely into various types of files, including images, videos, executables, and more. This can be particularly useful for protecting your data from viruses, malware, and unwanted visibility.

## Features

- **Secure Embedding**: Data and files can be securely embedded in images, videos, executables, and more.
- **Protection**: Protect your data from viruses, malware, and unwanted visibility.
- **Customizable**: Customize your embedding process with various options.

## Installation

You can download the latest version of My Exe Embedder from the [releases page](https://github.com/your-username/my-exe-embedder/releases). Simply download the appropriate binary for your platform and place it in your PATH.

## Usage
### Embed Single File
python handle.py -m 0 -t target_file_name -f Source_File_Name -v wrtie_unqiue_code

## Embed Complete Dir With Files And Folder
python handle.py -m 2 -t target_file_name -d dir_name -n dir_name  -v write_unqiue_code

Alternatively, you can compile My Exe Embedder from source:

```bash
git clone https://github.com/your-username/my-exe-embedder.git
cd my-exe-embedder
make
