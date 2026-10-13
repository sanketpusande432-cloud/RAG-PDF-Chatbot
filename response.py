from llm import get_llm
from vectordb import get_vectordb

llm = get_llm()
vector_db = get_vectordb()

def generate_response(question, previous_history):
    result = vector_db.query(query_texts=[question], n_results=2)

    selected_chunks = result['documents'][0]

    prompt = f'''System: You are a helpful assistant. Answer the user's question using ONLY the
factual context and previous history provided below.

If the answer cannot be found in the context, say "I cannot find the answer in the provided documents."

Do not use any outside knowledge or assumptions. Cite the source ID when stating a fact.

Context:
{selected_chunks}

History:
{previous_history}

User Query: {question}
'''

    result = llm.invoke(prompt)

    return result.content, selected_chunks