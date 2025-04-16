# seo_agent.py

import os
import re
import math
from typing import Dict
from google.generativeai import GenerativeModel
import google.generativeai as genai
import aiohttp
# import textstat

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = GenerativeModel("gemini-1.5-pro")

class SEOAgent:
    def __init__(self, topic: str, blog_md: str):
        self.topic = topic
        self.blog_md = blog_md
        self.datamuse_url = f"https://api.datamuse.com/words?ml={topic}"

    async def generate_seo_metadata(self) -> Dict:
        keywords = await self.fetch_keywords()
        response = model.generate_content(
            f"Given this blog content in Markdown, extract:\n"
            f"- A catchy SEO title\n"
            f"- A meta description (max 160 characters)\n"
            f"- 5-7 SEO tags\n"
            f"- A URL slug\n\n"
            f"Blog Content:\n{self.blog_md}"
        )

        raw_output = response.text
        return {
            "title": self.extract_field(raw_output, "title"),
            "description": self.extract_field(raw_output, "description"),
            "tags": keywords,
            "slug": self.slugify(self.topic),
            "reading_time": self.estimate_reading_time(self.blog_md),
        }

    async def fetch_keywords(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.datamuse_url) as response:
                data = await response.json()
                return [word["word"] for word in data[:7] if "word" in word]

    def estimate_reading_time(self, text: str) -> int:
        words = len(text.split())
        return math.ceil(words / 200)

    def slugify(self, text: str) -> str:
        return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

    def extract_field(self, content: str, field: str) -> str:
        lines = content.splitlines()
        for line in lines:
            if field.lower() in line.lower():
                return line.split(":", 1)[-1].strip()
        return ""
    
        
