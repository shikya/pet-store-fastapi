# Pet Store FastAPI

## Getting Started

This is a repo which contains sample api request for PET Store.

### Prerequisites

1. python>=3.12

### Installation

1. Clone the repo
2. (Optional) Use venv to create a virtual environment. 
2. install dependancies using `pip install -r requirements.txt`.
3. Run `fastapi dev app.py`.

### Working

Open http://localhost:8000/docs to generate and view OpenAPI spec

### Generate fake data

Run `py fake-data-generate.py` to generate fakedata in data directory

### Example Curl

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/search' \
  -H 'accept: application/json' \
  -H 'location: NYC' \
  -H 'Content-Type: application/json' \
  -d '{
  "breed": "cat_siamese",
  "query": "@ALL",
  "returnedFields": [
    "name", "age", "color", "weight", "favorite_toy"
  ],
  "limit": 3,
  "offset": 0
}'
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/search_with_cursor' \
  -H 'accept: application/json' \
  -H 'location: NYC' \
  -H 'Content-Type: application/json' \
  -d '{
  "breed": "cat_siamese",
  "query": "@ALL",
  "returnedFields": [
    "name", "age", "color", "weight", "favorite_toy"
  ],
  "cursor": "",
  "limit": 1
}'
```
