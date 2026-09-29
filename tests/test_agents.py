"""Unit tests for Agent infrastructure and skill routing."""

from src.agents.base_agent import BaseAgent
from src.skills.math_skills import compute_fibonacci

def test_agent_skill_execution():
    """Verify that an agent can register and successfully run a skill."""
    agent = BaseAgent(name="MathAnalyst", system_prompt="Test Prompt")
    agent.register_skill("compute_fibonacci", compute_fibonacci)
    
    # Simulate a routed request payload
    response = agent.handle_request(
        intent="compute_fibonacci", 
        payload={"n": 10}
    )
    
    assert "Result: 55" in response
