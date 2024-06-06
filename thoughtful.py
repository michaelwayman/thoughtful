import unittest


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Returns the 'stack' a package should be sorted into based on determining factors."""

    assert width > 0 and height > 0 and length > 0 and mass > 0, "Value must be greater than 0"

    # Calculate Volume
    volume = width * height * length
    # Determine if a dimension is 150 or more
    is_dim_gte_150 = width >= 150 or height >= 150 or length >= 150

    # Determine if package is bulky / heavy
    is_bulky = volume >= 1e6 or is_dim_gte_150
    is_heavy = mass >= 20

    # Return the correct stack
    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"


class SortStandardTestCase(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(1, 1, 1, 1), "STANDARD")


class SortSpecialTestCase(unittest.TestCase):
    def test_mass(self):
        self.assertEqual(sort(1, 1, 1, 20), "SPECIAL")

    def test_dimensions(self):
        self.assertEqual(sort(150, 1, 1, 1), "SPECIAL")
        self.assertEqual(sort(1, 150, 1, 1), "SPECIAL")
        self.assertEqual(sort(1, 1, 150, 1), "SPECIAL")

    def test_volume(self):
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")


class SortRejectedTestCase(unittest.TestCase):
    def test_rejected_case(self):
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")


class SortTestValueSanity(unittest.TestCase):
    def test_assertion_error(self):
        with self.assertRaises(AssertionError):
            sort(0, 0, 0, 0)


if __name__ == '__main__':
    unittest.main()
