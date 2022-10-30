from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"slackUsername":"pacifistapx0", "backend":True, "age":25, "bio":"The most important step a man can take is always the next one"}