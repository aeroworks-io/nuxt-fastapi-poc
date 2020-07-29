import uvicorn


def run():
    uvicorn.run("main:app", reload=True)
