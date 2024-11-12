# Wordlist Generator

A custom wordlist generator designed for penetration testing. This Python script allows you to generate password variations based on user input such as first name, last name, age, pet name, and more. It includes a variety of transformations like leetspeak, reverse strings, and more to generate a highly customized wordlist.

## Features

- Generate custom wordlists based on personal data (e.g., first name, last name, pet name, etc.).
- Include common password patterns and suffixes.
- Add user-specific known passwords and variations.
- Simple terminal-based animation and ASCII art.
- Allows the saving of wordlists to a file.

## Prerequisites

Before using the script, make sure your system has `Python 3` and `pip` installed. If not, please refer to the installation instructions below.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/unnideeraj/Custom_Wordlist_Generator.git
cd Custom_Wordlist_Generator
```
### 2. Run the installation script
The **`install.sh`** script will check if Python 3 is installed, install necessary Python dependencies, and optionally add the directory to your **`PATH`**.

```bash
bash install.sh
```
Or use
```bash
chmod +x install.sh
chmod +x setup.py
```
This will install the required dependencies:
- art
- pyfiglet
- itertools

**`Install.sh`** will install all the requirements and dependencies then proceed to installation of setup.
### 3. Run the program
After suuccessfull installation open terminal and run **`generate`** to run the script.

### 4. Manual installation if above automated script doesn't work.
#### 4.1. Make the script executable (if needed)
If you want to run the `**wordlist_generator.py**` script directly:
```bash
chmod +x wordlist_generator.py
```
#### 4.2. Install the package
To install the Python package locally:
```bash
pip install .
```
## Usage
After the installation, you can run the wordlist generator as follows:
```bash
generate
```

## If nothing works
you can directly run the python program each time by using **` python wordlist_generator.py `**.

Follow the prompts to input personal data (e.g., first name, last name, pet name, etc.). The script will generate a custom wordlist and save it to a specified file.

## Adding to PATH
If you want to run the script from anywhere on your system, you can add the directory to your **`PATH`**. The installation script will ask if you want to do this. Choose **`yes`** or **`no`** based on your preference.

## Manually add to PATH
If you want to manually add the script to your **`PATH`**, follow these steps:

Find the directory where **`wordlist_generator.py`** is located.
Add the directory to your **`PATH`** by modifying the **`.bashrc`**, **`.zshrc`**, or equivalent file depending on your shell:

```bash
export PATH=$PATH:/path/to/directory
```

## Note
This tool is intended for use in penetration testing and ethical hacking. Please use it responsibly and only on systems where you have permission to conduct security testing.

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- [art](https://pypi.org/project/art/) for ASCII art generation.
- [pyfiglet](https://pypi.org/project/pyfiglet/) for ASCII text generation.
- [itertools](https://docs.python.org/3/library/itertools.html) for generating combinations and permutations.

