"""Sub Agents - Strands Agents Workshop"""
from strands import Agent, tool
from strands_tools import http_request
from mcp_tools import get_position, wikipedia_search, duckduckgo_search
from model_config import get_configured_model
from typing import Dict, Any


@tool
def search_agent(query: str) -> str:
    """
    Intelligent Search Agent - Information search using Wikipedia and DuckDuckGo
    
    Args:
        query: Search keyword or question
        
    Returns:
        Organized search results as string
    """
    # TODO: Implement in Lab 3
    # Hint:
    # 1. Determine search strategy (Wikipedia vs DuckDuckGo)
    # 2. Attempt first search
    # 3. Perform supplementary search if needed
    # 4. Format results
    pass


@tool
def weather_agent(location: str) -> str:
    """
    Weather Information Specialist Agent - Location-based weather query
    
    Args:
        location: Location to query weather (city name, country name, etc.)
        
    Returns:
        Organized weather information as string
    """
    # TODO: Implement in Lab 3
    # Hint:
    # 1. Query weather information with get_weather()
    # 2. Select emoji based on temperature
    # 3. User-friendly formatting
    # 4. Add weather-based advice
    pass


@tool
def conversation_agent(message: str) -> str:
    """
    General Conversation Specialist Agent - Friendly and helpful conversation
    
    Args:
        message: User's message or question
        
    Returns:
        Friendly response message
    """
    # TODO: Implement in Lab 3
    # Hint:
    # 1. Create conversation specialist agent
    # 2. Friendly and helpful system prompt
    # 3. Use appropriate emojis
    # 4. Error handling and default responses
    pass


# Test code
if __name__ == "__main__":
    print("🧪 Sub Agents Test")
    print("=" * 60)
    
    # TODO: Write test code for each agent in Lab 3
    print("💡 Implement and test in Lab 3!")
    
    # Example:
    # print("\n🔍 Search Agent Test:")
    # result = search_agent("history of artificial intelligence")
    # print(result)
