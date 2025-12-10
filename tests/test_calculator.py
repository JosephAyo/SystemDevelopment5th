"""
Test suite for the Calculator class.
"""

import multiprocessing
try:
    multiprocessing.set_start_method('fork')
except RuntimeError:
    pass

# Patch multiprocessing.set_start_method to be a no-op.
# This prevents a RuntimeError when mutmut tries to set the start method to 'fork'
# where the multiprocessing context might already be initialized by pytest.
def _noop_set_start_method(method, force=False):
    pass
multiprocessing.set_start_method = _noop_set_start_method

import pytest
from calculator.calculator import Calculator, InvalidInputException


@pytest.fixture
def calc():
    """Create a Calculator instance for tests."""
    return Calculator()


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # Arrange
        a = 10
        b = 3
        expected = 7

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self, calc):
        """Test subtracting negative numbers."""
        # Arrange
        a = -10
        b = -3
        expected = -7

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # Arrange
        a = 4
        b = 3
        expected = 12

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_with_zero(self, calc):
        """Test multiplying with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        a = 10
        b = 2
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_by_zero(self, calc):
        """Test dividing by zero raises ValueError."""
        # Arrange
        a = 10
        b = 0

        # Act & Assert
        with pytest.raises(ValueError, match="^Cannot divide by zero$"):
            calc.divide(a, b)

    def test_divide_floats(self, calc):
        """Test dividing floating point numbers."""
        # Arrange
        a = 5.0
        b = 2.0
        expected = 2.5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestInputValidation:
    """Tests for input validation."""

    def test_input_too_large(self, calc):
        """Test that input larger than 1,000,000 raises InvalidInputException."""
        # Arrange
        a = 1000001
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException, match="Inputs must be between -1000000 and 1000000"):
            calc.add(a, b)

    def test_input_too_small(self, calc):
        """Test that input smaller than -1,000,000 raises InvalidInputException."""
        # Arrange
        a = -1000001
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException, match="Inputs must be between -1000000 and 1000000"):
            calc.add(a, b)

    def test_boundary_values(self, calc):
        """Test boundary values are accepted."""
        # MIN_VALUE
        assert calc.add(calc.MIN_VALUE, 0) == calc.MIN_VALUE
        assert calc.add(0, calc.MIN_VALUE) == calc.MIN_VALUE

        # MAX_VALUE
        assert calc.add(calc.MAX_VALUE, 0) == calc.MAX_VALUE
        assert calc.add(0, calc.MAX_VALUE) == calc.MAX_VALUE



