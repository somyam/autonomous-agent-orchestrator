"""Base Agent class capable of loading and executing registered skills."""

from typing import Any, Dict, Callable

class BaseAgent:
    def __init__(self, name: str, system_prompt: str):
        self.name: str = name
        self.system_prompt: str = system_prompt
        self.skills_registry: Dict[str, Callable] = {}

    def register_skill(self, skill_name: str, function_obj: Callable) -> None:
        """Explicitly register a Python function as an executable skill."""
        self.skills_registry[skill_name] = function_obj

    def execute_skill(self, skill_name: str, **kwargs) -> Any:
        """Execute a registered skill by its name with provided arguments."""
        if skill_name not in self.skills_registry:
            raise ValueError(f"Skill '{skill_name}' is not registered to this agent.")
        
        try:
            return self.skills_registry[skill_name](**kwargs)
        except Exception as e:
            return f"Error executing {skill_name}: {str(e)}"

    def handle_request(self, intent: str, payload: Dict[str, Any]) -> str:
        """Simulate a simple agent routing mechanism."""
        if intent in self.skills_registry:
            result = self.execute_skill(intent, **payload)
            return f"[{self.name} Response]: Successfully executed '{intent}'. Result: {result}"
        return f"[{self.name} Response]: Intent '{intent}' matches no available skills."
