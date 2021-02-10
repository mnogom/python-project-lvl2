# Difference Generator

---
### Hexlet tests and linter status:
[![Actions Status](https://github.com/mnogom/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/mnogom/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ae478a78f3f8b00d995c/maintainability)](https://codeclimate.com/github/mnogom/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ae478a78f3f8b00d995c/test_coverage)](https://codeclimate.com/github/mnogom/python-project-lvl2/test_coverage)

---
### Usage
1. From command line
```commandline
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

2. From python
```python
import gendiff

style = "plain"  # ["stylish (default)" | "plain" | "json"]
output = gendiff.generate_diff("path/to/file1", "path/to/file2", style)
```

---
### Features
1. Works with ***JSON*** and ***YAML*** format
2. Works with ***Plain*** and ***Recursive*** file structures
3. Output in ***Stylish***, ***Plain*** and ***JSON*** formats

*See examples below*

---
#### Plain JSON @ Stylish format
[![asciicast](https://asciinema.org/a/C2l9MVxQheGPdzy9pUaQSELit.svg?)](https://asciinema.org/a/C2l9MVxQheGPdzy9pUaQSELit)

#### Plain YAML @ Stylish format
[![asciicast](https://asciinema.org/a/ntkiU0MkQgkmFAQYbiVpntgCG.svg?)](https://asciinema.org/a/ntkiU0MkQgkmFAQYbiVpntgCG)

#### Recursive JSON @ Stylish format
[![asciicast](https://asciinema.org/a/kivjrbRyj1hSe9PxYSRZZdPTW.svg?)](https://asciinema.org/a/kivjrbRyj1hSe9PxYSRZZdPTW)

#### Recursive JSON @ Plain format
[![asciicast](https://asciinema.org/a/TW3TDGf5cCZr0sHH2mVMQHaas.svg?)](https://asciinema.org/a/TW3TDGf5cCZr0sHH2mVMQHaas)

#### Recursive JSON @ Json format
[![asciicast](https://asciinema.org/a/xH7L7UVwh4kdmno2GAwTbBNZr.svg?)](https://asciinema.org/a/xH7L7UVwh4kdmno2GAwTbBNZr)

---
### Installation
```commandline
pip3 install --upgrade git+https://github.com/mnogom/python-project-lvl2.git
```
