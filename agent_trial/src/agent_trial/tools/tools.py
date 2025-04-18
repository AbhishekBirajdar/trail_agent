from crewai_tools import YoutubeChannelSearchTool
from dotenv import load_dotenv
import os

def load_my_tool():
    load_dotenv()
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"
    return YoutubeChannelSearchTool(youtube_channel_name='@Footballia')
