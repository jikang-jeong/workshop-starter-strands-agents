# Strands Agents Workshop Starter Kit

🎭 **Multi-Agent System Workshop using Agents as Tools Pattern**

This starter kit provides basic templates for a workshop that implements the Agents as Tools pattern using Strands Agents and Amazon Bedrock.

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone the repository
git clone <repository-url>
cd strands-agents-workshop-starter-kit

# Grant execution permissions
chmod +x run.sh

# Set up environment variables
cp .env.example .env
# Edit .env file to add AWS configuration
```

### 2. Automatic Execution

```bash
# Create virtual environment, install packages, and run app all at once
./run.sh
```

## 📁 Project Structure

```
strands-agents-workshop-starter-kit/
├── README.md                    # This file
├── requirements.txt             # Dependencies list
├── run.sh                      # Automatic execution script
├── .env.example                # Environment variables template
├── model_config.py             # Model configuration (template)
├── mcp_tools.py               # MCP tools (template)
├── sub_agents.py              # Sub agents (template)
├── orchestrator_agent.py      # Orchestrator (template)
├── main.py                    # Main app (template)
├── workshop_test.py           # Test script
└── templates/                 # Step-by-step completed code reference
    ├── lab2-mcp_tools.py
    ├── lab3-sub_agents.py
    ├── lab4-orchestrator_agent.py
    └── lab5-main.py
```

## 🎯 Workshop Progress Order

1. **Lab 1**: Environment Setup - Set up this starter kit
2. **Lab 2**: MCP Tools Creation - Implement `mcp_tools.py`
3. **Lab 3**: Sub Agents Implementation - Implement `sub_agents.py`
4. **Lab 4**: Orchestrator Agent - Implement `orchestrator_agent.py`
5. **Lab 5**: Agents as Tools Pattern - Implement `main.py`

## 🔧 Key Features

- **🎭 Orchestrator Agent**: Request analysis and sub-agent coordination
- **🔍 Search Agent**: Intelligent search (Wikipedia + DuckDuckGo)
- **🌤️ Weather Agent**: Location-based weather information query
- **💬 Conversation Agent**: Natural conversation processing
- **🤖 Bedrock Integration**: Amazon Bedrock Claude model utilization

## 📝 Environment Variables Setup

Add the following configuration to your `.env` file:

```bash
# AWS Configuration
AWS_REGION=us-west-2
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

# Bedrock Model Configuration
BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0
```

## 🧪 Testing

```bash
# Individual component testing
python3 mcp_tools.py
python3 sub_agents.py
python3 orchestrator_agent.py

# Integrated system testing
python3 workshop_test.py

# Main application execution
python3 main.py
```

## 📚 Reference Code

Completed code for each step can be found in the `templates/` folder:

- `lab2-mcp_tools.py`: MCP tools completed code
- `lab3-sub_agents.py`: Sub agents completed code
- `lab4-orchestrator_agent.py`: Orchestrator completed code
- `lab5-main.py`: Complete system code

## 🆘 Troubleshooting

### Common Issues

1. **Model Access Error**
   - Check AWS credentials
   - Verify Bedrock service permissions
   - Confirm region settings

2. **Package Installation Error**
   - Check Python 3.10+ version
   - Verify virtual environment activation
   - Check network connection

3. **API Call Error**
   - Check internet connection
   - Verify API limits
   - Check timeout settings

## 🎓 Learning Objectives

Through this workshop, you can learn:

- **Agents as Tools Pattern**: AI-based dynamic tool selection
- **Hierarchical Agent Structure**: Orchestrator and sub-agents
- **Intelligent Orchestration**: Request analysis and execution planning
- **Practical Application**: Architecture applicable in production environments

## 📞 Support

If you encounter issues during the workshop:

1. Check reference code in the `templates/` folder
2. Refer to comments and docstrings in each file
3. Contact workshop facilitator

---

**Happy Coding! 🚀**
