"""Orchestrator Agent - Strands Agents Workshop"""
from strands import Agent
from sub_agents import search_agent, weather_agent, conversation_agent
from model_config import get_configured_model
from typing import Dict, Any
import re


class OrchestratorAgent:
    """
    Orchestrator Agent - Core of Agents as Tools Pattern

    Simplified AI system that analyzes user requests and delegates tasks
    to appropriate sub-agents.
    """

    def __init__(self, model=None, user_id: str = "workshop_user"):
        """
        Initialize Orchestrator Agent

        Args:
            model: LLM model to use (uses default model if None)
            user_id: User identifier
        """
        self.model = model or get_configured_model()
        self.user_id = user_id
        self.orchestrator = self._create_orchestrator_agent() 
        
    def _create_orchestrator_agent(self) -> Agent:
        """Create the main orchestrator agent with sub-agents as tools"""
        system_prompt = f"""You are an intelligent orchestrator that analyzes user requests and delegates tasks to appropriate sub-agents.
User ID: {self.user_id}

Available sub-agents:
- search_agent: Use for information search requests (Wikipedia + DuckDuckGo)
- weather_agent: Use for weather information requests (US regions only)  
- conversation_agent: Use for general conversation, greetings, simple questions

Instructions:
1. Analyze the user request carefully
2. If the request is very vague (single words like "coffee", "food"), ask for clarification using conversation_agent
3. For clear requests, select and use the most appropriate sub-agent(s)
4. You can use multiple sub-agents if needed for complex requests
5. Always provide a helpful and complete response to the user

Remember: You have the intelligence to determine what the user needs - trust your judgment!"""

        return Agent(
            model=self.model,
            system_prompt=system_prompt,
            tools=[search_agent, weather_agent, conversation_agent]
        )
    def process_user_input(self, user_input: str) -> Dict[str, Any]:
        """
        Process user input through the orchestrator agent
        
        Simple single-step processing:
        - Let the orchestrator agent handle everything intelligently
        - No complex planning or clarity assessment needed
        
        Args:
            user_input: User input
            
        Returns:
            Processing result
        """
        try:
            print(f"\n🎭 ORCHESTRATOR AGENT 처리 중...")
            print("="*50)
            
            # Let the orchestrator agent handle everything
            response = self.orchestrator(user_input)
            
            return {
                "success": True,
                "agent": "orchestrator_agent", 
                "user_input": user_input,
                "response": str(response),
                "needs_clarification": False,
                "user_id": self.user_id
            }
            
        except Exception as e:
            return {
                "success": False,
                "agent": "orchestrator_agent",
                "error": f"요청 처리 중 오류가 발생했습니다: {str(e)}",
                "user_input": user_input
            }
 
# Test code
# 테스트 코드 (파일 하단에 추가)

# Test code
if __name__ == "__main__":
    print("🧪 Orchestrator Agent Test")
    print("=" * 60)

    # Create orchestrator
    orchestrator = OrchestratorAgent()

    # Test cases
    test_cases = [
        ("Hello", "General conversation"),
        ("What's the weather in Seattle?", "Weather query"),
        ("Tell me about artificial intelligence", "Information search"),
        ("Tell me about Paris and also check the weather", "Complex request")
    ]

    for i, (query, description) in enumerate(test_cases, 1):
        print(f"\n🧪 Test {i}: {description}")
        print(f"Input: '{query}'")
        print("-" * 40)

        result = orchestrator.process_user_input(query)

        print(f"✅ Success: {result.get('success')}")
        print(f"🤖 Agent: {result.get('agent')}")

        if result.get('response'):
            response = result['response'][:200] + "..." if len(result['response']) > 200 else result['response']
            print(f"📝 Response: {response}")

        if result.get('error'):
            print(f"❌ Error: {result['error']}")

        print("=" * 60)

    print("🎉 Orchestrator test completed!")
