
from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from phi.tools.hackernews import HackerNews

# Create instances of the Assistant
story_researcher = Assistant(
    name="HackerNews Story Researcher",
    role="Researches hackernews stories and users.",
    tools=[HackerNews()],
    llm=Ollama(model="llama3:instruct", max_tokens=1024)
)

user_researcher = Assistant(
    name="HackerNews User Researcher",
    role="Reads articles from URLs.",
    tools=[HackerNews()],
    llm=Ollama(model="llama3:instruct", max_tokens=1024)
)

hn_assistant = Assistant(
    name="Hackernews Team",
    team=[story_researcher, user_researcher],
    llm=Ollama(model="llama3:instruct", max_tokens=1024)
)

hn_assistant.print_response(
    "Write a report about the users with the top 2 stories on hackernews", markdown=True
)
