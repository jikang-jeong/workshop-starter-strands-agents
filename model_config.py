"""Model Configuration - Strands Agents Workshop"""
import os
from strands.models import BedrockModel


def get_configured_model(model_id: str = None) -> BedrockModel:
    """Workshop Bedrock model configuration
    
    Args:
        model_id: Model ID to use (optional)
        
    Returns:
        Configured BedrockModel instance
    """
    # TODO: Implement in Lab 1
    # Determine model ID (priority: parameter > environment variable > default)
    final_model_id = (
        model_id or 
        os.getenv("MODEL_ID") or 
        "us.amazon.nova-pro-v1:0"
    )
    
    # AWS region configuration
    region = os.getenv("AWS_REGION", "us-west-2")
    
    # Create Bedrock model
    model = BedrockModel(
        model_id=final_model_id,
        region=region,
        temperature=0.7,
        max_tokens=4096,
        streaming=False  # Disable streaming for workshop
    )
    
    # Add model_id attribute (compatibility)
    if not hasattr(model, 'model_id'):
        model.model_id = final_model_id
    
    return model


# Environment information (for display)
MODEL_PROVIDER = "bedrock"
MODEL_ID = os.getenv("MODEL_ID", "us.amazon.nova-pro-v1:0")

# Supported models list (workshop reference)
SUPPORTED_MODELS = {
    "nova_pro": "us.amazon.nova-pro-v1:0",
    "claude_sonnet": "anthropic.claude-3-5-sonnet-20241022-v2:0",
    "claude_haiku": "anthropic.claude-3-haiku-20240307-v1:0"
}


def get_model_info(model_id: str = None) -> dict:
    """Return model information"""
    current_model_id = model_id or MODEL_ID
    
    model_names = {
        "us.amazon.nova-pro-v1:0": "Amazon Nova Pro",
        "anthropic.claude-3-5-sonnet-20241022-v2:0": "Claude 3.5 Sonnet",
        "anthropic.claude-3-haiku-20240307-v1:0": "Claude 3 Haiku"
    }
    
    return {
        "model_id": current_model_id,
        "model_name": model_names.get(current_model_id, "Unknown Model"),
        "provider": MODEL_PROVIDER,
        "region": os.getenv("AWS_REGION", "us-west-2")
    }
