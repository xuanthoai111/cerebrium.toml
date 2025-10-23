import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def log_lscpu_on_start():
    try:
        result = subprocess.run(["lscpu"], capture_output=True, text=True, check=True)
        print("===== LSCU INFO AT STARTUP =====")
        print(result.stdout)
        print("===== END OF LSCU INFO =====")
    except Exception as e:
        print("Error running lscpu:", e)

@app.get("/")
def root():
    return {"message": "App started. Check logs for CPU info."}
