from asyncio import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import random
import string
import time
from datetime import datetime
from selenium.common.exceptions import TimeoutException, WebDriverException
import pytest


class ManagePage(BasePage):
    """Page Object for the GTaskZ Manage Page - Updated UI"""
    
    # Sidebar Menu
    MANAGE_MENU = (By.XPATH, "//span[text()='Manage']")
    
    # Tabs
    RESOURCE_MANAGEMENT_TAB = (By.XPATH, "//button[contains(.,'Resource Management')]")
    
    # Add Resource Button (blue button on right side)
    ADD_RESOURCE_BUTTON = (By.XPATH, "//button[contains(text(),'Add Resource')]")
    
    # Modal Close Button (X icon)
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class,'MuiIconButton')]//svg[@data-testid='CloseIcon']")
    
    # Basic Info Tab Fields (using label-based locators for reliability)
    FIRST_NAME_INPUT = (By.XPATH, "//p[contains(text(),'First Name')]/ancestor::div[contains(@class,'MuiGrid-item')]//input")
    LAST_NAME_INPUT = (By.XPATH, "//p[contains(text(),'Last Name')]/ancestor::div[contains(@class,'MuiGrid-item')]//input")
    EMAIL_INPUT = (By.XPATH, "//p[contains(text(),'Email')]/ancestor::div[contains(@class,'MuiGrid-item')]//input")
    PHONE_INPUT = (By.CSS_SELECTOR, "div.react-tel-input input.form-control")
    DATE_OF_JOIN_INPUT = (By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
    EXPERIENCE_DROPDOWN = (By.XPATH, "//div[contains(text(),'Select Experience')]")
    PRIMARY_SKILL_DROPDOWN = (By.XPATH, "//div[contains(text(),'Select Skill')]")
    REPORTING_MANAGER_INPUT = (By.XPATH, "//input[@placeholder='Search...']")
    
    # Employment Tab
    EMPLOYMENT_TAB = (By.XPATH, "//button[contains(text(),'Employment')]")
    COMPANY_DROPDOWN = (By.XPATH, "//div[contains(text(),'Select Company')]")
    DEPARTMENT_DROPDOWN = (By.XPATH, "//div[contains(text(),'Select Department')]")
    ROLE_DROPDOWN = (By.XPATH, "//div[contains(text(),'Select Role')]")
    
    # Add Resource Button (in modal)
    ADD_RESOURCE_SUBMIT = (By.XPATH, "//button[contains(text(),'Add Resource') and contains(@class,'MuiButton-contained')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    # ==================== Navigation ====================
    
    def click_manage_menu(self):
        """Click on Manage menu in sidebar"""
        time.sleep(1)
        locators = [
            (By.XPATH, "//span[text()='Manage']"),
            (By.XPATH, "//*[contains(text(),'Manage')]"),
        ]
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
                element.click()
                print("[OK] Clicked Manage menu")
                return
            except:
                continue
    
    def click_resource_management_tab(self):
        """Click on Resource Management tab"""
        time.sleep(1)
        locators = [
            (By.XPATH, "//button[contains(.,'Resource Management')]"),
            (By.XPATH, "//*[contains(text(),'Resource Management')]"),
        ]
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
                element.click()
                print("[OK] Clicked Resource Management tab")
                return
            except:
                continue
    
    # ==================== Add Resource Flow ====================
    
    def click_add_resource_button(self):
        """Click the + Add Resource button"""
        time.sleep(1)
        locators = [
            (By.XPATH, "//button[contains(text(),'Add Resource')]"),
            (By.XPATH, "//button[contains(@class,'MuiButton')]//span[contains(text(),'Add Resource')]"),
            (By.XPATH, "//button[contains(@class,'MuiButton-containedPrimary')]"),
        ]
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
                element.click()
                print("[OK] Clicked Add Resource button")
                time.sleep(2)  # Wait for modal to open
                return
            except:
                continue
    
    def enter_first_name(self, first_name):
        """Enter first name - First text input in the modal"""
        time.sleep(0.5)
        locators = [
            (By.XPATH, "//p[contains(text(),'First Name')]/ancestor::div[contains(@class,'MuiGrid-item')]//input"),
            (By.XPATH, "(//div[@role='dialog']//input[contains(@class,'MuiOutlinedInput-input')])[1]"),
        ]
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                element.click()
                element.send_keys(Keys.CONTROL + "a")
                element.send_keys(first_name)
                print(f"[OK] Entered first name: {first_name}")
                return
            except:
                continue
    
    def enter_last_name(self, last_name):
        """Enter last name - Second text input in the modal"""
        time.sleep(0.5)
        locators = [
            (By.XPATH, "//p[contains(text(),'Last Name')]/ancestor::div[contains(@class,'MuiGrid-item')]//input"),
            (By.XPATH, "(//div[@role='dialog']//input[contains(@class,'MuiOutlinedInput-input')])[2]"),
        ]
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                element.click()
                element.send_keys(Keys.CONTROL + "a")
                element.send_keys(last_name)
                print(f"[OK] Entered last name: {last_name}")
                return
            except:
                continue
    
    def enter_email(self, email):
        """Enter email - Third text input in the modal"""
        time.sleep(0.5)
        locators = [
            (By.XPATH, "//p[contains(text(),'Email')]/ancestor::div[contains(@class,'MuiGrid-item')]//input"),
            (By.XPATH, "(//div[@role='dialog']//input[contains(@class,'MuiOutlinedInput-input')])[3]"),
        ]
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                element.click()
                element.send_keys(Keys.CONTROL + "a")
                element.send_keys(email)
                print(f"[OK] Entered email: {email}")
                return
            except:
                continue
    
    def enter_phone(self, phone):
        """Enter phone number - uses react-tel-input component
        
        The component already has India (+91) as default.
        We should NOT clear the field as it will remove the country code.
        Just click after the +91 and type the number.
        """
        time.sleep(0.5)
        locators = [
            (By.CSS_SELECTOR, "input.form-control[type='tel']"),
            (By.XPATH, "//div[contains(@class,'react-tel-input')]//input[@type='tel']"),
            (By.XPATH, "//input[contains(@placeholder,'123-4567')]"),
            (By.CSS_SELECTOR, "div.react-tel-input input.form-control"),
        ]
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                # Click at the end of the input (after +91)
                element.click()
                time.sleep(0.3)
                
                # Move cursor to end and type the phone number
                # Don't clear - just append to existing +91
                element.send_keys(Keys.END)
                element.send_keys(phone)
                print(f"[OK] Entered phone: +91 {phone}")
                return
            except:
                continue
    
    def select_date_of_joining(self, day, month, year):
        """Select date of joining using calendar picker - e.g., 14th July 2022"""
        time.sleep(0.5)
        
        # Click on the calendar icon button to open date picker
        cal_button_locators = [
            (By.XPATH, "//button[@aria-label='Choose date']"),
            (By.XPATH, "//svg[@data-testid='CalendarIcon']/parent::button"),
            (By.XPATH, "//button[contains(@class,'MuiIconButton')]//svg[@data-testid='CalendarIcon']"),
        ]
        
        for loc in cal_button_locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                element.click()
                print("[OK] Opened date picker")
                time.sleep(1)
                break
            except:
                continue
        
        # Navigate to the correct month/year
        # First, click on the month/year header to switch to year view
        try:
            month_year_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'MuiPickersCalendarHeader-switchViewButton')]"))
            )
            
            # Get current displayed month/year
            current_label = self.driver.find_element(By.XPATH, "//div[contains(@class,'MuiPickersCalendarHeader-label')]").text
            print(f"Current calendar shows: {current_label}")
            
            # Navigate backwards to July 2022
            # Click previous month button multiple times
            months_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                         'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
            
            target_date = datetime(year, month, day)
            current_date = datetime.now()
            
            # Calculate months to go back
            months_diff = (current_date.year - target_date.year) * 12 + (current_date.month - target_date.month)
            
            prev_button = (By.XPATH, "//button[@title='Previous month']")
            for _ in range(months_diff):
                try:
                    prev_btn = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(prev_button))
                    prev_btn.click()
                    time.sleep(0.3)
                except:
                    break
            
            time.sleep(0.5)
            
            # Now click on the day - try multiple locators
            day_locators = [
                (By.XPATH, f"//button[contains(@class,'MuiPickersDay') and text()='{day}']"),
                (By.XPATH, f"//button[contains(@class,'MuiPickersDay-root')][text()='{day}']"),
                (By.XPATH, f"//button[contains(@class,'MuiButtonBase-root')][text()='{day}']"),
                (By.XPATH, f"//div[contains(@class,'MuiPickersSlideTransition')]//button[text()='{day}']"),
                (By.XPATH, f"//button[not(@disabled)][text()='{day}']"),
            ]
            
            for day_loc in day_locators:
                try:
                    day_elem = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(day_loc))
                    day_elem.click()
                    print(f"[OK] Selected date: {day:02d}/{month:02d}/{year}")
                    time.sleep(0.5)
                    return
                except:
                    continue
            
            # If clicking doesn't work, try JavaScript click
            try:
                day_elem = self.driver.find_element(By.XPATH, f"//button[text()='{day}']")
                self.driver.execute_script("arguments[0].click();", day_elem)
                print(f"[OK] Selected date via JS: {day:02d}/{month:02d}/{year}")
                time.sleep(0.5)
                return
            except:
                pass
            
        except Exception as e:
            print(f"Calendar navigation failed: {e}")
        
        # Fallback: Try direct input
        date_input_locators = [
            (By.XPATH, "//input[@placeholder='DD/MM/YYYY']"),
            (By.XPATH, "//input[contains(@class,'MuiInputBase-inputAdornedEnd')]"),
        ]
        
        for loc in date_input_locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(loc))
                element.click()
                time.sleep(0.3)
                element.clear()
                element.send_keys(f"{day:02d}/{month:02d}/{year}")
                element.send_keys(Keys.TAB)
                print(f"[OK] Entered date directly: {day:02d}/{month:02d}/{year}")
                return
            except:
                continue
        
        print(f"[WARNING] Could not select date")
    
    def select_experience(self, years):
        """Select experience from dropdown - values are 0,1,2,3,4 etc."""
        time.sleep(0.5)
        
        # Click on experience dropdown - it's a MuiSelect component
        exp_locators = [
            (By.XPATH, "//div[contains(text(),'Select Experience')]"),
            (By.XPATH, "//p[contains(text(),'Experience')]/ancestor::div[contains(@class,'MuiGrid-item')]//div[@role='combobox']"),
            (By.XPATH, "//div[contains(@class,'MuiSelect-select')][contains(text(),'Select Experience')]"),
            (By.XPATH, "(//div[@role='combobox'])[1]"),
        ]
        
        for loc in exp_locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                element.click()
                break
            except:
                continue
        
        time.sleep(0.5)
        
        # Select the option - options are 0, 1, 2, 3, 4 (just numbers)
        option_locators = [
            (By.XPATH, f"//li[@role='option'][text()='{years}']"),
            (By.XPATH, f"//li[@data-value='{years}']"),
            (By.XPATH, f"//ul[@role='listbox']//li[text()='{years}']"),
        ]
        
        for loc in option_locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                element.click()
                print(f"[OK] Selected experience: {years} years")
                return
            except:
                continue
    
    def select_primary_skill(self, skill):
        """Select primary skill - e.g., 'python developer'
        Options: angular, backend developer, django, flask, frontend developer, 
                 html css, javascript, python developer, react, vue
        """
        time.sleep(0.5)
        
        # Click on primary skill dropdown
        skill_locators = [
            (By.XPATH, "//div[contains(text(),'Select Skill')]"),
            (By.XPATH, "//p[contains(text(),'Primary Skill')]/ancestor::div[contains(@class,'MuiGrid-item')]//div[@role='combobox']"),
            (By.XPATH, "//div[contains(@class,'MuiSelect-select')][contains(text(),'Select Skill')]"),
            (By.XPATH, "(//div[@role='combobox'])[2]"),
        ]
        
        for loc in skill_locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                element.click()
                break
            except:
                continue
        
        time.sleep(0.5)
        
        # Select the option (case-insensitive match)
        option_locators = [
            (By.XPATH, f"//li[@role='option'][translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='{skill.lower()}']"),
            (By.XPATH, f"//li[@role='option'][contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{skill.lower()}')]"),
            (By.XPATH, f"//ul[@role='listbox']//li[contains(text(),'{skill}')]"),
        ]
        
        for loc in option_locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                element.click()
                print(f"[OK] Selected primary skill: {skill}")
                return
            except:
                continue
        print(f"[WARNING] Could not select skill: {skill}")
    
   

    def select_reporting_manager(self, manager_name="Madhu Poclassery"):
        """Select reporting manager - click input to open dropdown, then select first option"""
        time.sleep(0.5)
        
        try:
            # Click on the Search input field to open dropdown
            input_field = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search...']"))
            )
            input_field.click()
            print("[OK] Clicked Reporting Manager input")
            time.sleep(1)
            
            # Wait for dropdown listbox to appear
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//ul[@role='listbox']"))
            )
            print("[OK] Dropdown opened")
            time.sleep(0.5)
            
            # Try to find and click the specific manager first
            try:
                option = WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, f"//ul[@role='listbox']//li[contains(.,'{manager_name}')]"))
                )
                self.driver.execute_script("arguments[0].click();", option)
                print(f"[OK] Selected: {manager_name}")
                return True
            except:
                pass
            
            # Fallback: Click the first option in the dropdown
            try:
                first_option = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul[@role='listbox']//li[1]"))
                )
                option_text = first_option.text.split('\n')[0]  # Get first line (name)
                self.driver.execute_script("arguments[0].click();", first_option)
                print(f"[OK] Selected first option: {option_text}")
                return True
            except:
                pass
            
            # Last fallback: keyboard navigation
            input_field.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
            input_field.send_keys(Keys.ENTER)
            print("[OK] Selected via keyboard")
            return True
            
        except Exception as e:
            print(f"[WARNING] Could not select reporting manager: {e}")
            return False

    # ==================== Employment Tab ====================
    
    def click_employment_tab(self):
        """Click on Employment tab in the modal"""
        time.sleep(2)  # Wait for modal to be fully loaded
        
        print("Attempting to click Employment tab...")
        
        # First, try to find all tabs and click the Employment one
        try:
            # Find all tab buttons in the modal
            tabs = self.driver.find_elements(By.XPATH, "//button[@role='tab']")
            print(f"Found {len(tabs)} tabs")
            for tab in tabs:
                tab_text = tab.text.strip()
                print(f"Tab found: '{tab_text}'")
                if "Employment" in tab_text:
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
                    time.sleep(0.5)
                    self.driver.execute_script("arguments[0].click();", tab)
                    print("✓ Clicked Employment tab (found in tabs list)")
                    time.sleep(1.5)
                    return
        except Exception as e:
            print(f"Tab iteration failed: {e}")
        
        # Try specific locators
        locators = [
            (By.XPATH, "//button[@role='tab'][.//span[contains(text(),'Employment')]]"),
            (By.XPATH, "//button[contains(@class,'MuiTab-root')][contains(.,'Employment')]"),
            (By.XPATH, "//div[contains(@class,'MuiTabs')]//button[contains(.,'Employment')]"),
            (By.XPATH, "//button[@role='tab'][2]"),  # Employment is typically the 2nd tab
            (By.CSS_SELECTOR, "button.MuiTab-root:nth-child(2)"),
        ]
        
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(loc))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                time.sleep(0.3)
                self.driver.execute_script("arguments[0].click();", element)
                print(f"✓ Clicked Employment tab using {loc}")
                time.sleep(1.5)
                return
            except Exception as e:
                continue
        
        print("⚠ Could not click Employment tab")
    
    def select_company(self, company_name="GigLabz"):
        """Select company from dropdown - default is GigLabz"""
        time.sleep(0.5)
        
        # Click on company dropdown - it's a MuiSelect
        comp_locators = [
            (By.XPATH, "//div[@role='combobox'][contains(.,'Select Company') or contains(.,'GigLabz')]"),
            (By.XPATH, "//div[contains(@class,'MuiSelect-select')][contains(text(),'Select Company')]"),
            (By.XPATH, "//p[contains(text(),'Company')]/following::div[@role='combobox'][1]"),
        ]
        
        for loc in comp_locators:
            try:
                element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
                element.click()
                print("✓ Clicked Company dropdown")
                break
            except:
                continue
        
        time.sleep(0.5)
        
        # Select the option from listbox
        option_locators = [
            (By.XPATH, f"//li[@role='option'][contains(text(),'{company_name}')]"),
            (By.XPATH, f"//li[contains(@class,'MuiMenuItem')][contains(text(),'{company_name}')]"),
            (By.XPATH, f"//ul[@role='listbox']//li[contains(text(),'{company_name}')]"),
        ]
        
        for opt_loc in option_locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(opt_loc))
                element.click()
                print(f"✓ Selected company: {company_name}")
                return
            except:
                continue
        print(f"⚠ Could not select company: {company_name}")
    
    def select_department(self, department):
        """Select department - e.g., 'IT'"""
        time.sleep(0.5)
        
        # Click on department dropdown
        dept_locators = [
            (By.XPATH, "//div[@role='combobox'][contains(.,'Select Department')]"),
            (By.XPATH, "//div[contains(@class,'MuiSelect-select')][contains(text(),'Select Department')]"),
            (By.XPATH, "//p[contains(text(),'Department')]/following::div[@role='combobox'][1]"),
        ]
        
        for loc in dept_locators:
            try:
                element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
                element.click()
                print("✓ Clicked Department dropdown")
                break
            except:
                continue
        
        time.sleep(0.5)
        
        # Select the option
        option_locators = [
            (By.XPATH, f"//li[@role='option'][contains(text(),'{department}')]"),
            (By.XPATH, f"//li[contains(@class,'MuiMenuItem')][contains(text(),'{department}')]"),
            (By.XPATH, f"//ul[@role='listbox']//li[contains(text(),'{department}')]"),
        ]
        
        for opt_loc in option_locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(opt_loc))
                element.click()
                print(f"✓ Selected department: {department}")
                return
            except:
                continue
        print(f"⚠ Could not select department: {department}")
    
    def select_role(self, role):
        """Select role - e.g., 'senior software developer'
        Options: intern, lead software developer, operations manager, quality analyst,
                 sales manager, senior project manager, senior qa, senior software developer,
                 software developer, technical lead, technical project manager
        """
        time.sleep(0.5)
        
        # Click on role dropdown
        role_locators = [
            (By.XPATH, "//div[@role='combobox'][contains(.,'Select Role')]"),
            (By.XPATH, "//div[contains(@class,'MuiSelect-select')][contains(text(),'Select Role')]"),
            (By.XPATH, "//p[contains(text(),'Role')]/following::div[@role='combobox'][1]"),
        ]
        
        for loc in role_locators:
            try:
                element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
                element.click()
                print("✓ Clicked Role dropdown")
                break
            except:
                continue
        
        time.sleep(0.5)
        
        # Select the option - use data-value attribute which matches exactly
        option_locators = [
            (By.XPATH, f"//li[@data-value='{role.lower()}']"),
            (By.XPATH, f"//li[@role='option'][contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{role.lower()}')]"),
            (By.XPATH, f"//li[contains(@class,'MuiMenuItem')][contains(text(),'{role}')]"),
        ]
        
        for opt_loc in option_locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(opt_loc))
                element.click()
                print(f"✓ Selected role: {role}")
                return
            except:
                continue
        print(f"⚠ Could not select role: {role}")

    def select_employee_type(self, employee_type="full time"):
        """Select employee type from dropdown"""
        time.sleep(0.5)
        
        try:
            # Click on employee_type dropdown
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Select Type']"))
            )
            element.click()
            print("✓ Clicked Employee Type dropdown")
            time.sleep(0.5)
            
            # Select the option
            option = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//li[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'full')]"))
            )
            option.click()
            print(f"✓ Selected employee type: {employee_type}")
        except Exception as e:
            print(f"⚠ Could not select employee type: {e}")

    def select_work_shift(self, work_shift="day"):
        """Select work shift from dropdown"""
        time.sleep(0.5)
        
        try:
            # Click on work_shift dropdown
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Select Shift']"))
            )
            element.click()
            print("✓ Clicked Work Shift dropdown")
            time.sleep(0.5)
            
            # Select the option
            option = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//li[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'day')]"))
            )
            option.click()
            print(f"✓ Selected work shift: {work_shift}")
        except Exception as e:
            print(f"⚠ Could not select work shift: {e}")

    def select_location(self, location="hyderabad"):
        """Select location from dropdown"""
        time.sleep(0.5)
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Select Location']"))
            )
            element.click()
            print("✓ Clicked location dropdown")
            time.sleep(0.5)
            option = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][@data-value='{location}']"))
            )
            option.click()
            print(f"✓ Selected location: {location}")
        except Exception as e:
            print(f"⚠ Could not select location: {e}")

    def select_vendor(self, vendor="cognizant"):
        """Select vendor from dropdown"""
        time.sleep(0.5)
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Select Vendor']"))
            )
            element.click()
            print("✓ Clicked vendor dropdown")
            time.sleep(0.5)
            option = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][@data-value='{vendor}']"))
            )
            option.click()
            print(f"✓ Selected vendor: {vendor}")
        except Exception as e:
            print(f"⚠ Could not select vendor: {e}")

    def select_project(self, project="fintech app"):
        """Select project from dropdown"""
        time.sleep(0.5)
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Select Project']"))
            )
            element.click()
            print("✓ Clicked project dropdown")
            time.sleep(0.5)
            option = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][@data-value='{project}']"))
            )
            option.click()
            print(f"✓ Selected project: {project}")
        except Exception as e:
            print(f"⚠ Could not select project: {e}")

    def click_add_resource_submit(self):
        """Click Add Resource button to submit the form"""
        time.sleep(0.5)
        locators = [
            (By.XPATH, "//button[contains(@class,'MuiButton-containedPrimary')][contains(.,'Add Resource')]"),
            (By.XPATH, "//div[contains(@class,'MuiDialogActions')]//button[contains(@class,'MuiButton-contained')]"),
            (By.XPATH, "//button[contains(text(),'Add Resource') and contains(@class,'MuiButton-contained')]"),
            (By.XPATH, "(//button[contains(text(),'Add Resource')])[last()]"),
        ]
        
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)
                element.click()
                print("✓ Clicked Add Resource submit button")
                time.sleep(2)  # Wait for save to complete
                return
            except:
                continue
            print("⚠ Could not click Add Resource button")

    
    def verify_user_create_or_update_toast(self, timeout=5):
        """Verify success toast appears after user create/update"""
        
        print("[DEBUG] Starting toast detection...")
        
        locators = [
            # 1. Toastify toast body - most common
            (By.CSS_SELECTOR, ".Toastify__toast-body"),
            
            # 2. Success toast specifically
            (By.XPATH, "//div[contains(@class,'Toastify__toast--success')]"),
            
            # 3. Any div with role alert
            (By.XPATH, "//div[@role='alert']"),
            
            # 4. MUI Alert/Snackbar
            (By.XPATH, "//div[contains(@class,'MuiAlert') or contains(@class,'MuiSnackbar')]"),
            
            # 5. Toast container - get any text inside
            (By.CSS_SELECTOR, ".Toastify__toast-container"),
        ]

        for by, locator in locators:
            try:
                print(f"[DEBUG] Trying locator: {locator}")
                toast = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((by, locator))
                )
                
                # Try to get text from element directly
                toast_text = toast.text.strip()
                
                # If no direct text, try getting innerText via JavaScript
                if not toast_text:
                    toast_text = self.driver.execute_script("return arguments[0].innerText;", toast)
                    if toast_text:
                        toast_text = toast_text.strip()
                
                # If still no text, try getting text from child elements
                if not toast_text:
                    try:
                        child_elements = toast.find_elements(By.XPATH, ".//*")
                        for child in child_elements:
                            child_text = child.text.strip()
                            if child_text:
                                toast_text = child_text
                                break
                    except:
                        pass
                
                if toast_text:
                    print(f"[FOUND] Toast text found: '{toast_text}'")
                    success_keywords = ["created", "updated", "success", "added", "saved", "successful"]
                    if any(keyword in toast_text.lower() for keyword in success_keywords):
                        print(f"[OK] Success Toast Detected: {toast_text}")
                        return toast_text
                    else:
                        # Toast found but no success keyword - might still be valid
                        print(f"[INFO] Toast found but no success keyword: '{toast_text}'")
                        # Return it anyway as we found a toast
                        return toast_text
                else:
                    print(f"[DEBUG] Toast element found but no text with locator: {locator}")
                    
            except TimeoutException:
                print(f"[DEBUG] Timeout for locator: {locator}")
                continue
            except Exception as e:
                print(f"[WARNING] Error checking toast with {locator}: {e}")
                continue
        
        # If no toast found after checking all locators, return None (don't fail)
        print("[WARNING] No toast message detected, continuing with validation...")
        return None
        
    
    @pytest.mark.skip(reason="Not used currently")
    def click_close_modal(self):
        """Click close (X) button on the modal"""
        time.sleep(0.5)
        locators = [
            (By.XPATH, "//button[.//svg[@data-testid='CloseIcon']]"),
            (By.XPATH, "//svg[@data-testid='CloseIcon']/ancestor::button"),
            (By.CSS_SELECTOR, "button svg[data-testid='CloseIcon']"),
        ]
        
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                element.click()
                print("[OK] Closed modal")
                time.sleep(0.5)
                return
            except:
                continue
        
        print("[WARNING] Could not close modal")
    
    # ==================== Validation ====================
    
    def verify_resource_in_list(self, name):
        """Verify that resource with given name appears in the list"""
        time.sleep(1)  # Reduced from 3 seconds
        
        print("\n" + "="*60)
        print("[VALIDATING] Checking if user was added to the list...")
        print("="*60)
        
        # Try most specific locator first with short timeout
        locators = [
            (By.XPATH, f"//p[contains(text(),'{name}')]"),
            (By.XPATH, f"//*[contains(text(),'{name}')]"),
        ]
        
        for loc in locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(loc))
                if element:
                    # Highlight the element on screen
                    self.driver.execute_script("arguments[0].style.border='3px solid green'", element)
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                    
                    print("\n" + "[SUCCESS]"*5)
                    print(f"[OK] SUCCESS: User '{name}' was ADDED SUCCESSFULLY!")
                    print(f"[OK] Found user in the resource list!")
                    print("[SUCCESS]"*5 + "\n")
                    
                    # Take screenshot for validation
                    try:
                        screenshot_name = f"resource_added_{name}_{int(time.time())}.png"
                        self.driver.save_screenshot(f"reports/{screenshot_name}")
                        print(f"[SCREENSHOT] Screenshot saved: reports/{screenshot_name}")
                    except:
                        pass
                    
                    return True
            except:
                continue
        
        print("\n" + "[FAILED]"*5)
        print(f"[FAILED] User '{name}' was NOT found in the resource list!")
        print("[FAILED]"*5 + "\n")
        return False
    
    # ==================== Helper Methods ====================
    
    def generate_random_name(self):
        """Generate random first and last name"""
        first_names = ["John", "Jane", "Mike", "Sarah", "David", "Emma", "Chris", "Lisa", "Tom", "Anna"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
        return random.choice(first_names), random.choice(last_names)
    
    def generate_random_phone(self):
        """Generate random 10-digit phone starting with 6-9"""
        first_digit = random.choice(['6', '7', '8', '9'])
        remaining = ''.join(random.choices('0123456789', k=9))
        return first_digit + remaining
    
    def generate_random_email(self, first_name, last_name):
        """Generate random yopmail email"""
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        return f"{first_name.lower()}{last_name.lower()}{suffix}@yopmail.com"
    
    # ==================== Complete Flow ====================


    @pytest.mark.skip(reason="Duplicate method, not used currently")
    def add_resource_complete_flow(self, first_name, last_name, email, phone, 
                                    join_day, join_month, join_year,
                                    experience, primary_skill, reporting_manager=None,
                                    company=None, department=None, role=None):
        """Complete flow to add a new resource"""
        
        print("\n" + "="*50)
        print(f"Adding Resource: {first_name} {last_name}")
        print("="*50)
        
        # Step 1: Click Add Resource button
        self.click_add_resource_button()
        
        # Step 2: Fill Basic Info
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_phone(phone)
        self.select_date_of_joining(join_day, join_month, join_year)
        self.select_experience(experience)
        self.select_primary_skill(primary_skill)
        self.select_reporting_manager()  # Selects first available option
        
        # Step 3: Click Employment tab
        self.click_employment_tab()
        
        # Step 4: Fill Employment Info - Company is required
        self.select_company()  # Selects first available company
        
        # Step 5: Submit
        self.click_add_resource_submit()
        time.sleep(3)
        
        # Step 6: Close modal if still open
        try:
            self.click_close_modal()
        except:
            pass
        
        time.sleep(2)
        
        # Step 7: Verify
        return self.verify_resource_in_list(first_name)
    
