# AB测试样本量计算器

## 项目简介
这是一个用于计算AB测试所需最小样本量的Python工具，基于统计功效分析。支持中英文界面切换。

## 功能特点
- 计算AB测试所需最小样本量
- 支持中英文双语界面
- 友好的图形用户界面
- 实时计算结果
- 详细的参数说明

## 使用方法
1. 安装依赖：`pip install -r requirements.txt`
2. 运行程序：`python main.py`
3. 输入参数：
   - 目标转化率基线 (0-1)
   - 最小可检测效果 (%)
   - 统计功效 (0-1)
   - 显著性水平 (0-1)
4. 点击"计算样本量"按钮查看结果

## 参数说明
- **目标转化率基线**：当前转化率
- **最小可检测效果**：希望检测到的最小变化百分比
- **统计功效**：检测到真实差异的概率
- **显著性水平**：第一类错误概率

## 示例
假设：
- 当前转化率：0.55
- 最小可检测效果：4%
- 统计功效：0.8
- 显著性水平：0.05

计算结果：每个实验组需要约8,027个样本

## 依赖要求
- Python 3.6+
- tkinter
- scipy
- numpy
