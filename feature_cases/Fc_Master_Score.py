import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Master_Score(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Master_Score tests..")

#Feature testcases

    def test_t001_Master_Score(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Master_Score.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Master_Score class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
