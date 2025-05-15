class ShapeRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, name: str):
        def decorator(cls):
            self._registry[name.lower()] = cls
            return cls
        return decorator

    def get(self, name: str):
        return self._registry.get(name.lower())

    def list_shapes(self):
        return list(self._registry.keys())
