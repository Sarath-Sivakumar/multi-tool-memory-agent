from fastapi import FastAPI
from agent import run_agent
from fastapi.middleware.cors import CORSMiddleware


from request_model import UserRequest

app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for learning
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(request: UserRequest):

	return run_agent(
		request.session_id,
		request.message
	)