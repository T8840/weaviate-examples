import weaviate
import json
from .config import client

result = client.backup.restore(
    backup_id="channelNum",
    backend='filesystem',
    wait_for_completion=True
)

print(json.dumps(result, indent=4))