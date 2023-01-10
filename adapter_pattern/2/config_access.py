from typing import Protocol, Any

class Config(Protocol):
    def get(self, key: str) -> Any | None:
        """Return the value associated with the key.
        """
        pass
    
