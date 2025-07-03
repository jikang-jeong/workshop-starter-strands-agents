"""Main Application - Strands Agents Workshop"""
import os
import sys
from typing import Dict, Any
from orchestrator_agent import OrchestratorAgent
from model_config import get_configured_model


class StrandsAgentsWorkshopApp:
    """
    Strands Agents Workshop Main Application
    
    Actual implementation of multi-agent system using 
    Agents as Tools pattern.
    """

    def __init__(self, model_id: str = None, user_id: str = "workshop_user"):
        """
        Initialize application
        
        Args:
            model_id: Model ID to use
            user_id: User identifier
        """
        # TODO: Implement in Lab 5
        # Hint:
        # 1. Model configuration
        # 2. Create orchestrator agent
        # 3. Display system information
        pass

    def _display_system_info(self):
        """Display system information"""
        # TODO: Implement in Lab 5
        pass

    def process_input(self, user_input: str) -> Dict[str, Any]:
        """
        Process user input through orchestrator agent
        
        Args:
            user_input: User input
            
        Returns:
            Processing result
        """
        # TODO: Implement in Lab 5
        pass

    def format_response(self, result: Dict[str, Any]) -> str:
        """
        Format processing result in user-friendly way
        
        Args:
            result: Processing result
            
        Returns:
            Formatted response string
        """
        # TODO: Implement in Lab 5
        pass

    def run_single_query(self, query: str) -> Dict[str, Any]:
        """
        Execute single query
        
        Args:
            query: Query to execute
            
        Returns:
            Execution result
        """
        # TODO: Implement in Lab 5
        pass

    def run_interactive_mode(self):
        """
        Execute interactive mode
        """
        # TODO: Implement in Lab 6
        # Hint:
        # 1. User input loop
        # 2. Handle exit conditions
        # 3. Format and output responses
        # 4. Error handling
        pass


def main():
    """Main execution function"""
    # TODO: Implement in Lab 5
    # Hint:
    # 1. Handle command line arguments
    # 2. Branch between single query vs interactive mode
    # 3. Execute application
    print("💡 Implement in Lab 5!")
    print("🎯 Goal: Support single query mode and interactive mode")


if __name__ == "__main__":
    main()
