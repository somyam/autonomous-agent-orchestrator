# Autonomous AI Agent Workspace

A production-grade, modular Python architecture demonstrating autonomous multi-skill orchestration using the Anthropic Claude API.

This repository implements a **Code-First Architecture with Automated Documentation**. `Pydantic` ensures type-safety, input validation, and real-time synchronization with cloud models.

---

## 🏛️ System Documentation Map

To keep the repository scannable for both human developers and downstream AI coding models (like Codex), system rules are split across three standardized documentation layers:

*   **`README.md`**: *The entry point for developers.* Contains high-level project goals, setup guides, environment instructions, and execution workflows.
*   **`AGENTS.md`**: *The system persona blueprint.* Outlines active agent roles, access restrictions, and identity constraints within the workspace.
*   **`SKILLS.md`**: *The capabilities tool manual.* Registers function pathways, strict interface inputs, and constraint conditions for available developer tools.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have `Python 3.10+` installed on your machine.

### 2. Set Up the Environment
Clone this repository to your local workspace, navigate to the root directory, and create an isolated virtual environment:

```bash
# Create and launch the virtual environment
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configure Authentication
The system uses the official Anthropic SDK which automatically looks for an `ANTHROPIC_API_KEY` system environment variable. Export your key in your active terminal session:

```bash
export ANTHROPIC_API_KEY="your-actual-claude-api-key-here"
```

---

## 🧪 Verification & Testing Protocol

Before executing the live autonomous application, run the localized unit test suite to guarantee that mathematical logic engines and routing states are entirely unbroken:

```bash
python -m pytest
```

---

## 🏃‍♂️ Running the Autonomous Application

To execute the application and witness the model autonomously evaluating user intent, selecting the correct local skill, executing it, and synthesizing a response, run the main orchestration script from the repository root:

```bash
python -m src.main
```

### Behind-The-Scenes Loop Lifecycle:
1. **Turn 1 (Evaluation)**: The system feeds the global tool payload (dynamically generated via Pydantic model schemas) to Claude.
2. **Interception**: Claude responds with a structured `tool_use` stop reason event, pausing text generation to request an external asset calculation.
3. **Execution**: Your local Python runtime triggers the matched native function algorithm (`src/skills/`).
4. **Turn 2 (Synthesis)**: The application submits the local execution outcomes back to the model history, prompting Claude to cleanly summarize the verified solution.
