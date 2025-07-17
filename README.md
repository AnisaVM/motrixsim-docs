# MotrixSim Docs

![PyPI - Version](https://img.shields.io/pypi/v/motrixsim)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/motrixsim)

![GitHub License](https://img.shields.io/github/license/motphys/motrixsim-docs)

`MotrixSim` 是一个高性能的物理仿真引擎，专为多体动力学和机器人仿真设计。它提供了一个高效、稳定的物理仿真平台，支持广泛的应用场景，包括机器人控制、强化学习、工业仿真等。

> 文档地址：https://motrixsim.readthedocs.io

## 主要特性

-   **物理仿真**: 支持刚体动力学、碰撞检测等完整的物理仿真功能
-   **广义坐标建模**: 采用广义坐标系统，支持复杂的多体系统建模
-   **全新求解器**: 采用自研的约束模型和求解器，提供高效、稳定的多体动力学计算
-   **高性能计算**: CPU 版本基于 Rust 开发，提供出色的性能和内存安全性
-   **Python API**: 简洁易用的 Python 接口，便于快速开发和原型制作
-   **机器人支持**: 专门优化的机器人仿真功能，高度兼容 MJCF 模型格式

## 适用场景

-   机器人控制算法开发和测试
-   强化学习环境构建
-   工业实时物理仿真
-   物理现象模拟和分析
-   工程设计验证
-   教育和研究

## 🚀 快速开始

> 以下示例使用了 Python 项目管理工具：[PDM](https://pdm-project.org/)
> 
> 在开始之前，请先[安装](https://pdm-project.org/en/latest/#installation)该工具。

### 1. 克隆仓库:

```bash
git clone https://github.com/Motphys/motrixsim-docs
```

### 2. 创建虚拟环境

```bash
cd motrixsim-docs

pdm use 3.10
```

### 3. 安装依赖

```
# 检查更新并安装依赖
pdm install -G examples -v

# 不检查更新，直接安装依赖
pdm sync -G examples -v
```

### 4. 执行对比与示例

> 参考 [文档](https://motrixsim.readthedocs.io) 中的说明

## 📬 联系方式

有问题或建议？欢迎通过以下方式联系我们：

- GitHub Issues: [提交问题](https://github.com/Motphys/motrixsim-docs/issues)

- Discussions: [加入讨论](https://github.com/Motphys/motrixsim-docs/discussions)
