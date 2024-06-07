import streamlit as st
from typing import List
from pydantic import BaseModel, Field
from phi.assistant import Assistant
from phi.llm.ollama import Ollama

class YoutubeTeam(BaseModel):
    setting: str = Field(..., description="Provide a nice setting for a viral inspiring-youtube-video.")
    ending: str = Field(..., description="Ending of the video. If not available, provide an inspiring ending.")
    genre: str = Field(..., description="Genre of the movie. If not available, select awe, emotional or imspiring.")
    name: str = Field(..., description="Suggest a viral title for the video")
    characters: List[str] = Field(..., description="Give a description of how this betters the audience")
    storyline: str = Field(..., description="3 sentence storyline for the video. Make it exciting!")

youtube_team = Assistant(
    description="You help write youtube scripts.",
    output_model=YoutubeTeam,
    llm=Ollama(model="llama3:instruct", max_tokens=1024)
)

query = "10,000hours Rule" # TO DO: create a streamlit-app
pprint(youtube_team.run(query))
