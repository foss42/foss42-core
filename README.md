[![Discord Server Invite](https://img.shields.io/badge/DISCORD-JOIN%20SERVER-5663F7?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/2s49SCNfyJ)

<!--This project is participating in GSSoC 2024.

![gssoc-logo-1](https://github.com/foss42/awesome-generative-ai-apis/assets/1382619/670b651a-15d7-4869-a4d1-6613df09fa37)-->

Contributors should go through the [Contributing Guide](https://github.com/foss42/foss42-core/blob/main/CONTRIBUTING.md) to learn how to setup development environment, raise an issue and send across a PR.

# foss42

![PyPI](https://img.shields.io/pypi/v/foss42?logo=python&logoColor=yellow&style=for-the-badge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/foss42?logo=python&logoColor=yellow&style=for-the-badge)

Core Python library for [foss42 Open Source APIs](https://github.com/foss42/api). 

## Installation

```
pip3 install foss42
```

## List of available functions

[Link](https://foss42.github.io/foss42-core)

## Usage example

```python
>>> import foss42.text.humanize as hz
>>> hz.humanize_bytes(1126,
                      2,
                      prefix = True,
                      trailing_zeros = True)
>>> '1.10 kilobytes'
```
