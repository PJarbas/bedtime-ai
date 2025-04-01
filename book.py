from typing import List

from loguru import logger
from pydantic import BaseModel, Field
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


class Book(BaseModel):
    """
    Represents a book with a title, story, and list of illustrations.
    """

    title: str = Field(..., description="The title of the story")
    story: str = Field(..., description="The main text of the story")
    illustrations: List[str] = Field(..., description="List of illustrations")


def create_book(title: str, story: str, file_name: str = "book.pdf") -> None:
    """
    Creates a PDF book from a story.

    Args:
        title: The title of the book.
        story: The story to include in the book.
        file_name: The name of the PDF file to create. Defaults to "book.pdf".
    """

    doc = SimpleDocTemplate(filename=file_name, pagesize=letter)
    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = 1  # Center alignment

    text_style = styles["Normal"]
    text_style.fontName = "Helvetica"
    text_style.fontSize = 12
    text_style.leading = 14

    elements = []

    elements.append(Paragraph(title, title_style))
    elements.append(Spacer(1, 0.5 * inch))

    paragraphs = story.split("\n\n")

    for paragraph in paragraphs:
        elements.append(Paragraph(paragraph, text_style))
        elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)
    logger.info(f"Book created: {file_name}")
