from typing import List, Optional, Tuple
from uuid import UUID

from pydantic import BaseModel


class ChatMessage(BaseModel):
    model: str = "gpt-3.5-turbo"
    question: str
    # A list of tuples where each tuple is (speaker, text)
    history: List[Tuple[str, str]]
    temperature: float = 0.0
    max_tokens: int = 1024
    use_summarization: bool = False
    chat_id: Optional[UUID] = None
    chat_name: Optional[str] = None


class ChatQuestion(BaseModel):
    model: str = "gpt-3.5-turbo"
    question: str
    temperature: float = 0.0
    max_tokens: int = 1024

class Message(BaseModel):
    role: str
    content: str

class ChatQuestionWithHistory(BaseModel):
    model: str = "gpt-3.5-turbo"
    question: str
    temperature: float = 0.0
    max_tokens: int = 1024
    history: List[Message] = []
    chat_id: Optional[UUID] = None
