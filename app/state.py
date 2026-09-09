from dataclasses import dataclass, field


@dataclass
class AgentState:
    user_input: str
    goal: str

    plan: list[str] = field(default_factory=list)
    current_step: int = 0

    tool_results: dict = field(default_factory=dict)
    retrieved_memories: list[str] = field(default_factory=list)

    final_answer: str = ""
    reflection: str = ""

    confidence: float = 0.0

    metadata: dict = field(default_factory=dict)

@dataclass
class AgentState:
    user_input: str
    goal: str

    pdf_path: str = ""

    plan: list = field(default_factory=list)
    current_step: int = 0

    tool_results: dict = field(default_factory=dict)
    retrieved_memories: list[str] = field(default_factory=list)

    final_answer: str = ""
    reflection: str = ""

    confidence: float = 0.0

    metadata: dict = field(default_factory=dict)