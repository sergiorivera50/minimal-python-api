from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return { "Hello": "World" }

# This is just simply a new route
@app.get("/new")
def new():
  return { "msg": "This is a new route!" }
