from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello GitOps! My CI/CD pipeline is working."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
