"""MCP Tools - Strands Agents Workshop"""
import httpx
import wikipedia
import asyncio
import json
from typing import Dict, Any
from strands import tool

@tool
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

@tool
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

@tool
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
 

@tool
def get_weather_forecast(latitude: float, longitude: float) -> Dict[str, Any]:
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
