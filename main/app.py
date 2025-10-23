import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def log_lscpu_on_start():
    print("===== RUNNING LSCU =====")
    try:
        # Gọi lscpu và in ra log
        result = subprocess.run(["lscpu"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print("Error running lscpu:", e)
    print("===== END OF LSCU INFO =====")

@app.get("/")
def root():
    return {"message": "App started. Check logs for lscpu info."}

@app.post("/predict")
def predict():
    try:
        result = subprocess.run(["lscpu"], capture_output=True, text=True)
        print("===== LSCU INFO ON REQUEST =====")
        print(result.stdout)
        print("===== END =====")
        return {"output": result.stdout}
    except Exception as e:
        return {"error": str(e)}
