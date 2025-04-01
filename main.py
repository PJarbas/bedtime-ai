from book import Book, create_book
from llm_story_generator import generate_story
from prompts import story_prompt


def main() -> None:
    """
    Generates a children's story using an LLM and creates a book.
    """
    protagonist = "João"
    friend = "Passarinho"

    prompt = story_prompt(protagonist, friend)
    book: Book = generate_story(prompt)
    create_book(book.title, book.story)


if __name__ == "__main__":
    main()
