from docx import Document

# Load the master document with all phrases
doc = Document("AA Cover Letter BASE.docx")

# Extract all paragraphs
paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]

print(paragraphs)

