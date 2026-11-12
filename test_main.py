import unittest
from main import run
class TestRun(unittest.TestCase):
 def test_smoke(self):
  self.assertIsNotNone(run("a"))
if __name__=="__main__": unittest.main()
