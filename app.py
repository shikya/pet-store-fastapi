import base64
import pandas as pd 
import json
import os

from fastapi import FastAPI, Header, Body
from typing import Annotated, List, Union
from pydantic import BaseModel

app = FastAPI()

DATA_FOLDER = "data"

# "name", "age", "color", "weight", "favorite_toy"

def filter_records(records, panda_query):
    ALL = slice(None)
    filtered = records.query(panda_query, engine='python')
    # print(filtered)
    return filtered

def paginate(records, limit, cursor):
    if cursor:
        cursor_data = base64.b64decode(cursor)
        cursor_json = json.loads(cursor_data)
        page = cursor_json['page']
    else:
        page = 1
    
    start_index = (page - 1) * limit
    end_index = start_index + limit
    print(start_index, end_index)
    paginated_records = records[start_index:end_index]
    next_cursor = base64.b64encode(json.dumps({'page': page + 1}).encode()).decode()
    
    return paginated_records, next_cursor


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post(
        '/search',
        responses = {
            200: {
                "description": "Data returned for the request",
                "content": {
                    "application/json": {
                        "example": {
                            "offset":   0,
                            "totalCount": 5,
                            "results": [
                                {
                                "index": 0,
                                "name": "Tigger",
                                "age": 5,
                                "color": "Brown",
                                "weight": 3.8,
                                "favorite_toy": "Catnip mice"
                                },
                                {
                                "index": 1,
                                "name": "Mittens",
                                "age": 1,
                                "color": "White",
                                "weight": 1.12,
                                "favorite_toy": "Tunnel"
                                }
                            ]
                        }
                    }
                }
            }
        }
    )
def search(
    breed: Annotated[str, Body(embed=True)],
    query: Annotated[str, Body(embed=True)],
    returnedFields: Annotated[List[str], Body(embed=True), []],
    limit: Annotated[int | None , Body(embed=True, gt=0)] = 10,
    offset: Annotated[int | None , Body(embed=True, gte=0)] = 10,
    location: str = Header(...),
):
    print({"breed": breed, "query": query, "returnedFields": returnedFields, "limit": limit, "offset": offset, "location": location })
    print("returnedFields")
    print(returnedFields)
    
    # Read CSV data
    records = pd.read_csv(os.path.join("data", location, breed + ".csv"))
    
    # Filter records based on panda query string
    filtered_records = filter_records(records, query)
    print("filtered_records")
    print(filtered_records)

    # Paginate results
    paginated_records_fields = filtered_records.reindex(columns=returnedFields)[offset:offset + limit]
    print("paginated_records_fields")
    print(paginated_records_fields)

    # Prepare response
    response = {
        "offset": offset,
        "results": json.loads(paginated_records_fields.reset_index().to_json(orient='records')),
        "totalCount": len(filtered_records)
    }
    
    return response

@app.post(
        '/search_with_cursor',
        responses = {
            200: {
                "description": "Data returned for the request",
                "content": {
                    "application/json": {
                        "example": {
                            "cursor": "eyJwYWdlIjogMn0=",
                            "totalCount": 5,
                            "results": [
                                {
                                "index": 0,
                                "name": "Tigger",
                                "age": 5,
                                "color": "Brown",
                                "weight": 3.8,
                                "favorite_toy": "Catnip mice"
                                },
                                {
                                "index": 1,
                                "name": "Mittens",
                                "age": 1,
                                "color": "White",
                                "weight": 1.12,
                                "favorite_toy": "Tunnel"
                                }
                            ]
                        }
                    }
                }
            }
        }
    )
def search_with_cursor(
    breed: Annotated[str, Body(embed=True)],
    query: Annotated[str, Body(embed=True)],
    returnedFields: Annotated[List[str], Body(embed=True), []],
    cursor: Annotated[str, Body(embed=True), ''] = '',
    limit: Annotated[int | None , Body(embed=True, gt=0)] = 10,
    location: str = Header(...),
):
    d = {"breed": breed, "query": query, "returnedFields": returnedFields, "cursor": cursor, "limit": limit, "location": location }
    print(d)
    print("returnedFields")
    print(returnedFields)
    
    # Read CSV data
    records = pd.read_csv(os.path.join("data", location, breed + ".csv"))
    
    # Filter records based on panda query string
    filtered_records = filter_records(records, query)
    print("filtered_records")
    print(filtered_records)

    # Paginate results
    paginated_records_all, next_cursor = paginate(filtered_records, limit, cursor)
    print("paginated_records_all")
    print(paginated_records_all)
    paginated_records_fields = paginated_records_all.reindex(columns=returnedFields)
    print("paginated_records_fields")
    print(paginated_records_fields)

    # Prepare response
    response = {
        "cursor": next_cursor,
        "results": json.loads(paginated_records_fields.reset_index().to_json(orient='records')),
        "totalCount": len(filtered_records)
    }
    
    return response
