import os
from dotenv import load_dotenv
load_dotenv()

class LLM_Config:

    @staticmethod
    def get_llmconfig():
        api_key = os.environ.get("API_KEY")
        if not api_key:
            print("Error: API key not found.")
        llm_config = {
            "model": "gpt-4o",
            "api_key": api_key
        }
        return llm_config