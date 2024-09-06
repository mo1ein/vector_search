# Vector Search

## Project Overview

This project demonstrates a search functionality for [Hacker News](https://news.ycombinator.com/) articles using modern web technologies and natural language processing techniques. It consists of three main components:

1. A web scraper that collects articles from Hacker News
2. A vector embedding system that converts article text into numerical representations
3. A FastAPI-based search API that finds similar articles based on user queries

## Technologies Used

- **FastAPI**
- **Pydantic**
- **PostgreSQL**
- **SQLAlchemy**
- **BeautifulSoup**
- **Sentence Transformers**

## Installation
```bash
git clone https://github.com/mo1ein/vector_search.git
cd vector_search
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
If packages are large (like `torch`) and you got _timout_ error, you can use this command:
```bash
pip install -r requirements.txt --default-timeout=1000
```

## Run
Set your database configs in `.env`file. create a database with name `vector_db` in your connected postgres then run [migrations](migrations/init.up.sql). <br>
I recommend to use [`pycharm extension`](https://www.jetbrains.com/help/pycharm/relational-databases.html) or [`datagrip`](https://www.jetbrains.com/datagrip/).
```bash
python main.py
```
Then, enjoy the app!
[`http://127.0.0.1:8500/docs#/`](http://127.0.0.1:8500/docs#/)

### Endpoints
Scrap data, embed to vector and insert to database. Body is empty. This operation may take several seconds to complete.
```
POST /
```

Search string query and find similarity.
```
POST /search
```
First should run `/` endpoint to get data then you can use `/search`.

### Examples

Scrap data
```bash
curl -X POST http://0.0.0.0:8500
```
response:
```text
"Text extracted, embedded and saved to db successfully!" 
```

Search
```bash
 curl -X POST \
  http://0.0.0.0:8500/search \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "rust"
}'
```
response:
```json
{"similar_text":"Swift is a more convenient Rust Understanding the Y Combinator"}
```
