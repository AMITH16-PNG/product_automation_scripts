from selenium.webdriver.common.by import By
from conftest import driver
from pages.base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    """Page Object for the GTaskZ Login Page"""
    
    # Locators for Login Page (Email/Phone input)
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Email Address/Phone Number']")
    SEND_OTP_BUTTON = (By.XPATH, "//button[contains(text(), 'Send OTP')]")
    
    # Locators for OTP Page - 4 input boxes for OTP digits
    OTP_INPUT_BOXES = (By.CSS_SELECTOR, "input[type='tel']")
    OTP_BOX_1 = (By.XPATH, "(//input[@type='tel' or contains(@class,'MuiInputBase-input')])[1]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    GO_BACK_LINK = (By.XPATH, "//*[contains(text(), 'Go Back')]")
    RESEND_OTP_LINK = (By.XPATH, "//*[contains(text(), 'Resend OTP')]")

    # Locators for logout
    PROFILE_CLICK = (By.XPATH, "//img[@alt='down']")
    LOGOUT = (By.XPATH, "//p[text()='Logout']")

    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_email(self, email):
        """Enter email or phone number in the input field"""
        self.enter_text(self.EMAIL_INPUT, email)
    
    def click_send_otp(self):
        """Click the Send OTP button"""
        self.click(self.SEND_OTP_BUTTON)
    
    def is_otp_page_displayed(self):
        """Check if OTP page is displayed"""
        return self.is_element_visible(self.LOGIN_BUTTON, timeout=15)
    
    def enter_otp_digit(self, index, digit):
        """Enter a single OTP digit by clicking the corresponding number button
        
        Args:
            index: Position of OTP box (0-3)
            digit: The digit to enter (0-9)
        """
        # Click on the OTP number pad button corresponding to the digit
        digit_button = (By.XPATH, f"//button[contains(@class, 'MuiButton') and text()='{digit}']")
        self.click(digit_button)
    
    def enter_otp(self, otp_code: str):
        """Enter OTP into all OTP input boxes.
    
        Args:
            otp_code (str): OTP value, e.g. "1234"
        """
        # Wait for OTP inputs to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "otp-input-0"))
        )
        
        # Enter each digit into individual OTP input boxes by their specific ID
        for i, digit in enumerate(otp_code):
            otp_input_id = f"otp-input-{i}"
            try:
                # Wait for the specific input to be clickable
                otp_box = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.ID, otp_input_id))
                )
                
                # Click on the input to focus it
                otp_box.click()
                time.sleep(0.1)
                
                # Clear existing value and enter the digit
                otp_box.send_keys(Keys.CONTROL + "a")
                otp_box.send_keys(Keys.DELETE)
                otp_box.send_keys(digit)
                time.sleep(0.3)
                
            except Exception as e:
                print(f"Error entering digit {digit} in {otp_input_id}: {e}")
                # Fallback: Try using JavaScript to set value
                self.driver.execute_script(
                    f"document.getElementById('{otp_input_id}').value = '{digit}';"
                )
                # Trigger input event for React/MUI to recognize the change
                self.driver.execute_script(
                    f"""
                    var input = document.getElementById('{otp_input_id}');
                    var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                    nativeInputValueSetter.call(input, '{digit}');
                    var event = new Event('input', {{ bubbles: true }});
                    input.dispatchEvent(event);
                    """
                )
                time.sleep(0.2)

    
    def click_login(self):
        """Click the Login button"""
        self.click(self.LOGIN_BUTTON)
    
    def click_go_back(self):
        """Click the Go Back link"""
        self.click(self.GO_BACK_LINK)
    
    def click_resend_otp(self):
        """Click the Resend OTP link"""
        self.click(self.RESEND_OTP_LINK)
    
    def login_with_email(self, email):
        """Perform login step 1: Enter email and send OTP
        
        Args:
            email: Email address or phone number
        """
        self.enter_email(email)
        self.click_send_otp()
    
    def complete_otp_login(self, otp_code):
        """Complete login step 2: Enter OTP and click login
        
        Args:
            otp_code: 4-digit OTP code
        """
        self.enter_otp(otp_code)
        self.click_login()
    
    def full_login(self, email, otp_code, manual_otp_wait=30):
        """Perform complete login process
        
        Args:
            email: Email address or phone number
            otp_code: 4-digit OTP code (or None for manual entry)
            manual_otp_wait: Seconds to wait for manual OTP entry
        """
        self.login_with_email(email)
        
        # Wait for OTP page
        if self.is_otp_page_displayed():
            if otp_code:
                self.complete_otp_login(otp_code)
            else:
                # Wait for manual OTP entry
                print(f"Please enter OTP manually within {manual_otp_wait} seconds...")
                time.sleep(manual_otp_wait)


    def logout(self):
        """Logout from the application"""
        try:
            print("DEBUG: Attempting to logout...")
            
            # Wait for page to be stable
            time.sleep(2)
            
            # Click profile dropdown (img with alt="down")
            try:
                profile_elem = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.PROFILE_CLICK)
                )
                profile_elem.click()
                print("✓ Clicked profile dropdown")
            except Exception as e:
                print(f"⚠ Could not find profile dropdown: {e}")
                return
            
            time.sleep(1)  # Wait for dropdown menu to appear
            
            # Click Logout (p element with text "Logout")
            try:
                logout_elem = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(self.LOGOUT)
                )
                logout_elem.click()
                print("✓ Clicked Logout")
            except Exception as e:
                print(f"⚠ Could not find Logout button: {e}")
                # Try alternative locator
                try:
                    logout_elem = self.driver.find_element(By.XPATH, "//li[@role='menuitem']//p[text()='Logout']")
                    logout_elem.click()
                    print("✓ Clicked Logout (alternative)")
                except:
                    print("⚠ Logout element not found")
                    return
            
            time.sleep(2)
            print("✓ Logout completed")
            
        except Exception as e:
            print(f"⚠ Logout failed: {e}")



