from fastapi import FastAPI

app = FastAPI()

hr = []


@app.get("/")
async def api_status():
    return {"message": "api running"}


@app.get("/hr")
async def show_hr_values():
    if hr:
        return hr
    return {"message": "hr empty"}


@app.post("/hr/{hr_value}")
async def add_hr_value(hr_value: int):
    hr.append(hr_value)
    return {"message": f"hr = {hr_value} added"}