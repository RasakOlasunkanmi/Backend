from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os
from typing import Optional


load_dotenv()

app = FastAPI(title = 'Simple FastAPI App', version = '1.0.0')
data = [{"name": "Sam Larry", "age": 20, "track": "AI Developer"},
        {"name": "Bahubali", "age": 21, "track": "Backend Developer"},
        {"name": "John Doe", "age": 22, "track": "Frontend Developer"}]


class Item(BaseModel):
    name: str = Field(..., example="Perpetual")
    age: int = Field(..., example=25)
    track: str = Field(..., example="Frontend Developer")

@app.get("/", description = "This endpoint just returns a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI Application"}

@app.get("/get-data")
def get_data():
    return data

@app.post("/create")
def create_data(req: Item):
    data.append(req.dict())
    print(data)
    return {"Message": "Data Received", "Data": data}

@app.put("/update_data/{id}")
def update_data(id: int, req: Item):
    data[id] = req.dict()
    print(data)
    return {"Message": "Data Updated", "Data": data}

# Assignment
# write an endpoint to patch and delete entries from the data var

class PatchItem(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    track: Optional[str] = None

@app.patch("/edit-data/{id}")
def edit_data(id: int, req: PatchItem):
    try:
        existing = data[id]
    except IndexError:
        return {"Message": "Record not found"}

    try:
        updates = req.model_dump(exclude_unset=True)
    except AttributeError:
        updates = req.model_dump(exclude_unset=True)

    if updates:
        existing.update(updates)
        data[id] = existing
        print(data)
        return {"Message": "Data edited", "Data": data}
    else:
        return {"Message": "No fields to update", "Data": data}
    
    
@app.delete("/delete-data/{id}")
def delete_data(id: int):
    try:
        del data[id]
        print(data)
        return {"Message": "Data Deleted", "Data": data}
    except IndexError:
        return {f"Message": "Record not found"}


if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host = os.getenv("host"), port = int(os.getenv("port")))
    c