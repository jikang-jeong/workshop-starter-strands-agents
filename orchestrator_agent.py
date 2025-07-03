"""Orchestrator Agent - Strands Agents Workshop"""
from strands import Agent
from sub_agents import search_agent, weather_agent, conversation_agent
from model_config import get_configured_model
from typing import Dict, Any


class OrchestratorAgent:
    """
    Orchestrator Agent - Core of Agents as Tools Pattern
    
    Advanced AI system that analyzes user requests and delegates tasks 
    to appropriate sub-agents.
    """

    def __init__(self, model=None, user_id: str = "workshop_user"):
        """
        Initialize Orchestrator Agent
        
        Args:
            model: LLM model to use (uses default model if None)
            user_id: User identifier
        """
        # TODO: Implement in Lab 4
        # Hint:
        # 1. Model configuration and availability test
        # 2. Create orchestrator agent
        # 3. Register sub-agents as tools
        pass

    def _assess_clarity(self, user_input: str) -> Dict[str, Any]:
        """
        Assess the clarity of user request.
        
        Args:
            user_input: User input
            
        Returns:
            Clarity assessment result
        """
        # TODO: Implement in Lab 4
        # Hint:
        # 1. Create clarity assessment dedicated agent
        # 2. CLEAR/VAGUE judgment logic
        # 3. Error handling
        pass

    def _create_execution_plan(self, user_input: str) -> Dict[str, Any]:
        """
        Create execution plan for user request.
        
        Args:
            user_input: User input
            
        Returns:
            Execution plan information
        """
        # TODO: Implement in Lab 4
        # Hint:
        # 1. Create planning dedicated agent (no tool usage)
        # 2. Define execution plan format
        # 3. Determine agent selection and order
        pass

    def process_user_input(self, user_input: str) -> Dict[str, Any]:
        """
        Process user input and delegate to appropriate sub-agents
        
        3-step processing pipeline:
        1. Clarity assessment
        2. Execution plan creation  
        3. Plan execution
        
        Args:
            user_input: User input
            
        Returns:
            Processing result
        """
        # TODO: Implement in Lab 4
        # Hint:
        # 1. Check model availability
        # 2. Implement 3-step pipeline
        # 3. Handle vague requests
        # 4. Execute plan and organize results
        pass

    def get_agent_status(self) -> Dict[str, Any]:
        """Return agent status information"""
        # TODO: Implement in Lab 4
        pass


# Test code
if __name__ == "__main__":
    print("🧪 Orchestrator Agent Test")
    print("=" * 60)
    
    # TODO: Write test code in Lab 4
    print("💡 Implement and test in Lab 4!")
    
    # Example:
    # orchestrator = OrchestratorAgent()
    # result = orchestrator.process_user_input("Hello")
    # print(f"Success: {result.get('success')}")
