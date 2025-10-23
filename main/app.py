import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is running"}

@app.post("/predict")
def run_lscpu():
    try:
        result = subprocess.run(["lscpu"], capture_output=True, text=True, check=True)
        print("===== CPU INFO START =====")
        print(result.stdout)   # 👈 cái này sẽ hiện trong Cerebrium logs
        print("===== CPU INFO END =====")
        return {"output": result.stdout}
    except subprocess.CalledProcessError as e:
        print("Error running lscpu:", e.stderr)
        return {"error": e.stderr}
