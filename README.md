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
  - Writer Agent → generates full blog with customizable length
- **Configurable blog settings**
  - Adjustable blog length (Short: 400-600, Medium: 700-1000, Long: 1200-1500 words)
  - Optional FAQ section
  - Temperature control for LLM creativity
  - Model selection (Llama 3.1/3.3)
- **Clean Streamlit UI** with sidebar controls
- **Live logs panel** for execution tracking
- **Automatic Markdown export** with download button
- **Stores output inside `/outputs/` folder** with timestamps

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
├── streamlit_app.py          # Streamlit user interface
├── app/                      # Main application package
│   ├── __init__.py
│   ├── main_pipeline.py      # Main automation pipeline
│   │
│   ├── agents/               # CrewAI agents
│   │   ├── transcript_agent.py
│   │   └── writer_agent.py
│   │
│   ├── tasks/                # CrewAI tasks
│   │   ├── extraction_task.py
│   │   └── writing_task.py
│   │
│   ├── tools/                # Custom tools
│   │   └── yt_transcript_tool.py
│   │
│   ├── config/               # Configuration
│   │   └── llm_config.py
│   │
│   └── utils/                # Utility functions
│       └── __init__.py
│
├── outputs/                  # Generated blog posts (auto-created)
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not in git)
├── .gitignore
└── README.md
```

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/MuhammadAkmal03/CrewAI
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

##  Running the Application

Launch the Streamlit interface:

```bash
streamlit run streamlit_app.py
```

Then open the browser link (usually `http://localhost:8501/`).

##  How It Works

1. **User enters a YouTube URL** and configures settings (blog length, FAQ, temperature, model)
   ↓
2. **The Transcript Agent retrieves transcript** using the YouTube Transcript API
   ↓
3. **The same agent summarizes main points** (2-3 paragraphs, 5 key takeaways, 3 title suggestions)
   ↓
4. **The Writer Agent generates a full blog** (Markdown format) based on the summary and user preferences
   ↓
5. **Streamlit displays the content** + automatically saves it as a `.md` file in `/outputs/` folder

##  Example Output

- **Three blog title suggestions** (numbered list)
- **Brief summary** (2–3 paragraphs, user-friendly)
- **Five key takeaways** (bulleted list, one line each)
- **Full blog article** (configurable length: 400-1500 words)
- **Markdown formatting** with proper headings (##, ###)
- **Optional FAQ section** (5-7 Q&A pairs if enabled)

##  Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you want to improve.

##  License

This project is open-source under the MIT License.

