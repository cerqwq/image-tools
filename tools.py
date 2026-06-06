"""
Image Tools - AI图像工具集
支持图像分析、描述生成、标签提取
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class ImageTools:
    """
    AI图像工具集
    支持：分析、描述、标签、优化建议
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_alt_text(self, image_description: str) -> str:
        """生成替代文本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下图片生成简洁的alt文本：

描述：{image_description}

要求：
1. 简洁明了
2. 描述主要内容
3. 适合屏幕阅读器
4. 100字符以内"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        return response.choices[0].message.content

    def generate_seo_tags(self, image_description: str, context: str = "") -> List[str]:
        """生成SEO标签"""
        if not self.client:
            return ["LLM客户端未配置"]

        prompt = f"""请为以下图片生成SEO标签：

描述：{image_description}
{f'上下文：{context}' if context else ''}

请返回JSON数组格式：["标签1", "标签2", ...]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [response.choices[0].message.content]

    def suggest_composition(self, image_description: str) -> Dict:
        """建议构图"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下图片的构图并提供改进建议：

描述：{image_description}

请返回JSON格式：
{{
    "current_composition": "当前构图分析",
    "suggestions": ["建议1", "建议2"],
    "rule_of_thirds": "三分法建议",
    "leading_lines": "引导线建议",
    "balance": "平衡建议"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"suggestion": content}

    def generate_social_media_caption(self, image_description: str, platform: str = "instagram") -> str:
        """生成社交媒体文案"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下图片生成{platform}文案：

描述：{image_description}

要求：
1. 吸引眼球
2. 包含表情符号
3. 包含话题标签
4. 符合{platform}风格"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def analyze_color_palette(self, image_description: str) -> Dict:
        """分析配色"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下图片的配色方案：

描述：{image_description}

请返回JSON格式：
{{
    "dominant_colors": [{{"name": "颜色名", "hex": "#xxx", "percentage": "占比"}}],
    "mood": "色彩情绪",
    "harmony": "配色和谐度",
    "suggestions": ["建议1", "建议2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def generate_image_prompt(self, style: str, subject: str, details: str = "") -> str:
        """生成图像生成提示"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下需求生成AI图像生成提示：

风格：{style}
主题：{subject}
细节：{details}

要求：
1. 详细描述
2. 包含风格关键词
3. 包含技术参数
4. 适合Midjourney/Stable Diffusion"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> ImageTools:
    """创建图像工具"""
    return ImageTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Image Tools")
    print()

    # 测试
    alt = tools.generate_alt_text("一只橘色猫咪坐在窗台上，阳光洒在它身上")
    print(f"Alt text: {alt}")

    tags = tools.generate_seo_tags("一只橘色猫咪坐在窗台上")
    print(f"Tags: {tags}")
