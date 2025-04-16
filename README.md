# 🧠 Agentic Python Blog Writer

An autonomous content generation agent that mimics a junior blog writer + SEO optimizer. Powered by LLMs and public APIs, it can research, generate, optimize, and export long-form SEO blogs — all in one go.

---

## 🚀 Features

- ✍️ **Automated Blog Writing** using Google Gemini Pro API
- 🔍 **Research Agent** pulls context from:
  - NewsData.io (latest news)
  - Datamuse (keyword expansion)
  - Quotable.io (relevant quotes)
- 📈 **SEO Optimizer** generates:
  - Meta title, description, tags
  - URL slug and reading time
- 📄 **Exports**:
  - Blog in Markdown (`.md`)
  - Metadata in JSON (`.json`)
- 📊 **Readability Score** (Flesch-Kincaid)
- 🌐 **Streamlit UI** for non-CLI users

---

## 🧩 Architecture

main.py               
    Entry point – runs the blog generation pipeline

context_agent.py      
    Gathers external research info (NewsData, Datamuse, Quotable)

writing_agent.py      
    Uses Gemini Pro API to write blog content

seo_agent.py          
    Extracts metadata and SEO keywords

execution_agent.py    
    Handles export of markdown and metadata

streamlit_app.py      
    Streamlit-based web interface


.env                  
    API keys for Gemini, NewsData.io, etc.

blogs/                
    Output folder for generated blogs and metadata

requirements.txt      
    Python dependencies


## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/836hardik-agrawal/agentic-blog-writer.git
cd agentic-blog-writer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup API Keys
```bash
GEMINI_API_KEY=your_google_gemini_key
NEWSDATA_API_KEY=your_newsdata_api_key
```

### 4. Run the CLI
```bash
python main.py --topic "How Python is used in AI" --tone "educational"
```

### 5. Run the Web UI
```bash
streamlit run streamlit_app.py
```



