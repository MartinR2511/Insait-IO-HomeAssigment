from abc import ABC, abstractmethod

class ChatAI(ABC):
    """
    Abstract base class for an AI chat.

    Methods:
        ask(question): Sends a question to AI returns the response.
    """

    @abstractmethod
    def ask(self, question):
        pass