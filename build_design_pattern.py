# DocumentBuilder interface
class DocumentBuilder:
    def create_header(self, text):
        pass

    def create_paragraph(self, text):
        pass

    def create_list(self, items):
        pass

    def get_document(self):
        pass

# Concrete builder for PDF documents
class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = ""

    def create_header(self, text):
        self.document += f"<h1>{text}</h1>\n"

    def create_paragraph(self, text):
        self.document += f"<p>{text}</p>\n"

    def create_list(self, items):
        self.document += "<ul>\n"
        for item in items:
            self.document += f"  <li>{item}</li>\n"
        self.document += "</ul>\n"

    def get_document(self):
        return self.document

# Concrete builder for HTML documents
class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = ""

    def create_header(self, text):
        self.document += f"<h1>{text}</h1>\n"

    def create_paragraph(self, text):
        self.document += f"<p>{text}</p>\n"

    def create_list(self, items):
        self.document += "<ul>\n"
        for item in items:
            self.document += f"  <li>{item}</li>\n"
        self.document += "</ul>\n"

    def get_document(self):
        return self.document

# Concrete builder for Plain Text documents
class PlainTextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = ""

    def create_header(self, text):
        self.document += f"--- {text} ---\n\n"

    def create_paragraph(self, text):
        self.document += f"{text}\n\n"

    def create_list(self, items):
        for idx, item in enumerate(items, start=1):
            self.document += f"{idx}. {item}\n"
        self.document += "\n"

    def get_document(self):
        return self.document

# Director class that builds documents using the provided builder
class DocumentGenerator:
    def __init__(self, builder):
        self.builder = builder

    def generate_document(self):
        self.builder.create_header("Sample Document")
        self.builder.create_paragraph("This is a paragraph in the document.")
        self.builder.create_list(["Item 1", "Item 2", "Item 3"])

# Client code
if __name__ == "__main__":
    pdf_builder = PDFDocumentBuilder()
    html_builder = HTMLDocumentBuilder()
    plain_text_builder = PlainTextDocumentBuilder()

    pdf_document_generator = DocumentGenerator(pdf_builder)
    html_document_generator = DocumentGenerator(html_builder)
    plain_text_document_generator = DocumentGenerator(plain_text_builder)

    pdf_document_generator.generate_document()
    pdf_document = pdf_builder.get_document()
    print("Generated PDF Document:")
    print(pdf_document)

    html_document_generator.generate_document()
    html_document = html_builder.get_document()
    print("\nGenerated HTML Document:")
    print(html_document)

    plain_text_document_generator.generate_document()
    plain_text_document = plain_text_builder.get_document()
    print("\nGenerated Plain Text Document:")
    print(plain_text_document)
