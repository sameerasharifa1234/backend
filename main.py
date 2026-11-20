from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/hello")
def hello():
    return {
        "message":"Hello,World!",
    }


@app.post("/user")
def create_user(user_id: int,name:str, age:int):
    return{
        "message": "User created successfully",
        "user_id": user_id,
        "name": name,
        "age": age
    }

@app.put("/user/{user_id}")
def update_user(user_id: int, name:str , age:int):
    return{
        "message":"User updated successfully",
        "user_id": user_id,
        "name": name,
        "age": age
    }

@app.patch("/user/{user_id}")
def update_user_partial(user_id: int, age: int):
    return {
        "message": "User partially updated successfully",
        "user_id": user_id,
        "age": age
    }

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "User deleted successfully",
        "user_id" : user_id
    }
