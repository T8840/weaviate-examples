import weaviate
import time
from .config import client

schema = {
   "classes": [
       {
           "class": "Discord",
           "description": "Discord Information.",
           "moduleConfig": {
               "text2vec-transformers": {
                    "skip": False,
                    "vectorizeClassName": False,
                    "vectorizePropertyName": False
                }
           },
           "vectorIndexType": "hnsw",
           "vectorizer": "text2vec-transformers",
           "properties": [
               {
                   "name": "content",
                   "dataType": ["text"],
                   "description": "The text content of the podcast clip",
                   "moduleConfig": {
                    "text2vec-transformers": {
                        "skip": False,
                        "vectorizePropertyName": False,
                        "vectorizeClassName": False
                    }
                   }
               },
               {
                "name": "sender",
                "dataType": ["string"],
                "description": "The sender in the discord",
                "moduleConfig": {
                    "text2vec-transformers": {
                        "skip": True,
                        "vectorizePropertyName": False,
                        "vectorizeClassName": False
                    }
                }
               },
               {
                   "name": "channelNum",
                   "dataType": ["int"],
                   "description": "The channel number.",
                   "moduleConfig": {
                    "text2vec-transformers": {
                        "skip": True,
                        "vectorizePropertyName": False,
                        "vectorizeClassName": False
                    }
                   }
               },
           ]
       }
   ]
}

client.schema.create(schema)