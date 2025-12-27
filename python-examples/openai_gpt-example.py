#!/usr/bin/env python3
"""
OpenAI GPT API Example
Demonstrates using the OpenAI API with GPT models for various tasks.

Requirements:
    pip install openai python-dotenv

Setup:
    1. Create a .env file in the project root
    2. Add your OpenAI API key: OPENAI_API_KEY=sk-...
    3. Get your API key at: https://platform.openai.com/api-keys
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def simple_chat_completion():
    """Basic chat completion example."""
    print("=" * 60)
    print("1. Simple Chat Completion")
    print("=" * 60)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4", "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain quantum computing in one sentence."}
        ],
        temperature=0.7,
        max_tokens=150
    )
    
    answer = response.choices[0].message.content
    print(f"User: Explain quantum computing in one sentence.")
    print(f"Assistant: {answer}\n")
    print(f"Tokens used: {response.usage.total_tokens}")
    print(f"Model: {response.model}\n")


def streaming_response():
    """Stream responses token by token."""
    print("=" * 60)
    print("2. Streaming Response")
    print("=" * 60)
    
    print("User: Write a haiku about Python programming.\n")
    print("Assistant: ", end="", flush=True)
    
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Write a haiku about Python programming."}
        ],
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")


def function_calling():
    """Demonstrate function calling (tool use)."""
    print("=" * 60)
    print("3. Function Calling")
    print("=" * 60)
    
    # Define a function schema
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA"
                        },
                        "unit": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "The temperature unit"
                        }
                    },
                    "required": ["location"]
                }
            }
        }
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "What's the weather like in Boston?"}
        ],
        tools=tools,
        tool_choice="auto"
    )
    
    message = response.choices[0].message
    
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        print(f"User: What's the weather like in Boston?")
        print(f"\nGPT wants to call function: {tool_call.function.name}")
        print(f"Arguments: {tool_call.function.arguments}\n")
    else:
        print(f"Response: {message.content}\n")


def system_prompt_example():
    """Show how system prompts affect behavior."""
    print("=" * 60)
    print("4. System Prompt Example")
    print("=" * 60)
    
    prompts = [
        ("You are a pirate. Respond in pirate speak.", "How do I write Python code?"),
        ("You are a Shakespeare scholar. Use Elizabethan English.", "How do I write Python code?"),
    ]
    
    for system_msg, user_msg in prompts:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg}
            ],
            max_tokens=100,
            temperature=0.8
        )
        
        print(f"System: {system_msg}")
        print(f"User: {user_msg}")
        print(f"Assistant: {response.choices[0].message.content}\n")


def conversation_with_history():
    """Maintain conversation context."""
    print("=" * 60)
    print("5. Multi-turn Conversation")
    print("=" * 60)
    
    messages = [
        {"role": "system", "content": "You are a helpful Python programming tutor."}
    ]
    
    conversation = [
        "What is a list comprehension?",
        "Can you show me an example?",
        "How is it different from a regular for loop?"
    ]
    
    for user_input in conversation:
        messages.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=150
        )
        
        assistant_message = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_message})
        
        print(f"User: {user_input}")
        print(f"Assistant: {assistant_message}\n")


def with_json_mode():
    """Use JSON mode for structured outputs."""
    print("=" * 60)
    print("6. JSON Mode")
    print("=" * 60)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that outputs JSON."
            },
            {
                "role": "user",
                "content": "Extract the following information in JSON format: Name: John Doe, Age: 30, City: New York"
            }
        ],
        response_format={"type": "json_object"},
        temperature=0
    )
    
    print("User: Extract information from: Name: John Doe, Age: 30, City: New York")
    print(f"Assistant (JSON): {response.choices[0].message.content}\n")


def error_handling():
    """Demonstrate error handling."""
    print("=" * 60)
    print("7. Error Handling")
    print("=" * 60)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Hello!"}
            ],
            max_tokens=50
        )
        print(f"✓ Success: {response.choices[0].message.content}\n")
        
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}")
        print(f"  Message: {str(e)}\n")


if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key.")
        print("Example: OPENAI_API_KEY=sk-...")
        exit(1)
    
    print("\n" + "=" * 60)
    print("OpenAI GPT API Examples")
    print("=" * 60 + "\n")
    
    try:
        simple_chat_completion()
        streaming_response()
        function_calling()
        system_prompt_example()
        conversation_with_history()
        with_json_mode()
        error_handling()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error running examples: {e}")
        print("Make sure your OPENAI_API_KEY is valid and you have credits.")
