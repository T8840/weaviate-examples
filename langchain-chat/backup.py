import weaviate
import json
from .config import client

# add an extra check to make sure we aren't overwriting an existing backup!!

result = client.backup.create(
    backup_id="channelNum",
    backend='filesystem',
)

print(json.dumps(result, indent=4))