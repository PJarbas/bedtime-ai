import instructor
from config import get_llm_client
from book import Book
from loguru import logger


def generate_story(prompt: str) -> Book:
    """
    Generate a story from a prompt.

    Args:
        prompt: The prompt to generate the story from.

    Returns:
        The generated story.
    """

    logger.info("Generating story from prompt")

    llm_client, model = get_llm_client()

    client = instructor.from_openai(llm_client, mode=instructor.Mode.MD_JSON)

    llm_response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        response_model=Book,
    )

    logger.info("Story generated!")

    return llm_response
