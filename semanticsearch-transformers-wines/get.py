## https://weaviate.io/developers/weaviate/tutorials/query

import weaviate
import json
from .config import  api_key,weaviate_url

client = weaviate.Client(
    url=weaviate_url,  # Replace with your endpoint
    additional_headers={
        "X-OpenAI-Api-Key": api_key  # Or "X-Cohere-Api-Key" or "X-HuggingFace-Api-Key"
    }
)
### Get with nearText
nearText = {"concepts": ["fruit"]}

result = (
    client.query
    .get("Wine", ["title","description"])
    .with_near_text(nearText)
    .with_limit(2)
    .do()
)

print(json.dumps(result, indent=4))

