# PRISM
**AI-Powered PR Review System**

## Overview
**PRISM** is an advanced microservices-based solution that automates GitHub Pull Request (PR) reviews using cutting-edge Large Language Models (LLMs). Designed for scalability and efficiency, PRISM handles multiple file modifications in PRs, providing intelligent feedback and insights to improve code quality.

## Key Features
- **Automated PR Reviews**: Integrates LLMs to analyze and review code changes.
- **Microservices Architecture**: Combines Django REST Framework and FastAPI for seamless API handling.
- **Asynchronous Processing**: Utilizes Celery and Redis to manage concurrent tasks efficiently.
- **Scalable Design**: Processes large and complex PRs with high performance.
- **Intelligent Insights**: Leverages GROQ and Meta’s LLaMA models for accurate and context-aware code reviews.

## Tech Stack
- **Languages**: Python
- **Frameworks**: Django REST Framework, FastAPI
- **Task Management**: Celery
- **Message Brokering and Caching**: Redis
- **LLM Integration**: GROQ, Meta LLaMA
- **API Integration**: GitHub API


## How It Works
1. **Request Submission**: The client sends a PR review request through FastAPI.
2. **Backend Processing**: Django REST Framework handles the backend logic and routes requests.
3. **LLM Analysis**: Integrated LLMs process and review code changes for feedback.
4. **Asynchronous Task Handling**: Celery and Redis manage multiple modified file reviews concurrently.
5. **Feedback Generation**: Insights and suggestions are returned to the client for review.

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Celery 
- Redis (for caching and message brokering)

## Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Nikky000/PRISM.git
   cd prism

Configure Redis:

Ensure Redis is running on your system and verify the connection settings in the settings.py file.
Start the Celery worker:

celery -A your_project_name worker --loglevel=info

Run the servers:
Django:
python manage.py runserver 8001

FastAPI:
uvicorn main:app --reload
