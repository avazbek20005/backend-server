from fastapi import FastAPI
import uvicorn

# 1. Create the app instance. This "app" object is your whole backend.
app = FastAPI(title="My First Backend")


# 3. A basic GET endpoint - just returns some data
@app.get("/hello/{number}")
def say_hello(number):
    return {"message": "Hello! Your backend is working. Number is "+str(number)}



# 7. Allows running with: python main.py (instead of the uvicorn command)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)