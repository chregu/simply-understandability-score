from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# Import your functions
from understandability import get_understandability, get_cefr_level  # Replace `your_module` with the actual module name

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

@app.post("/understandability", response_model=UnderstandabilityResponse)
async def get_understandability_endpoint(request: TextRequest):
    try:
        understandability_score = get_understandability(request.text)
        cefr_level = get_cefr_level(understandability_score)
        return UnderstandabilityResponse(
            understandability=understandability_score,
            cefr_level=cefr_level
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) # UVICORN_PORT=8001...