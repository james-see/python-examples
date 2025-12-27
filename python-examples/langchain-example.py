#!/usr/bin/env python3
"""
LangChain Framework Example
Demonstrates using LangChain for building LLM applications.

Requirements:
    pip install langchain langchain-openai langchain-community python-dotenv

Setup:
    1. Create a .env file in the project root
    2. Add your OpenAI API key: OPENAI_API_KEY=sk-...
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

# Load environment variables
load_dotenv()


def basic_llm_call():
    """Simple LLM call with LangChain."""
    print("=" * 60)
    print("1. Basic LLM Call")
    print("=" * 60)
    
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content="What is LangChain?")
    ]
    
    response = llm.invoke(messages)
    print(f"User: What is LangChain?")
    print(f"Assistant: {response.content}\n")


def prompt_template_example():
    """Use prompt templates for reusable prompts."""
    print("=" * 60)
    print("2. Prompt Templates")
    print("=" * 60)
    
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    
    template = ChatPromptTemplate.from_messages([
        ("system", "You are a {expertise} expert."),
        ("human", "{question}")
    ])
    
    chain = template | llm
    
    result = chain.invoke({
        "expertise": "Python programming",
        "question": "What is a decorator?"
    })
    
    print("Template: You are a {expertise} expert.")
    print("Question: What is a decorator?")
    print(f"Response: {result.content}\n")


def conversation_with_memory():
    """Maintain conversation memory."""
    print("=" * 60)
    print("3. Conversation Memory")
    print("=" * 60)
    
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    
    memory = ConversationBufferMemory(return_messages=True)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful coding assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    conversation = [
        "What is a list comprehension in Python?",
        "Show me an example",
        "How is it different from a map function?"
    ]
    
    for user_input in conversation:
        # Get chat history
        history = memory.load_memory_variables({})
        
        # Create chain
        chain = prompt | llm
        
        # Get response
        response = chain.invoke({
            "history": history.get("history", []),
            "input": user_input
        })
        
        # Save to memory
        memory.save_context({"input": user_input}, {"output": response.content})
        
        print(f"User: {user_input}")
        print(f"Assistant: {response.content[:200]}...\n")


def structured_output_parsing():
    """Parse LLM output into structured data."""
    print("=" * 60)
    print("4. Structured Output Parsing")
    print("=" * 60)
    
    # Define output structure
    class Recipe(BaseModel):
        """Recipe information."""
        name: str = Field(description="Name of the dish")
        ingredients: List[str] = Field(description="List of ingredients")
        steps: List[str] = Field(description="Cooking steps")
        prep_time: int = Field(description="Preparation time in minutes")
    
    # Set up parser
    parser = PydanticOutputParser(pydantic_object=Recipe)
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful cooking assistant."),
        ("human", "{query}\n\n{format_instructions}")
    ])
    
    chain = prompt | llm | parser
    
    result = chain.invoke({
        "query": "Give me a simple pasta recipe",
        "format_instructions": parser.get_format_instructions()
    })
    
    print("Query: Give me a simple pasta recipe\n")
    print(f"Recipe Name: {result.name}")
    print(f"Prep Time: {result.prep_time} minutes")
    print(f"Ingredients: {', '.join(result.ingredients[:3])}...")
    print(f"Steps: {len(result.steps)} steps\n")


def simple_rag_example():
    """Simple Retrieval-Augmented Generation example."""
    print("=" * 60)
    print("5. Simple RAG Pattern")
    print("=" * 60)
    
    # Simulate document retrieval
    documents = [
        "LangChain is a framework for developing applications powered by language models.",
        "It enables applications that are context-aware and can reason based on provided context.",
        "LangChain provides components for working with LLMs, prompts, memory, and agents."
    ]
    
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    
    # Create RAG prompt
    rag_prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer the question based on the following context:\n\n{context}"),
        ("human", "{question}")
    ])
    
    chain = rag_prompt | llm
    
    question = "What does LangChain enable?"
    context = "\n".join(documents)
    
    response = chain.invoke({
        "context": context,
        "question": question
    })
    
    print(f"Context: [3 documents about LangChain]")
    print(f"Question: {question}")
    print(f"Answer: {response.content}\n")


def few_shot_prompting():
    """Demonstrate few-shot learning with examples."""
    print("=" * 60)
    print("6. Few-Shot Prompting")
    print("=" * 60)
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))
    
    few_shot_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a sentiment classifier. Respond with only: positive, negative, or neutral."),
        ("human", "I love this product!"),
        ("ai", "positive"),
        ("human", "This is terrible."),
        ("ai", "negative"),
        ("human", "It's okay, nothing special."),
        ("ai", "neutral"),
        ("human", "{text}")
    ])
    
    chain = few_shot_prompt | llm
    
    test_cases = [
        "This is amazing!",
        "I'm disappointed.",
        "It works as expected."
    ]
    
    print("Few-shot sentiment classification:\n")
    for text in test_cases:
        result = chain.invoke({"text": text})
        print(f"Text: '{text}'")
        print(f"Sentiment: {result.content}\n")


def chain_multiple_calls():
    """Chain multiple LLM calls together."""
    print("=" * 60)
    print("7. Sequential Chains")
    print("=" * 60)
    
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    
    # First chain: Generate a topic
    topic_prompt = ChatPromptTemplate.from_messages([
        ("system", "Generate a random technical topic in one word."),
        ("human", "Give me a topic")
    ])
    
    # Second chain: Explain the topic
    explain_prompt = ChatPromptTemplate.from_messages([
        ("system", "Explain the following topic in one sentence."),
        ("human", "{topic}")
    ])
    
    topic_chain = topic_prompt | llm
    explain_chain = explain_prompt | llm
    
    # Execute chains
    topic_response = topic_chain.invoke({})
    topic = topic_response.content.strip()
    
    explanation = explain_chain.invoke({"topic": topic})
    
    print(f"Generated Topic: {topic}")
    print(f"Explanation: {explanation.content}\n")


if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key.")
        exit(1)
    
    print("\n" + "=" * 60)
    print("LangChain Examples")
    print("=" * 60 + "\n")
    
    try:
        basic_llm_call()
        prompt_template_example()
        conversation_with_memory()
        structured_output_parsing()
        simple_rag_example()
        few_shot_prompting()
        chain_multiple_calls()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error running examples: {e}")
        print("Make sure your OPENAI_API_KEY is valid.")
