import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    try:
        # Chạy lệnh lscpu và lấy output
        result = subprocess.run(["lscpu"], capture_output=True, text=True, check=True)
        return {"cpu_info": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr}
