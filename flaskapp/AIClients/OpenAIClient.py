from openai import OpenAI
from AIClients.AbstractAIClient import AbstractAIClient

class OpenAIClient(AbstractAIClient):
    """
    A client for interacting with the OpenAI API using the GPT-3.5 Turbo model.

    Attributes:
        client (OpenAI): An instance of the OpenAI class for making API requests.

    Methods:
        __init__(): Initializes the OpenAIClient with the OpenAI API key.
        ask(question): Sends a question to the OpenAI API and returns the response.
    """

    def __init__(self, OPEN_AI_SECRET_KEY):
        """
        Initializes the OpenAIClient with the OpenAI API key.
        """
        self.client = OpenAI(api_key=OPEN_AI_SECRET_KEY)

    def ask(self, question):
        """
        Sends a question to the OpenAI API and returns the response.

        Args:
            question (str): The question to ask the AI.

        Returns:
            str: The response from the AI.
        """
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return chat_completion.choices[0].message.content