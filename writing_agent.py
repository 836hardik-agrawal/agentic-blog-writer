# writing_agent.py

import os
from typing import Dict
from google.generativeai import GenerativeModel
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-pro")

class WritingAgent:
    def __init__(self, topic: str, context: Dict, tone: str = "educational"):
        self.topic = topic
        self.context = context
        self.tone = tone

    async def generate_blog(self) -> str:
        context_text = self._compose_context()
        prompt = (
            f"Write a detailed, long-form SEO blog post in Markdown format on the topic: '{self.topic}'.\n"
            f"Use the following style: {self.tone}.\n"
            f"Incorporate relevant news references, quotes, and keywords where appropriate.\n"
            f"Structure:\n"
            f"1. Engaging Introduction (~100-150 words)\n"
            f"2. H2-based outline with 4-5 subheadings, each 200-300 words\n"
            f"3. Strong Conclusion with Call-to-Action\n"
            f"4. Format everything in Markdown with headings, bullets, etc.\n\n"
            f"5. Dont write Note in the last."
            f"Here’s the contextual background you can use:\n{context_text}"
        )

        response = model.generate_content(prompt)
        return response.text

    def _compose_context(self) -> str:
        news_snippets = "\n".join([f"- {article['title']}" for article in self.context.get("news", [])])
        quotes = "\n".join([f"> {quote}" for quote in self.context.get("quotes", [])])
        keywords = ", ".join(self.context.get("keywords", []))

        return (
            f"Keywords: {keywords}\n\n"
            f"Recent News:\n{news_snippets}\n\n"
            f"Quotes:\n{quotes}"
        )
