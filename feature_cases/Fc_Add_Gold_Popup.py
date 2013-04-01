import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Add_Gold_Popup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Add_Gold_Popup tests..")

#Feature testcases

    def test_t001_Add_Gold_Popup(self):
        h=self._h
        try:
            h.click("#buygold")
            state=h.is_displayed("#goldmenu-popup")
            self.assertTrue(state)
        except:
            h.screenshot("test_t001_Add_Gold_Popup.png")
            raise


    def test_t002_Add_Gold_Popup_Close_Button(self):
        h=self._h
        try:
	    h.click("#buygold")
            h.click(".ui-dialog-titlebar-close")
            state=h.is_displayed("#goldmenu-popup")
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Add_Gold_Popup_Close_Button.png")
            raise


    def test_t003_Add_Gold_Popup_Title(self):
        h=self._h
        try:
            h.click("#buygold")
	    title = h.execute_script("return $('#goldmenu-popup').find('.title').html()")
	    #print title
	    if title == "Add Gold":
		state = "True"
	    else:
		state = "False"	
	    self.assertTrue(state)
        except:
            h.screenshot("test_t003_Add_Gold_Popup_Title.png")
            raise


    def test_t004_Add_Gold_Popup_Select_Credits(self):
        h=self._h
        try:
            h.click("#buygold")
	    h.execute_script("$('.options').find('input')[0].click()")
	    state = h.execute_script("return $('.options').find('input').is(':checked')")
            self.assertTrue(state)
	    h.execute_script("$('.options').find('input')[1].click()")
            state = h.execute_script("return $('.options').find('input').is(':checked')")
            self.assertTrue(state)
            h.execute_script("$('.options').find('input')[2].click()")
            state = h.execute_script("return $('.options').find('input').is(':checked')")
            self.assertTrue(state)
   	    h.execute_script("$('.options').find('input')[3].click()")
            state = h.execute_script("return $('.options').find('input').is(':checked')")
            self.assertTrue(state)
            h.execute_script("$('.options').find('input')[4].click()")
            state = h.execute_script("return $('.options').find('input').is(':checked')")
            self.assertTrue(state)
            h.execute_script("$('.options').find('input')[5].click()")
            state = h.execute_script("return $('.options').find('input').is(':checked')")
            self.assertTrue(state)
 
        except:
            h.screenshot("test_t004_Add_Gold_Popup_Select_Credits.png")
            raise


    def test_t005_Add_Gold_Popup_Add_Button(self):
        h=self._h
        try:
            h.click("#buygold")
	    title = h.execute_script("return $('#goldmenu-popup').find('.button').html()")
	    if title == "Add":
                state = "True"
            else:
                state = "False"
            self.assertTrue(state)

        except:
            h.screenshot("test_t005_Add_Gold_popup_Add_Button.png")
            raise


    def test_t006_Add_Gold_Popup_Earn_Button(self):
        h=self._h
        try:
            h.click("#buygold")
	    title = h.execute_script("return $('#goldmenu-popup').find('.earngold').html()")
	    if title == "Earn Gold":
                state = "True"
            else:
                state = "False"
            self.assertTrue(state)
	    h.click(".ui-dialog-titlebar-close")
        except:
            h.screenshot("test_t006_Add_Gold_Popup_Earn_button.png")
            raise

    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Add_Gold_Popup class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
