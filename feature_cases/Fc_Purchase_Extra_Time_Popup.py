import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Purchase_Extra_Time_Popup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Purchase_Extra_Time_Popup tests..")

#Feature testcases

    def test_t001_Purchase_Extra_Time_Popup(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Purchase_Extra_Time_Popup.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Purchase_Extra_Time_Popup class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
