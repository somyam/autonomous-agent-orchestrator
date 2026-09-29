"""Autonomous agent runner implementing global tool routing via Claude Opus 5.5."""

import os
import sys
from typing import List, Dict, Callable, Any
import anthropic
from pydantic import BaseModel, Field

# Ensure internal modules can resolve
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.skills.math_skills import compute_fibonacci
from src.skills.text_skills import analyze_and_summarize_text


# ==========================================
# 🧮 1. DYNAMIC TOOL GENERATION (Pydantic)
# ==========================================

class FibonacciInput(BaseModel):
    """Input validation structure for the Fibonacci calculation skill."""
    n: int = Field(..., description="The 1-based index position of the sequence to retrieve.")


class TextAnalysisInput(BaseModel):
    """Input validation structure for the text analysis skill."""
    text: str = Field(..., description="The raw target body of text that needs structural metadata analysis.")
    max_keywords: int = Field(default=3, description="The maximum number of top frequency keywords to extract.")


def generate_anthropic_schema(name: str, description: str, input_model: type[BaseModel]) -> Dict[str, Any]:
    """Transforms a Pydantic input model automatically into a valid Anthropic tool schema block."""
    return {
        "name": name,
        "description": description,
        "input_schema": input_model.model_json_schema()
    }


# ==========================================
# 🧠 2. GLOBAL SYSTEM REGISTRY (Unified Pool)
# ==========================================

GLOBAL_TOOL_SCHEMAS = [
    generate_anthropic_schema(
        name="compute_fibonacci",
        description="Calculate the n-th Fibonacci number using an optimized, O(n) iterative approach. Use this when the user mentions sequence positions.",
        input_model=FibonacciInput
    ),
    generate_anthropic_schema(
        name="analyze_and_summarize_text",
        description="Analyze a text string block, calculate word frequencies, count total words, and return key metrics. Use this for documents, strings, or counting requests.",
        input_model=TextAnalysisInput
    )
]

GLOBAL_TOOL_MAPPING: Dict[str, Callable] = {
    "compute_fibonacci": compute_fibonacci,
    "analyze_and_summarize_text": analyze_and_summarize_text
}


# ==========================================
# 🚀 3. RUNTIME AUTONOMOUS ROUTER
# ==========================================

def run_autonomous_router(user_prompt: str):
    """Feeds the user request and ALL tools to Claude, allowing the model to choose dynamically."""
    client = anthropic.Anthropic()
    
    model_name = "claude-opus-5-5"

    supervisor_prompt = (
        "You are an Autonomous Orchestrator Engine executing within a Python workspace. "
        "You have access to a suite of highly specific local developer tools. "
        "Analyze the user's intent, select the correct tool from your available toolkit, "
        "execute it, and cleanly report back the results."
    )

    print(f"\n[User Query Input]: '{user_prompt}'")
    print(f"[Supervisor Status]: Evaluating global toolkit using {model_name}...")

    # Turn 1: Initial orchestration pass
    response = client.messages.create(
        model=model_name,
        max_tokens=2048,  # Bumped tokens to safely accommodate reasoning/thinking chains
        system=supervisor_prompt,
        tools=GLOBAL_TOOL_SCHEMAS,
        messages=[{"role": "user", "content": user_prompt}]
    )

    # Handle Tool Execution
    if response.stop_reason == "tool_use":
        tool_use_block = next(block for block in response.content if block.type == "tool_use")
        tool_name = tool_use_block.name
        tool_input = tool_use_block.input
        tool_use_id = tool_use_block.id

        print(f"[Dynamic Selection]: Claude autonomously selected tool -> '{tool_name}'")
        print(f"[Extracted Payload]: {tool_input}")

        if tool_name in GLOBAL_TOOL_MAPPING:
            # Safely execute local function mapping matches
            tool_result = GLOBAL_TOOL_MAPPING[tool_name](**tool_input)
            print(f"[Execution Success]: Output generated -> {tool_result}")

            # Turn 2: Secondary pass feeding local outcomes back to the model
            final_response = client.messages.create(
                model=model_name,
                max_tokens=2048,
                system=supervisor_prompt,
                tools=GLOBAL_TOOL_SCHEMAS,
                messages=[
                    {"role": "user", "content": user_prompt},
                    {"role": "assistant", "content": response.content},
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "tool_result",
                                "tool_use_id": tool_use_id,
                                "content": str(tool_result),
                            }
                        ],
                    },
                ],
            )
            print("\n[Agent Autonomous Response]:")
            text_output = next((block.text for block in final_response.content if block.type == "text"), "(No text response)")
            print(text_output)
        else:
            print(f"[Error]: Selected tool '{tool_name}' does not exist in local Python registry.")
    else:
        print("\n[Agent Autonomous Response]:")
        text_output = next((block.text for block in response.content if block.type == "text"), "(No text response)")
        print(text_output)


if __name__ == "__main__":
    # Test 1: Verifying autonomous math skill routing selection
    math_query = "What is the 8th value in the Fibonacci sequence?"
    run_autonomous_router(math_query)
    
    print("-" * 50)
    
    # Test 2: Verifying autonomous text skill routing selection
    text_query = "Can you count the words in this string: 'Hello running workspace system'?"
    run_autonomous_router(text_query)
