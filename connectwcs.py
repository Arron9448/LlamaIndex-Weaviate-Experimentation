### ====== Connect to Weaviate instance, return Client ====== 
import os
import weaviate

def connectwcs():
    client = weaviate.Client(
        url=os.getenv("WCS_URL"),
        auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY")),
        additional_headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
       }
    )
    assert client.is_ready()
    return client