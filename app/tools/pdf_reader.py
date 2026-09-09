from pypdf import PdfReader


def pdf_reader(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text