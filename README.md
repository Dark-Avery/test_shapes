# geometry-shapes

A flexible geometry shape library.

## Installation

Build and install via PEP 517:

```bash
pip install build           # if not already installed
python -m build --wheel     # builds a wheel into dist/
pip install dist/*.whl      # installs the library
````

Or install in editable (development) mode:

```bash
pip install build
pip install -e .
```

## Usage

```python
from test_shapes import ShapeRegistry, register_shapes, create_shape, Shape

# 1. Create a registry
registry = ShapeRegistry()

# 2. Register the shapes provided by the library (circle, triangle)
register_shapes(registry)

# 3. Create shapes dynamically by name
circle   = create_shape("circle",   5,       registry=registry)
triangle = create_shape("triangle", 3, 4, 5, registry=registry)

print(circle.area())    # 78.5398...
print(triangle.area())  # 6.0

# 4. For Triangle, you can also check if it's a right-angled triangle
print(triangle.is_right())  # True for (3,4,5)

# 5. Dynamically register your own new shape (e.g. square)
@registry.register("square")
class Square(Shape):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side must be positive")
        self.side = side

    def area(self) -> float:
        return self.side ** 2

sq = create_shape("square", 4, registry=registry)
print(sq.area())        # 16
```

## API Reference

### Classes

* **ShapeRegistry**

  * `register(name: str)`: decorator to register a `Shape` subclass under the given name.
  * `get(name: str) -> Type[Shape] | None`: retrieve the registered class by name.
  * `list_shapes() -> List[str]`: list all registered shape names.

* **Shape** (abstract base class)
  * `area() -> float`: compute the area of the shape.

* **Triangle** (subclass of `Shape`)
  * `is_right() -> bool`: return `True` if the triangle is right-angled (i.e. satisfies \(a^2 + b^2 = c^2\)), else `False`.

### Functions

* `register_shapes(registry: ShapeRegistry)`: registers the built-in shapes (`circle`, `triangle`) in the given registry.
* `create_shape(name: str, *args, registry: ShapeRegistry) -> Shape`: factory function to create a shape by name with the provided parameters.

## Tests

Run all tests with:

```bash
python -m unittest discover tests
```
