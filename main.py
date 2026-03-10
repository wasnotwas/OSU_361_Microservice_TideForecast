import httpx
from fastapi import FastAPI, HTTPException

NOAA_BASE_URL = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"

app = FastAPI()

@app.get("/")
def root_message():
    return {"Server is running"}

@app.get("/tides/{station_id}")
async def get_tide_forecast(station_id: str):
    """
    Fetch today's high/low tide predictions for a given NOAA station ID.
    Example: /tides/8557863
    """
    params = {
        "date": "today",
        "station": station_id,
        "product": "predictions",
        "datum": "MLLW",
        "time_zone": "lst_ldt",
        "interval": "hilo",
        "units": "english",
        "application": "student_project_OSU",
        "format": "json",
    }

    print(params)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(NOAA_BASE_URL, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail=f"Error contacting NOAA API: {str(e)}")

    data = response.json()

    # Error message created if the user passes an invalid station
    if "error" in data:
        raise HTTPException(status_code=400, detail=data["error"].get("message", "NOAA API error"))

    return data

# run this code as a standalone FastApi server from directly from Python
if __name__ == '__main__':
    # import FastAPI web server
    import uvicorn

    # launch this file in web server
    uvicorn.run(app)