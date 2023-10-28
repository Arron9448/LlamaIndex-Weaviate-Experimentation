### ====== Import article data to Weaviate instance (WCS) ====== 
import os
import weaviate 
from connectwcs import connectwcs

from llama_index import SimpleDirectoryReader
#from llama_index.node_parser import SimpleNodeParser
from llama_index.vector_stores import WeaviateVectorStore
from llama_index import VectorStoreIndex, StorageContext
from llama_index.storage.storage_context import StorageContext

# Connect to Weaviate instance (WCS)
client = connectwcs()

# Load .json documents from dataset
articles = SimpleDirectoryReader(input_dir='./dataset').load_data()
print(f"Loaded {len(articles)} articles")

# Build the VectorStoreIndex
#parser = SimpleNodeParser.from_defaults(chunk_size=1024, chunk_overlap=20)
#nodes = parser.get_nodes_from_documents(articles)

vector_store = WeaviateVectorStore(weaviate_client = client, index_name="Article", text_key="title")
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(articles, storage_context=storage_context)