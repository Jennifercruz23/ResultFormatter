# test_resultformatter.py
"""
Tests for ResultFormatter module.
"""

import unittest
from resultformatter import ResultFormatter

class TestResultFormatter(unittest.TestCase):
    """Test cases for ResultFormatter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ResultFormatter()
        self.assertIsInstance(instance, ResultFormatter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ResultFormatter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
