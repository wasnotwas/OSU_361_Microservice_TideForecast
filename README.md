# Tide Forecast Microservice
Allows surfers and commercial fishers to use tide data to improve their work. 

## API Specification
This API accepts one parameter, the Station ID. This is a NOAA Weather station. You can find a list of all station IDs here: https://tidesandcurrents.noaa.gov/. The API will return the high and low tide data for the next 24 hours at that station. 
- The 't' is the time returned is local standard time corrected for Daylight Savings time.
- The 'v' is the height is measured in feet.
- The 'type' is either "H" for high tide or "L" for low tide

#### Request Example
```
GET /tides/8557863
```

#### Response Example in JSON
```JSON
{
  "predictions": [
    {
      "t": "2026-03-10 01:02",
      "v": "3.61",
      "type": "H"
    },
    {
      "t": "2026-03-10 07:27",
      "v": "0.869",
      "type": "L"
    },
    {
      "t": "2026-03-10 13:20",
      "v": "2.695",
      "type": "H"
    },
    {
      "t": "2026-03-10 19:22",
      "v": "0.719",
      "type": "L"
    }
  ]
}
```
