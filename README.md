# 🎥 YouTube → Blog Generator

Convert any YouTube video into a clean, SEO-optimized blog post using CrewAI, Groq LLM, and Streamlit.

##  Overview

This project transforms YouTube videos into well-structured, SEO-friendly blog articles. It retrieves the transcript, summarizes key ideas, and generates a polished blog post — all automated using a multi-agent CrewAI workflow.

Built for creators, writers, educators, and anyone who wants to repurpose YouTube content into publish-ready blogs.

##  Features

- **One-click YouTube → Blog conversion**
- **Transcript extraction** (no API key needed for YouTube transcript)
- **Groq LLM integration** for ultra-fast generation
- **CrewAI multi-agent workflow**
  - Transcript Agent → retrieves + summarizes
  - Writer Agent → generates full blog (700–1000 words)
- **Clean Streamlit UI**
- **Live logs panel**
- **Automatic Markdown export**
- **Stores output inside `/outputs/` folder**

##  Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Groq Llama 3.1 / 3.3 |
| Agent Orchestration | CrewAI |
| UI | Streamlit |
| Transcript Retrieval | youtube-transcript-api |
| Language | Python |

## 📂 Project Structure

```
CrewAi/
│
├── streamlit_app.py          # User interface
├── main.py                   # Standalone runner (optional)
│
├── pipeline/
│     ├── run_pipeline.py     # Main automation pipeline
│
├── agents/
│     ├── transcript_agent.py
│     ├── writer_agent.py
│
├── tasks/
│     ├── extraction_task.py
│     ├── writing_task.py
│
├── tools/
│     ├── youtube_tool.py     # Custom transcript tool
│
├── outputs/                  # Generated blogs
├── requirements.txt
└── README.md
```

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/yt-blog-generator
cd yt-blog-generator
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_key
GROQ_MODEL_NAME=llama-3.1-70b-versatile
```

You can get your Groq API key from: [https://console.groq.com](https://console.groq.com)

##  Running the Application

Launch the Streamlit interface:

```bash
streamlit run streamlit_app.py
```

Then open the browser link (usually `http://localhost:8501/`).

##  How It Works

1. **User enters a YouTube URL**
   ↓
2. **The Transcript Agent retrieves transcript**
   ↓
3. **The same agent summarizes main points**
   ↓
4. **The Writer Agent generates a full blog (Markdown)**
   ↓
5. **Streamlit displays the content + saves it as a `.md` file**

##  Example Output

- Title suggestion
- 2–3 paragraph summary
- Five key takeaways
- Full blog article (700–1000 words)
- Markdown headings & structure

##  Roadmap

- [ ] Add multiple LLM provider options
- [ ] Add image generation for blog thumbnails
- [ ] Support long videos with auto-chunking
- [ ] Add SEO scoring
- [ ] Add multi-language transcript support

##  Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you want to improve.

##  License

This project is open-source under the MIT License.

