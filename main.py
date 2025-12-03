from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# Import your functions
from understandability import get_understandability, get_cefr_level  # Replace `your_module` with the actual module name
from zix.understandability import get_zix, get_cefr
import textstat       # Load the library

app = FastAPI()
# Set up CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class TextRequest(BaseModel):
    text: str

class UnderstandabilityResponse(BaseModel):
    understandability: float
    cefr_level: str
    flesch: float

# OPTIONS handlers for CORS preflight
@app.options("/understandability")
async def options_understandability(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return {}

# old way extracted from original repo
@app.post("/understandability", response_model=UnderstandabilityResponse)
async def get_understandability_endpoint(request: TextRequest):
    try:
        flesch = textstat.flesch_reading_ease(request.text)  # Use textstat to get Flesch score
        understandability_score = get_understandability(request.text)
        cefr_level = get_cefr_level(understandability_score)
        return UnderstandabilityResponse(
            understandability=understandability_score,
            cefr_level=cefr_level,
            flesch=flesch
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.options("/zix")
async def options_zix(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return {}

# new way from ZIX project
@app.post("/zix", response_model=UnderstandabilityResponse)
async def get_understandability_endpoint(request: TextRequest):
    try:
        flesch = textstat.flesch_reading_ease(request.text)  # Use textstat to get Flesch score
        understandability_score = get_zix(request.text)
        cefr_level = get_cefr(understandability_score)
        return UnderstandabilityResponse(
            understandability=understandability_score,
            cefr_level=cefr_level,
            flesch=flesch
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) # UVICORN_PORT=8001...