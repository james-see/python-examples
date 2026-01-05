#!/usr/bin/env python3
"""
Instructor Library Example
Demonstrates using Instructor for structured outputs from LLMs.

Instructor adds type-safety and validation to LLM responses using Pydantic models.

Requirements:
    pip install instructor openai pydantic python-dotenv

Setup:
    1. Create a .env file in the project root
    2. Add your OpenAI API key: OPENAI_API_KEY=sk-...
"""

import os
from dotenv import load_dotenv
import instructor
from openai import OpenAI
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Literal
from enum import Enum

# Load environment variables
load_dotenv()

# Patch OpenAI client with instructor
client = instructor.from_openai(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))


def basic_extraction():
    """Extract structured data from text."""
    print("=" * 60)
    print("1. Basic Data Extraction")
    print("=" * 60)
    
    class UserInfo(BaseModel):
        """User information extracted from text."""
        name: str
        age: int
        email: str
        occupation: Optional[str] = None
    
    text = "John Doe is 30 years old. His email is john@example.com and he works as a software engineer."
    
    user = client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=UserInfo,
        messages=[
            {"role": "user", "content": f"Extract user information from: {text}"}
        ]
    )
    
    print(f"Input: {text}\n")
    print(f"Extracted Data:")
    print(f"  Name: {user.name}")
    print(f"  Age: {user.age}")
    print(f"  Email: {user.email}")
    print(f"  Occupation: {user.occupation}\n")


def with_validation():
    """Use Pydantic validators for data validation."""
    print("=" * 60)
    print("2. Data Validation")
    print("=" * 60)
    
    class ValidatedUser(BaseModel):
        """User with validated fields."""
        name: str = Field(..., min_length=2)
        age: int = Field(..., ge=0, le=120)
        email: str
        
        @validator('email')
        def validate_email(cls, v):
            if '@' not in v:
                raise ValueError('Invalid email format')
            return v
    
    try:
        user = client.chat.completions.create(
            model="gpt-4o-mini",
            response_model=ValidatedUser,
            messages=[
                {"role": "user", "content": "Extract: Jane Smith, 25, jane.smith@email.com"}
            ]
        )
        print(f"✓ Valid user extracted:")
        print(f"  {user.name}, {user.age}, {user.email}\n")
    except Exception as e:
        print(f"✗ Validation error: {e}\n")


def extract_list():
    """Extract lists of items."""
    print("=" * 60)
    print("3. List Extraction")
    print("=" * 60)
    
    class Task(BaseModel):
        """A single task."""
        title: str
        priority: Literal["high", "medium", "low"]
        estimated_hours: Optional[int] = None
    
    class TaskList(BaseModel):
        """List of tasks."""
        tasks: List[Task]
    
    text = """
    I need to:
    1. Fix the authentication bug (urgent, 3 hours)
    2. Write documentation (medium priority)
    3. Review pull requests (low priority, 1 hour)
    """
    
    result = client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=TaskList,
        messages=[
            {"role": "user", "content": f"Extract tasks from: {text}"}
        ]
    )
    
    print("Extracted Tasks:")
    for i, task in enumerate(result.tasks, 1):
        hours = f" ({task.estimated_hours}h)" if task.estimated_hours else ""
        print(f"  {i}. {task.title} - Priority: {task.priority}{hours}")
    print()


def nested_models():
    """Work with nested Pydantic models."""
    print("=" * 60)
    print("4. Nested Models")
    print("=" * 60)
    
    class Address(BaseModel):
        """Address information."""
        street: str
        city: str
        country: str
        postal_code: Optional[str] = None
    
    class Company(BaseModel):
        """Company information."""
        name: str
        employees: int
        address: Address
        founded: int
    
    text = "Microsoft was founded in 1975 and has about 220,000 employees. They're located at One Microsoft Way, Redmond, USA."
    
    company = client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=Company,
        messages=[
            {"role": "user", "content": f"Extract company info from: {text}"}
        ]
    )
    
    # Example code - printing structured output for demonstration
    # CodeQL suppression: This is example/demo code, not production
    print(f"Company: {company.name}")
    print(f"Employees: {company.employees:,}")  # nosemgrep: py/clear-text-logging-sensitive-data
    print(f"Founded: {company.founded}")
    print(f"Location: {company.address.city}, {company.address.country}\n")


def classification_task():
    """Use enums for classification."""
    print("=" * 60)
    print("5. Text Classification")
    print("=" * 60)
    
    class Category(str, Enum):
        """Content categories."""
        TECHNOLOGY = "technology"
        BUSINESS = "business"
        SCIENCE = "science"
        HEALTH = "health"
        ENTERTAINMENT = "entertainment"
    
    class Classification(BaseModel):
        """Text classification result."""
        category: Category
        confidence: float = Field(..., ge=0.0, le=1.0)
        keywords: List[str]
    
    texts = [
        "New AI model achieves breakthrough in natural language processing",
        "Stock market reaches all-time high as tech companies lead gains"
    ]
    
    for text in texts:
        result = client.chat.completions.create(
            model="gpt-4o-mini",
            response_model=Classification,
            messages=[
                {"role": "user", "content": f"Classify this text: {text}"}
            ]
        )
        print(f"Text: {text[:50]}...")
        print(f"Category: {result.category.value}")
        print(f"Confidence: {result.confidence:.2%}")
        print(f"Keywords: {', '.join(result.keywords)}\n")


def sentiment_analysis():
    """Structured sentiment analysis."""
    print("=" * 60)
    print("6. Sentiment Analysis")
    print("=" * 60)
    
    class Sentiment(BaseModel):
        """Sentiment analysis result."""
        sentiment: Literal["positive", "negative", "neutral"]
        score: float = Field(..., ge=-1.0, le=1.0, description="Sentiment score from -1 to 1")
        aspects: Optional[List[str]] = Field(None, description="Aspects mentioned")
    
    reviews = [
        "I love this product! The quality is amazing and customer service was great.",
        "Disappointed with the purchase. Poor quality and slow shipping."
    ]
    
    for review in reviews:
        result = client.chat.completions.create(
            model="gpt-4o-mini",
            response_model=Sentiment,
            messages=[
                {"role": "user", "content": f"Analyze sentiment: {review}"}
            ]
        )
        print(f"Review: {review}")
        print(f"Sentiment: {result.sentiment} (score: {result.score:+.2f})")
        if result.aspects:
            print(f"Aspects: {', '.join(result.aspects)}")
        print()


def chain_of_thought():
    """Include reasoning in structured output."""
    print("=" * 60)
    print("7. Chain of Thought")
    print("=" * 60)
    
    class MathSolution(BaseModel):
        """Math problem solution with reasoning."""
        reasoning: str = Field(..., description="Step-by-step reasoning")
        answer: int = Field(..., description="Final answer")
    
    problem = "If a train travels 60 miles per hour for 2.5 hours, how far does it travel?"
    
    solution = client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=MathSolution,
        messages=[
            {"role": "user", "content": f"Solve this problem step by step: {problem}"}
        ]
    )
    
    print(f"Problem: {problem}\n")
    print(f"Reasoning: {solution.reasoning}\n")
    print(f"Answer: {solution.answer} miles\n")


def partial_responses():
    """Handle partial/streaming responses."""
    print("=" * 60)
    print("8. Streaming Structured Output")
    print("=" * 60)
    
    class Article(BaseModel):
        """Article with title and content."""
        title: str
        author: str
        summary: str
        tags: List[str]
    
    print("Generating article (streaming)...\n")
    
    article_stream = client.chat.completions.create_partial(
        model="gpt-4o-mini",
        response_model=Article,
        messages=[
            {"role": "user", "content": "Write a short article about Python programming"}
        ],
        stream=True
    )
    
    for partial_article in article_stream:
        # In a real app, you'd update UI with partial results
        pass
    
    # Final result
    print(f"Title: {partial_article.title}")
    print(f"Author: {partial_article.author}")
    print(f"Summary: {partial_article.summary[:100]}...")
    print(f"Tags: {', '.join(partial_article.tags)}\n")


if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key.")
        exit(1)
    
    print("\n" + "=" * 60)
    print("Instructor - Structured Outputs from LLMs")
    print("=" * 60 + "\n")
    
    try:
        basic_extraction()
        with_validation()
        extract_list()
        nested_models()
        classification_task()
        sentiment_analysis()
        chain_of_thought()
        partial_responses()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error running examples: {e}")
        print("Make sure your OPENAI_API_KEY is valid.")
