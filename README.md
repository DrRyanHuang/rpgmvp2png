[简体中文](./README_cn.md) | English

# RPGMVP2PNG

<!-- star数, fork数, pulls数, issues数, contributors数, 开源协议 -->

<a href="https://github.com/DrRyanHuang/rpgmvp2png/stargazers"><img src="https://img.shields.io/github/stars/DrRyanHuang/rpgmvp2png" alt="Stars Badge"/></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/network/members"><img src="https://img.shields.io/github/forks/DrRyanHuang/rpgmvp2png" alt="Forks Badge"/></a>
<br/>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/pulls"><img src="https://img.shields.io/github/issues-pr/DrRyanHuang/rpgmvp2png" alt="Pull Requests Badge"/></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/issues"><img src="https://img.shields.io/github/issues/DrRyanHuang/rpgmvp2png" alt="Issues Badge"/></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/DrRyanHuang/rpgmvp2png?color=2b9348"></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/blob/master/LICENSE"><img src="https://img.shields.io/github/license/DrRyanHuang/rpgmvp2png?color=2b9348" alt="License Badge"/></a>
<br/>
<a href=""><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python Version"/></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/actions/workflows/ci.yml"><img src="https://github.com/DrRyanHuang/rpgmvp2png/actions/workflows/ci.yml/badge.svg" alt="Python CI"/></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/actions/workflows/static.yml"><img src="https://github.com/DrRyanHuang/rpgmvp2png/actions/workflows/static.yml/badge.svg" alt="Deploy static content to Pages"/></a>

A lightweight tool to convert RPG Maker MV encrypted images (`.rpgmvp`) to standard PNG format. Available as a Python CLI and a web-based tool.

<div align="center">
  <img src="logo/CutIn_Furea.png" width="50%" alt="Logo">
</div>

## 1. Features

- **Batch Processing**: Decrypt entire directories recursively.
- **Cross-Platform**: Works on Windows, macOS, and Linux via Python.
- **Web Interface**: Browser-based decryption without installation.

## 2. Usage

### CLI Tool

Requires Python 3.10+.

**Examples:**

You can find sample `.rpgmvp` files in the `examples/` directory to test the tool.

**Decrypt a single file:**

```bash
python rpgmvp2png.py examples/Fire1.rpgmvp out.png
```

**Decrypt an entire directory:**

```bash
python rpgmvp2png.py examples
```

_This creates a mirrored directory structure with the decrypted PNGs._

### Web Tool

Access the online converter here: [RPGMVP2PNG Web](https://drryanhuang.github.io/rpgmvp2png/rpgmvp2png.html)

1.  Select `.rpgmvp` files.
2.  Choose whether to download as a ZIP archive.
3.  Process and save your images.

## 3. Development

This project uses `uv` for project management. We use `ruff` for linting and formatting, and `pyright` for static type checking.

### Setup

```bash
# Install dependencies
uv sync
```

### Linting and Formatting

```bash
# Run ruff check
uv run ruff check .

# Run ruff format
uv run ruff format .
```

### Type Checking

```bash
# Run pyright
uv run pyright
```

## 4. Disclaimer

This tool is for educational purposes only. Please respect copyright laws and do not use this tool for illegal activities.
