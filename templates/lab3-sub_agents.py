"""Sub Agents - Agents as Tools 패턴을 위한 하위 에이전트들"""
from strands import Agent, tool
from strands_tools import http_request
from mcp_tools import get_position, wikipedia_search, duckduckgo_search
from model_config import get_configured_model
from typing import Dict, Any


# Search Agent - 지능적 검색 도구 선택
SEARCH_AGENT_PROMPT = """
당신은 지능적 검색 전문 에이전트입니다.
사용자의 검색 요청을 분석하여 가장 적합한 검색 도구를 선택하고 사용합니다.

🔍 검색 도구 선택 전략:

1. **WIKIPEDIA 우선 사용 케이스:**
   - 역사적 사실, 인물, 지역, 국가 정보
   - 과학적 개념, 학술적 내용
   - 잘 정립된 주제의 포괄적 설명
   - 예: "아인슈타인", "프랑스", "양자역학", "르네상스"

2. **DUCKDUCKGO 우선 사용 케이스:**
   - 기술 용어 정의, 프로그래밍 개념
   - 최신 트렌드, 현대적 주제
   - 간단한 정의나 설명이 필요한 경우
   - 예: "API란", "머신러닝 정의", "React 프레임워크"

3. **선택 원칙:**
   - 먼저 하나의 도구만 사용하여 검색
   - 결과가 불충분하거나 실패한 경우에만 다른 도구 추가 사용
   - 두 도구 모두 사용하는 것은 최후의 수단

4. **결과 평가:**
   - 검색 결과의 품질과 완성도를 평가
   - 사용자 질문에 충분히 답변할 수 있는지 판단
   - 필요시에만 보완 검색 실행

검색 후 결과를 분석하여 사용자가 이해하기 쉽게 요약하고, 어떤 검색 도구를 사용했는지 명시하세요.
"""

@tool
def search_agent(query: str) -> str:
    """
    지능적 검색 도구 선택을 통한 최적화된 정보 검색 에이전트
    
    Args:
        query: 검색할 내용
        
    Returns:
        선택된 검색 도구를 통한 최적화된 답변
    """
    try:
        agent = Agent(
            model=get_configured_model(),
            system_prompt=SEARCH_AGENT_PROMPT,
            tools=[wikipedia_search, duckduckgo_search]
        )
        
        search_prompt = f"""
        사용자 검색 요청: "{query}"
        
        다음 단계를 따라 검색을 수행하세요:
        
        1. **요청 분석**: 이 검색 요청의 성격을 파악하세요
           - 역사적/학술적 내용인가?
           - 기술적 정의나 현대적 주제인가?
           - 포괄적 설명이 필요한가, 간단한 정의면 충분한가?
        
        2. **도구 선택**: 분석 결과에 따라 가장 적합한 도구 하나를 선택하세요
           - Wikipedia: 포괄적이고 권위있는 정보가 필요한 경우
           - DuckDuckGo: 빠른 정의나 현대적 주제인 경우
        
        3. **검색 실행**: 선택한 도구로 검색을 수행하세요
        
        4. **결과 평가**: 검색 결과가 사용자 질문에 충분히 답변하는지 평가하세요
           - 충분하다면: 결과를 정리하여 답변
           - 불충분하다면: 다른 도구로 보완 검색 수행
        
        5. **최종 답변**: 
           - 검색 결과를 사용자 친화적으로 요약
           - 사용한 검색 도구 명시 (예: "Wikipedia에 따르면...", "DuckDuckGo 검색 결과...")
           - 필요시 두 도구의 결과를 종합
        
        중요: 처음부터 두 도구를 모두 사용하지 마세요. 하나씩 순차적으로 사용하세요.
        """
        
        response = agent(search_prompt)
        return str(response)
        
    except Exception as e:
        return f"검색 중 오류가 발생했습니다: {str(e)}"


# Weather Agent - 날씨 정보 전문
WEATHER_AGENT_PROMPT = """
당신은 날씨 정보 전문 에이전트입니다.
사용자가 특정 지역의 날씨를 요청하면, 먼저 해당 지역의 좌표를 찾고
National Weather Service API를 사용하여 날씨 정보를 제공합니다.
미국 지역만 지원됩니다.
"""

@tool
def weather_agent(location_query: str) -> str:
    """
    특정 지역의 날씨 정보를 제공하는 전문 에이전트
    
    Args:
        location_query: 날씨를 알고 싶은 지역
        
    Returns:
        해당 지역의 날씨 정보
    """
    try:
        agent = Agent(
            model=get_configured_model(),
            system_prompt=WEATHER_AGENT_PROMPT,
            tools=[get_position, http_request]
        )
        
        weather_prompt = f"""
        "{location_query}" 지역의 날씨 정보를 제공해주세요.
        
        단계:
        1. 먼저 지역의 정확한 좌표(위도, 경도)를 찾으세요
        2. 좌표가 미국 지역인지 확인하세요 (위도: 24-49, 경도: -125 ~ -66)
        3. 미국 지역이면 National Weather Service API를 사용하여 날씨 정보를 가져오세요
           - https://api.weather.gov/points/위도,경도 호출
           - 응답에서 forecast URL 추출
           - forecast URL 호출하여 날씨 예보 가져오기
        4. 미국 외 지역이면 "미국 지역만 지원합니다"라고 안내하세요
        
        사용자 친화적인 날씨 보고서를 제공해주세요.
        """
        
        response = agent(weather_prompt)
        return str(response)
        
    except Exception as e:
        return f"날씨 정보 조회 중 오류가 발생했습니다: {str(e)}"


# Conversation Agent - 일반 대화 전문
CONVERSATION_AGENT_PROMPT = """
당신은 친근하고 도움이 되는 대화 전문 에이전트입니다.
검색이나 날씨가 아닌 일반적인 대화, 인사, 질문에 대해 자연스럽고 유용한 답변을 제공합니다.
사용자와 친근한 대화를 나누며 필요시 조언이나 정보를 제공하세요.
"""

@tool
def conversation_agent(message: str) -> str:
    """
    일반적인 대화와 질문에 응답하는 전문 에이전트
    
    Args:
        message: 사용자의 메시지나 질문
        
    Returns:
        요청에 응답의 양식이 있다면 요청응답에 따르며, 없다면 도움이 되는 답변.
    """
    try:
        agent = Agent(
            model=get_configured_model(),
            system_prompt=CONVERSATION_AGENT_PROMPT,
            tools=[]
        )
        
        conversation_prompt = f"""
        사용자가 다음과 같이 입력하였습니다: "{message}" 
        """
        
        response = agent(conversation_prompt)
        return str(response)
        
    except Exception as e:
        return f"대화 처리 중 오류가 발생했습니다: {str(e)}"
