from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )