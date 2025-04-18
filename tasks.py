from crewai import Task
from agents import blog_researcher, blog_writer
from tools import load_my_tool

my_tool = load_my_tool()

# Research task
research_task = Task(
    description="Identify the video {topic}. Get detailed information about the video from the YouTube channel.",
    expected_output="A comprehensive 3-paragraph long report based on the {topic} of video content.",
    tools=[my_tool],
    agent=blog_researcher,
)

# Write task
write_task = Task(
    description="Get the info from the YouTube channel on the topic {topic}.",
    expected_output="Summarize the info from the YouTube channel video on the topic {topic} and create the content for the blog.",
    tools=[my_tool],
    agent=blog_writer,
    aysnc_execution=False,
    output_file='new-blog-md'
)
