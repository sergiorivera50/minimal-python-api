from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return { "Hello": "World" }

@app.get("/new")
def new():
  return { "msg": "This is a new route!" }
