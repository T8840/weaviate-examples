import weaviate
from .config import client

class_obj = {
    "invertedIndexConfig": {
        "stopwords": { 
            "preset": "en",
            "additions": ["is", "exactly"]                                         
        }
    }
}

client.schema.update_config("Discord", class_obj)