# context_agent.py

import aiohttp
import asyncio
from typing import List, Dict
from functools import lru_cache

class ContextAgent:
    def __init__(self, topic: str):
        self.topic = topic
        # self.news_url = f"https://newsdata.io/api/1/news?apikey={self._get_api_key()}&q={topic}&language=en"
        self.news_url = f"https://newsdata.io/api/1/news?apikey={self._get_api_key()}&q={topic}&language=en"
        self.datamuse_url = f"https://api.datamuse.com/words?ml={topic}"
        self.quotable_url = "https://api.quotable.io/quotes/random?limit=5"
    @lru_cache
    def _get_api_key(self):
        import os
        return os.getenv("NEWSDATA_API_KEY")

    async def gather_context(self) -> Dict:
        async with aiohttp.ClientSession() as session:
            news_task = session.get(self.news_url)
            
            keywords_task = session.get(self.datamuse_url)
            # quotes_task = session.get(self.quotable_url)

            # responses = await asyncio.gather(news_task, keywords_task, quotes_task)
            responses = await asyncio.gather(news_task, keywords_task)
            news_json = await responses[0].json()
            keywords_json = await responses[1].json()
            # quotes_json = await responses[2].json()

            return {
                "news": news_json.get("results", [])[:5],
                "keywords": [word["word"] for word in keywords_json[:7] if "word" in word],
                # "quotes": [q["content"] for q in quotes_json.get("results", [])]
            }
