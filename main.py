from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"SlackUsername":"pacifistapx0", "backend":True, "age":1, "bio":"The most important step a man can take is always the next one"}