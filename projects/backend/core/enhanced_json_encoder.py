from dataclasses import asdict, is_dataclass
from json import JSONEncoder


class EnhancedJSONEncoder(JSONEncoder):
    """
    EnhancedJSONEncoder is used to return dataclasses as dict if it is needed
    """

    def default(self, o):
        if is_dataclass(o) and hasattr(o, "repr_json"):
            return asdict(o)
        return super().default(o)
