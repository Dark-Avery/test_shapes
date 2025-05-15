def create_shape(name: str, *args, registry):
    cls = registry.get(name)
    if not cls:
        raise ValueError(f"Unknown shape: {name}")
    return cls(*args)
