from enum import Enum 
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel


app = FastAPI()

class operation_type(Enum):
    multiplication= 1
    addition= 2
    subtraction = 3

class Post(BaseModel):
    operation_type: str
    x: int
    y: int

operation_list = ["multiplication", "addition", "subtraction"]

@app.get("/")
def root():
    return {"slackUsername":"pacifistapx0", "backend":True, "age":25, "bio":"The most important step a man can take is always the next one"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post:Post):
    print(post)
    value = 0
    if post.operation_type.lower() not in operation_list:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    try:
        if post.operation_type.lower() == operation_type.multiplication.name:
            value = post.x * post.y
            return {"slackUsername": "pacifistapx0", "result": value, "operation_type":operation_type.multiplication.value}
        elif post.operation_type.lower() == operation_type.addition.name:
            value = post.x + post.y
            return {"slackUsername": "pacifistapx0", "result": value, "operation_type":operation_type.addition.value}
        else:
            post.operation_type.lower() == operation_type.subtraction.name
            value = post.x - post.y
            return {"slackUsername": "pacifistapx0", "result": value, "operation_type":operation_type.subtraction.value}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="Operation not available")
    