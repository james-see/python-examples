#!/usr/bin/env python3
"""
Anthropic Claude API Example
Demonstrates using the Anthropic API with Claude models.

Requirements:
    pip install anthropic python-dotenv

Setup:
    1. Create a .env file in the project root
    2. Add your Anthropic API key: ANTHROPIC_API_KEY=sk-ant-...
    3. Get your API key at: https://console.anthropic.com/
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Initialize Anthropic client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def simple_message():
    """Basic message example with Claude."""
    print("=" * 60)
    print("1. Simple Message")
    print("=" * 60)
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",  # or "claude-3-opus-20240229", "claude-3-haiku-20240307"
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Explain machine learning in one sentence."}
        ]
    )
    
    print(f"User: Explain machine learning in one sentence.")
    print(f"Claude: {message.content[0].text}\n")
    print(f"Tokens - Input: {message.usage.input_tokens}, Output: {message.usage.output_tokens}")
    print(f"Model: {message.model}\n")


def streaming_response():
    """Stream responses from Claude."""
    print("=" * 60)
    print("2. Streaming Response")
    print("=" * 60)
    
    print("User: Write a haiku about artificial intelligence.\n")
    print("Claude: ", end="", flush=True)
    
    with client.messages.stream(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Write a haiku about artificial intelligence."}
        ]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    print("\n")


def system_prompt():
    """Use system prompts to set Claude's behavior."""
    print("=" * 60)
    print("3. System Prompt")
    print("=" * 60)
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system="You are a helpful Python expert who explains concepts clearly and concisely.",
        messages=[
            {"role": "user", "content": "What is a decorator?"}
        ]
    )
    
    print("System: You are a helpful Python expert...")
    print("User: What is a decorator?")
    print(f"Claude: {message.content[0].text}\n")


def multi_turn_conversation():
    """Demonstrate multi-turn conversations with Claude."""
    print("=" * 60)
    print("4. Multi-turn Conversation")
    print("=" * 60)
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "I'm learning Python. What should I learn first?"},
            {"role": "assistant", "content": "Great! Start with these fundamentals:\n1. Variables and data types\n2. Control flow (if/else, loops)\n3. Functions\n4. Lists and dictionaries\n\nWould you like me to explain any of these?"},
            {"role": "user", "content": "Yes, explain functions please."}
        ]
    )
    
    print("User: I'm learning Python. What should I learn first?")
    print("Claude: [previous response about fundamentals]")
    print("\nUser: Yes, explain functions please.")
    print(f"Claude: {message.content[0].text}\n")


def with_vision():
    """Use Claude's vision capabilities (if using a vision-enabled model)."""
    print("=" * 60)
    print("5. Vision Example (Placeholder)")
    print("=" * 60)
    
    # Note: This requires an image URL or base64 encoded image
    print("Claude supports vision! You can send images like this:")
    print("""
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "url",
                            "url": "https://example.com/image.jpg"
                        }
                    },
                    {
                        "type": "text",
                        "text": "What's in this image?"
                    }
                ]
            }
        ]
    )
    """)
    print()


def thinking_mode():
    """Demonstrate extended thinking for complex problems."""
    print("=" * 60)
    print("6. Complex Reasoning")
    print("=" * 60)
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        temperature=1.0,
        messages=[
            {
                "role": "user",
                "content": "Solve this logic puzzle: There are 3 boxes. One contains only apples, one contains only oranges, and one contains both. All boxes are labeled incorrectly. You can pick one fruit from one box. How do you correctly label all boxes?"
            }
        ]
    )
    
    print("User: [Logic puzzle about mislabeled fruit boxes]")
    print(f"Claude: {message.content[0].text}\n")


def with_prefill():
    """Use prefill to guide Claude's response format."""
    print("=" * 60)
    print("7. Response Prefill")
    print("=" * 60)
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "What are the three laws of robotics?"},
            {"role": "assistant", "content": "The Three Laws of Robotics are:\n\n1."}
        ]
    )
    
    print("User: What are the three laws of robotics?")
    print(f"Claude: The Three Laws of Robotics are:\n\n1.{message.content[0].text}\n")


def error_handling():
    """Demonstrate error handling with Anthropic API."""
    print("=" * 60)
    print("8. Error Handling")
    print("=" * 60)
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            messages=[
                {"role": "user", "content": "Hello Claude!"}
            ]
        )
        print(f"✓ Success: {message.content[0].text}\n")
        
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}")
        print(f"  Message: {str(e)}\n")


if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key.")
        print("Example: ANTHROPIC_API_KEY=sk-ant-...")
        exit(1)
    
    print("\n" + "=" * 60)
    print("Anthropic Claude API Examples")
    print("=" * 60 + "\n")
    
    try:
        simple_message()
        streaming_response()
        system_prompt()
        multi_turn_conversation()
        with_vision()
        thinking_mode()
        with_prefill()
        error_handling()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error running examples: {e}")
        print("Make sure your ANTHROPIC_API_KEY is valid and you have credits.")
