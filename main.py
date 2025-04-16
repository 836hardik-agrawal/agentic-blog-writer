# main.py

import argparse
import asyncio
import os
from context_agent import ContextAgent
from writing_agent import WritingAgent
from seo_agent import SEOAgent
from execution_agent import ExecutionAgent


async def run_blog_pipeline(topic: str, tone: str = "educational", output_dir: str = "blogs",return_data: bool = False):
    print(f"🚀 Starting blog generation for topic: '{topic}' with tone: '{tone}'")

    # Step 1: Context Gathering
    context_agent = ContextAgent(topic)
    print("🔍 Fetching context...")
    context = await context_agent.gather_context()
    # print(context["news"])

    # Step 2: Blog Writing
    writer = WritingAgent(topic, context, tone)
    print("✍️ Generating blog content...")
    blog_md = await writer.generate_blog()

    # Step 3: SEO Optimization
    seo_agent = SEOAgent(topic, blog_md)
    print("📈 Extracting SEO metadata...")
    metadata = await seo_agent.generate_seo_metadata()

    # Step 4: Export
    executor = ExecutionAgent(output_dir)
    executor.export(blog_md, metadata)

    # Summary
    print("✅ Blog generation complete!")
    print("\n📝 Metadata Summary:")
    for key, val in metadata.items():
        print(f"{key.capitalize()}: {val}")
    
    if return_data:
        return blog_md, metadata

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agentic Blog Writer")
    parser.add_argument("--topic", type=str, required=True, help="Topic for the blog post")
    parser.add_argument("--tone", type=str, default="educational", help="Tone of the blog (e.g., formal, creative, technical)")
    parser.add_argument("--output_dir", type=str, default="blogs", help="Output directory for blog files")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    asyncio.run(run_blog_pipeline(args.topic, args.tone, args.output_dir))
