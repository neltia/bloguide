# Blog Guide
<div style="text-align: right">
<a href="https://github.com/neltia/bloguide">English</a>
|
<a href="/docs/README_kr.md">한국어</a>
</div>

## About
Purpose:
- Automatically convert non-Markdown blog posts into Markdown format,
- analyze the converted text data, and provide insights.

Key Features (RoadMap):
- [ ] Provide API for Markdown conversion of blog posts.
- [ ] Provide text analysis API (search, statistics, correlation analysis).
- [ ] Offer public APIs for external users.
- [ ] Implement popular post search and recommendation features.
- [ ] Provide file upload and revision history management APIs.
- [ ] Support PDF report and statistical data download functionality.
- [ ] Use LLM for text summarization, comment generation, and recommendations.

Technologies Used:
- Lang: Python
- API: FastAPI
- DB: Elasticsearch, PostgreSQL

Target Users:
- Blog administrators.
- Users requiring blog content analysis.
- Content marketing professionals.

## Getting Started
- python 3.10+
- FastAPI
- Uvicorn (ASGI server)
- Other dependencies as listed in `requirements.txt`

### Installation
- virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
