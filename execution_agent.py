# execution_agent.py

import os
import json
from datetime import datetime
from pathlib import Path

class ExecutionAgent:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)

    def export(self, blog_md: str, metadata: dict):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        slug = metadata.get("slug", "blog")

        md_filename = self.output_dir / f"{slug}_{timestamp}.md"
        json_filename = self.output_dir / f"{slug}_{timestamp}.json"

        with open(md_filename, "w", encoding="utf-8") as md_file:
            md_file.write(blog_md)

        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump(metadata, json_file, indent=4)

        print(f"📄 Blog Markdown saved at: {md_filename}")
        print(f"🧠 Metadata JSON saved at: {json_filename}")
