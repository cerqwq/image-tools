# 🖼️ Image Tools

AI图像工具集，支持图像分析、描述生成、标签提取。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 Alt文本生成
- 🏷️ SEO标签生成
- 🎨 构图建议
- 📱 社交媒体文案
- 🎨 配色分析
- 🖼️ 图像生成提示

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from image_tools import create_tools

tools = create_tools()

# 生成Alt文本
alt = tools.generate_alt_text("一只橘色猫咪坐在窗台上")

# 生成SEO标签
tags = tools.generate_seo_tags("产品图片", "电商")

# 构图建议
composition = tools.suggest_composition("风景照片")

# 社交媒体文案
caption = tools.generate_social_media_caption("美食照片", "instagram")

# 配色分析
colors = tools.analyze_color_palette("蓝色调的科技感背景")

# 图像生成提示
prompt = tools.generate_image_prompt("赛博朋克", "城市夜景", "霓虹灯")
```

## 📁 项目结构

```
image-tools/
├── tools.py       # 图像工具核心
└── README.md
```

## 📄 许可证

MIT License
