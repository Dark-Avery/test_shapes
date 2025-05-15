import unittest
from test_shapes import ShapeRegistry, register_shapes, create_shape, Shape

class TestShapes(unittest.TestCase):
    def setUp(self):
        self.registry = ShapeRegistry()
        register_shapes(self.registry)

    def test_circle_area(self):
        circle = create_shape("circle", 2, registry=self.registry)
        self.assertAlmostEqual(circle.area(), 12.56637, places=5)

    def test_triangle_area(self):
        triangle = create_shape("triangle", 3, 4, 5, registry=self.registry)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_is_right(self):
        triangle = create_shape("triangle", 3, 4, 5, registry=self.registry)
        self.assertTrue(triangle.is_right())

    def test_triangle_not_right(self):
        triangle = create_shape("triangle", 3, 4, 6, registry=self.registry)
        self.assertFalse(triangle.is_right())

    def test_unknown_shape(self):
        with self.assertRaises(ValueError):
            create_shape("hexagon", 1, registry=self.registry)

    def test_dynamic_shape_registration(self):
        @self.registry.register("square")
        class Square(Shape):
            def __init__(self, side: float):
                self.side = side

            def area(self) -> float:
                return self.side * self.side

        sq = create_shape("square", 4, registry=self.registry)
        self.assertIsNotNone(sq)
        self.assertEqual(sq.area(), 16)

        self.assertIn("square", self.registry.list_shapes())

if __name__ == "__main__":
    unittest.main()
