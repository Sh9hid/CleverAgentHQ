from typing import List
from pydantic import BaseModel, Field
from phi.assistant import Assistant
from phi.llm.ollama import Ollama

from phi.assistant import Assistant
from phi.tools.serpapi_tools import SerpApiTools

intern = Assistant(
    name = "intern",
    instruction="Find trending tutorials and tech articles and make a list of the top ones.",
    tool=[SerpApiTools()],
    llm=Ollama(model="llama3:instruct", max_tokens=1024)
)

analyst = Assistant(
    name= "analyst",
    instruction="Make a detailed report individually of each technical article provided to you.",
    tool=[SerpApiTools()],
    llm=Ollama(model="llama3:instruct", max_tokens=1024)
)

assistant = Assistant(
    name="personal assistant",
    description= "Curate and make a short summary and suggest which ones to start with. You have to report to the CEO, that is me. Talk in a professional tone." ,
    tools=[SerpApiTools()],
    team= [intern, analyst],
    show_tool_calls=True,
     llm=Ollama(model="llama3:instruct", max_tokens=1024),
)

assistant.print_response(
   "What's trending in tech?",
    markdown=True
)


