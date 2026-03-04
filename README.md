# VidyāMitra Backend

FastAPI backend for the VidyāMitra Intelligent Career Agent.

## 🚀 Features

- AI-powered resume analysis with Gemini integration
- Personalized training plans
- Mock interview sessions
- Quiz system with multiple domains
- Job recommendations
- User authentication with JWT
- Supabase database integration

## 📋 Prerequisites

- Python 3.9+
- Virtual environment
- API keys (see environment variables)

## 🛠️ Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🔧 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
GEMINI_API_KEY=your_gemini_key
YOUTUBE_API_KEY=your_youtube_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
PEXELS_API_KEY=your_pexels_key
NEWS_API_KEY=your_news_key
EXCHANGE_API_KEY=your_exchange_key
JWT_SECRET=your_jwt_secret
```

## 🚀 Running Locally

```bash
# Start the server
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Or use the start script
python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## 📚 API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation.

## 🐳 Docker Support

```bash
# Build image
docker build -t vidyamitra-backend .

# Run container
docker run -p 8000:8000 vidyamitra-backend
```

## 🌐 Deployment

### Render Deployment

1. Connect this repository to Render
2. Create a new Web Service
3. Environment: Python
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add all environment variables

## 📊 Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Database**: Supabase (PostgreSQL)
- **AI**: Google Gemini, OpenAI
- **Authentication**: JWT
- **Deployment**: Render

## 📝 License

MIT License
