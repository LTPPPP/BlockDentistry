import json
from datetime import datetime

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def serialize_to_json(obj):
    """Serialize an object to JSON"""
    return json.dumps(obj, cls=JSONEncoder)

def deserialize_from_json(json_str):
    """Deserialize an object from JSON"""
    return json.loads(json_str)