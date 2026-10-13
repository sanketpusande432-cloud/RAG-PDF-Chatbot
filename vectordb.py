from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb


def get_vectordb(filename='Python_RAG_8_Pages.pdf'):

    reader = PdfReader(filename)

    text = ""

    for page in reader.pages:
        text = text + (page.extract_text() or "")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(text)

    client = chromadb.Client()

    vector_db = client.get_or_create_collection('python_db')

    ids = ['c' + str(i) for i in range(len(chunks))]

    vector_db.add(documents=chunks, ids=ids)

    return vector_db