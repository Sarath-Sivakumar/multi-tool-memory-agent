import ollama
import os

from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT
from tools import get_weather, get_current_time, calculate
from memory import get_memory, save_memory

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")


def run_agent(session_id, user_message):

    memory = get_memory(session_id)

    conversation_context = "\n".join(memory)

    prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{conversation_context}

Current User Question:
{user_message}
"""

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    agent_output = response["message"]["content"]

    lines = agent_output.split("\n")

    action = ""
    action_input = ""

    for line in lines:

        if line.startswith("ACTION:"):
            action = line.replace("ACTION:", "").strip()

        if line.startswith("ACTION_INPUT:"):
            action_input = line.replace("ACTION_INPUT:", "").strip()

    observation = ""

    if action == "weather":
        observation = get_weather(action_input)

    elif action == "calculator":
        observation = calculate(action_input)

    elif action == "time":
        observation = get_current_time()

    else:
        observation = "No tool selected"

    final_prompt = f"""
Conversation History:
{conversation_context}

User Question:
{user_message}

Tool Observation:
{observation}

Generate final helpful response.
"""

    final_response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    final_answer = final_response["message"]["content"]

    save_memory(session_id, f"User: {user_message}")
    save_memory(session_id, f"Agent: {final_answer}")

    return {
        "memory": memory,
        "tool_used": action,
        "observation": observation,
        "final_answer": final_answer
    }