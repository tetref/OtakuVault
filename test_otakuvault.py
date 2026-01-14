# test_otakuvault.py
"""
Tests for OtakuVault module.
"""

import unittest
from otakuvault import OtakuVault

class TestOtakuVault(unittest.TestCase):
    """Test cases for OtakuVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OtakuVault()
        self.assertIsInstance(instance, OtakuVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OtakuVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
