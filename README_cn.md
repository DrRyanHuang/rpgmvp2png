简体中文 | [English](./README.md)

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

一个用于将 RPG Maker MV 加密图像 (`.rpgmvp`) 转换为标准 PNG 格式的轻量级工具。提供 Python 命令行版本和网页版。

<div align="center">
  <img src="logo/CutIn_Furea.png" width="50%" alt="Logo">
</div>

## 1. 功能特点

- **批量处理**：支持递归解密整个文件夹。
- **跨平台**：通过 Python 支持 Windows, macOS 和 Linux。
- **网页版**：无需安装即可在浏览器中解密。

## 2. 使用说明

### 命令行工具 (CLI)

需要 Python 3.10+ 环境。

**示例文件：**

你可以在 `examples/` 目录下找到一些 `.rpgmvp` 文件来测试本工具。

**解密单个文件：**

```bash
python rpgmvp2png.py examples/Fire1.rpgmvp out.png
```

**解密整个目录：**

```bash
python rpgmvp2png.py examples
```

_此命令将在当前目录下创建一个与原目录结构一致的文件夹，其中包含解密后的 PNG 图片。_

### 网页工具

在线使用地址：[RPGMVP2PNG Web](https://drryanhuang.github.io/rpgmvp2png/rpgmvp2png.html)

1.  选择 `.rpgmvp` 文件。
2.  选择是否打包为 ZIP 下载。
3.  处理并保存图片。

## 3. 开发指南

本项目使用 `uv` 进行项目管理。我们使用 `ruff` 进行代码检查和格式化，使用 `pyright` 进行静态类型检查。

### 环境配置

```bash
# 安装依赖
uv sync
```

### 代码检查与格式化

```bash
# 运行 ruff 检查
uv run ruff check .

# 运行 ruff 格式化
uv run ruff format .
```

### 类型检查

```bash
# 运行 pyright
uv run pyright
```

## 4. 免责声明

本工具仅供学习和参考使用。请遵守相关版权法律法规，切勿将本工具用于任何非法用途。
