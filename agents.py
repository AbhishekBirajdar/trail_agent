from crewai import Agent
from tools import load_my_tool
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

llm = ChatOpenAI(model=os.environ["OPENAI_MODEL_NAME"])

my_tool = load_my_tool()

# Blog researcher agent
blog_researcher = Agent(
    role='Blog Researcher for YouTube videos',
    goal='Get the relevant video for the topic {topic} from the YouTube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning, and GenAI, and providing suggestions."
    ),
    tools=[my_tool],
    llm=llm,
    allow_delegation=True
)

# Blog writer agent
blog_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about the video {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[my_tool],
    llm=llm,
    allow_delegation=False
)
