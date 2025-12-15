from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import random
import string
import time
from datetime import datetime



class SystemAdministrationPage(BasePage):
    """Page Object for the GTaskZ System Administration Page"""
    
    # Sidebar Menu - based on screenshot showing "SYSTEM ADMINISTRATION" text in uppercase
    SA_MENU = (By.XPATH, "//p[contains(text(),'System Administration')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_SA_menu(self):
        """Click on System Administration menu in sidebar"""
        time.sleep(1)
        locators = [
            # The text appears as uppercase "SYSTEM ADMINISTRATION" in the UI
            (By.XPATH, "//p[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'system administration')]"),
            (By.XPATH, "//p[contains(@class,'MuiTypography')][contains(text(),'SYSTEM ADMINISTRATION')]"),
            (By.XPATH, "//p[contains(@class,'MuiTypography')][contains(text(),'System Administration')]"),
            (By.XPATH, "//*[contains(text(),'SYSTEM ADMINISTRATION')]"),
            (By.XPATH, "//div[contains(@class,'MuiBox-root')]//p[contains(text(),'System')]"),
            # From screenshot: p.MuiTypography-root.MuiTypography-body1.css-5ajsgi
            (By.CSS_SELECTOR, "p.MuiTypography-body1.css-5ajsgi"),
        ]
        
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                # FAIL in many real UI cases because the element is not visible or not in viewport
                # ElementNotInteractableException, ElementClickInterceptedException
                time.sleep(0.3)
                element.click()
                print("[OK] Clicked System Administration menu")
                return True
            except:
                continue
        
        # Try JavaScript click as fallback
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(loc))
                self.driver.execute_script("arguments[0].click();", element)
                # Bypasses Selenium’s normal .click(), Directly triggers the DOM click event using JavaScript
                # Aviods Visibility/Interactable issues
                print("[OK] Clicked System Administration menu (JS)")
                return True
            except:
                continue
        
        print("[WARNING] Could not click System Administration menu")
        return False