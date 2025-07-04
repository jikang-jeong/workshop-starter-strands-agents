"""Sub Agents - Strands Agents Workshop"""
from strands import Agent, tool
from strands_tools import http_request
from mcp_tools import get_position, wikipedia_search, duckduckgo_search
from model_config import get_configured_model
from typing import Dict, Any
SEARCH_AGENT_PROMPT = """
You are an intelligent search specialist agent.
Analyze user search requests and select the most appropriate search tool to use.

 Search Tool Selection Strategy:

1. **WIKIPEDIA Priority Use Cases:**
   - Historical facts, people, regions, country information
   - Scientific concepts, academic content
   - Comprehensive explanations of well-established topics
   - Examples: "Einstein", "France", "quantum mechanics", "Renaissance"

2. **DUCKDUCKGO Priority Use Cases:**
   - Technical term definitions, programming concepts
   - Latest trends, modern topics
   - Cases requiring simple definitions or explanations
   - Examples: "What is API", "machine learning definition", "React framework"

3. **Selection Principles:**
   - First use only one tool for searching
   - Use additional tools only if results are insufficient or failed
   - Using both tools should be a last resort

After searching, analyze the results to summarize them in an easy-to-understand way for users, and specify which search tool was used.
"""

@tool
def search_agent(query: str) -> str:
    """
    Optimized information search agent through intelligent search tool selection

    Args:
        query: Content to search for

    Returns:
        Optimized answer through selected search tool
    """
    try:
        model = get_configured_model()
        agent = Agent(
            model=model,
            system_prompt=SEARCH_AGENT_PROMPT,
            tools=[wikipedia_search, duckduckgo_search]
        )
        
        response = agent(f"다음 검색 요청을 처리해주세요: {query}")
        return str(response)
        
    except Exception as e:
        return f"검색 에이전트 오류: {str(e)}"
# Weather Agent - 위치 기반 날씨 정보
WEATHER_AGENT_PROMPT = """You are a weather assistant with HTTP capabilities. You can:

1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States

When retrieving weather information:
1. First get the coordinates using get_position tool if needed
2. Then get the grid information using https://api.weather.gov/points/{latitude},{longitude}
3. Finally use the returned forecast URL to get the actual forecast

When displaying responses:
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language

Always explain the weather conditions clearly and provide context for the forecast.
"""

@tool 
def weather_agent(location: str) -> str:
    """
    Weather information agent using National Weather Service API

    Args:
        location: Location to get weather for

    Returns:
        Formatted weather information
    """
    try:
        model = get_configured_model()
        agent = Agent(
            model=model,
            system_prompt=WEATHER_AGENT_PROMPT,
            tools=[get_position, http_request]  # 가이드 문서와 동일
        )

        response = agent(f"What's the weather like in {location}?")
        return str(response)

    except Exception as e:
        return f"Weather agent error: {str(e)}"

# Conversation Agent - 일반 대화 처리
CONVERSATION_AGENT_PROMPT = """
You are a friendly and helpful conversation specialist agent.

Characteristics:
- Communicate with a warm and friendly tone
- Understand and empathize with users' emotions
- Use appropriate emojis to enhance expressiveness
- Provide concise yet meaningful responses

Approach by conversation type:
- Greetings: Warmly acknowledge greetings
- Emotional expressions: Show empathy and respond appropriately
- General questions: Provide helpful answers
- Thank you messages: Accept graciously

Guidelines:
- For questions requiring search or weather information, guide users that other agents will handle them
- Keep responses brief, 2-3 sentences maximum
- Maintain natural and human-like conversation
"""

@tool
def conversation_agent(message: str) -> str:
    """
    General conversation handling agent

    Args:
        message: User message

    Returns:
        Conversation response
    """ 
    model = get_configured_model()
    agent = Agent(
        model=model,
        system_prompt=CONVERSATION_AGENT_PROMPT,
        tools=[]
    )
    
    response = agent(message)
    return str(response)

 
# 테스트 코드 (파일 하단에 추가)
if __name__ == "__main__":
    print("🧪 sub agent test..")
    print("=" * 60)
    
    # Search Agent 테스트
    print("\n🔍 Search Agent test:")
    print("-" * 30)
    search_result = search_agent("Artifical Intelligent")
    print(search_result[:200] + "..." if len(search_result) > 200 else search_result)
    
    # Weather Agent 테스트  
    print("\n🌤️ Weather Agent test:")
    print("-" * 30)
    weather_result = weather_agent("newyork")
    print(weather_result[:200] + "..." if len(weather_result) > 200 else weather_result)
    
    # Conversation Agent 테스트
    print("\n💬 Conversation Agent test:")
    print("-" * 30)
    conversation_result = conversation_agent("hello. good morning?!")
    print(conversation_result)
    
    print("\n" + "=" * 60)
    print("✅ complete!")
