import unittest
import pytest
class test_A(unittest.TestCase):
        def test_method(self):
                pass
        def test_method1(self):
                pass
        def test_method2(self):
                pass
        @pytest.mark.second
        def test_method3(self):
                pass
        @pytest.mark.first
        def test_method4(self):
                for i in range(10):
                        print i
                        #print a
                
