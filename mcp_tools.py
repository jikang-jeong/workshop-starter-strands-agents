"""MCP Tools - Strands Agents Workshop"""
import json
import httpx
import wikipedia
from typing import Dict, Any, Optional


def wikipedia_search(query: str) -> Dict[str, Any]:
    """
    Search for information on Wikipedia.
    
    Args:
        query: Search keyword
        
    Returns:
        Dictionary containing search results
    """
    # TODO: Implement in Lab 2
    # Hint: Use wikipedia.set_lang(), wikipedia.page()
    pass


def duckduckgo_search(query: str) -> Dict[str, Any]:
    """
    Search for real-time information on DuckDuckGo.
    
    Args:
        query: Search keyword
        
    Returns:
        Dictionary containing search results
    """
    # TODO: Implement in Lab 2
    # Hint: Use DuckDuckGo Instant Answer API
    # URL: https://api.duckduckgo.com/
    pass


def get_position(location: str) -> Dict[str, Any]:
    """
    Convert location name to latitude/longitude coordinates.
    
    Args:
        location: Location name (e.g., "Seoul", "New York")
        
    Returns:
        Dictionary containing location information
    """
    # TODO: Implement in Lab 2
    # Hint: Use OpenStreetMap Nominatim API
    # URL: https://nominatim.openstreetmap.org/search
    pass


def get_weather(location: str) -> Dict[str, Any]:
    """
    Query weather information for the specified location.
    
    Args:
        location: Location name
        
    Returns:
        Dictionary containing weather information
    """
    # TODO: Implement in Lab 2
    # Hint: 
    # 1. Get location coordinates with get_position()
    # 2. Query weather information with Open-Meteo API
    # URL: https://api.open-meteo.com/v1/forecast
    pass


# Test code
if __name__ == "__main__":
    print("🧪 MCP Tools Test")
    print("=" * 50)
    
    # TODO: Write test code for each function in Lab 2
    print("💡 Implement and test in Lab 2!")
    
    # Example:
    # print("\n📚 Wikipedia Search Test:")
    # result = wikipedia_search("artificial intelligence")
    # print(f"Success: {result.get('success', False)}")
