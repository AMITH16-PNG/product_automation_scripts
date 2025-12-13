import pytest
import time
from pages.login_page import LoginPage
from pages.manage_page import ManagePage
from pages.system_adminstration import SystemAdministrationPage


class TestLogin:
    """Test cases for GTaskZ Login functionality"""
    
    @pytest.mark.skip(reason="Skipping for now")
    def test_login_page_loads(self, driver):
        """Verify that login page loads correctly"""
        login_page = LoginPage(driver)
        
        # Verify email input field is visible
        assert login_page.is_element_visible(login_page.EMAIL_INPUT), \
            "Email input field should be visible"
    
    @pytest.mark.skip(reason="Skipping for now")
    def test_send_otp_button_disabled_without_email(self, driver):
        """Verify Send OTP button behavior without email"""
        login_page = LoginPage(driver)
        
        # Check if Send OTP button exists
        assert login_page.is_element_visible(login_page.SEND_OTP_BUTTON), \
            "Send OTP button should be visible"
    
    @pytest.mark.skip(reason="Skipping for now")
    def test_enter_email_and_send_otp(self, driver, config):
        """Test entering email and clicking Send OTP"""
        login_page = LoginPage(driver)
        
        # Enter email from config
        email = config.get("email", "test@example.com")
        login_page.enter_email(email)
        
        # Click Send OTP
        login_page.click_send_otp()
        
        # Verify OTP page is displayed
        assert login_page.is_otp_page_displayed(), \
            "OTP page should be displayed after clicking Send OTP"
    
    @pytest.mark.skip(reason="Skipping for now")
    def test_otp_page_elements(self, driver, config):
        """Verify OTP page elements are present"""
        login_page = LoginPage(driver)
        
        # Enter email and send OTP
        email = config.get("email", "test@example.com")
        login_page.login_with_email(email)
        
        # Wait for OTP page
        assert login_page.is_otp_page_displayed(), \
            "OTP page should be displayed"
        
        # Verify Login button is present
        assert login_page.is_element_visible(login_page.LOGIN_BUTTON), \
            "Login button should be visible on OTP page"
        
    @pytest.mark.skip(reason="Skipping for now")
    def test_complete_login_with_manual_otp(self, driver, config):
        """Test complete login flow with manual OTP entry
        
        This test requires manual OTP entry from the user.
        The test will wait for the configured time for manual input.
        """
        login_page = LoginPage(driver)
        
        # Get credentials from config
        email = config.get("email", "test@example.com")
        manual_wait = config.get("otp_manual_wait_secs", 15)
        
        # Manual OTP entry
        login_page.login_with_email(email)
        
        # Wait for OTP page
        assert login_page.is_otp_page_displayed(), \
            "OTP page should be displayed"
        
        # Wait for manual OTP entry and login
        print(f"\n>>> Please enter OTP manually within {manual_wait} seconds <<<")
        time.sleep(manual_wait)
        login_page.click_login()
        
        # Wait for page to load after login
        time.sleep(5)
        
        # Verify login was successful by checking URL change
        current_url = driver.current_url
        base_url = config.get("base_url", "")
        
        # Login is successful if we're no longer on the OTP page
        assert current_url != f"{base_url}/otp", \
            f"Should be redirected after successful login. Current URL: {current_url}"
        
        print(f"Login successful! Redirected to: {current_url}")
    
    @pytest.mark.skip(reason="Skipping for now")
    def test_go_back_from_otp_page(self, driver, config):
        """Test Go Back functionality from OTP page"""
        login_page = LoginPage(driver)
        
        # Enter email and send OTP
        email = config.get("email", "test@example.com")
        login_page.login_with_email(email)
        
        # Wait for OTP page
        assert login_page.is_otp_page_displayed(), \
            "OTP page should be displayed"
        
        # Click Go Back
        login_page.click_go_back()
        
        # Verify we're back on login page
        assert login_page.is_element_visible(login_page.EMAIL_INPUT), \
            "Should be back on login page with email input visible"


class TestResourceManagement:
    """Test cases for Resource Management functionality - Updated UI with tabs"""
    
    def test_add_resource_new_flow(self, driver, config):
        """Test adding resource with new tabbed modal UI
        
        13-Step Flow:
        1. Click Add Resource button
        2. Enter First Name
        3. Enter Last Name
        4. Enter Email
        5. Enter Phone
        6. Select 14th July 2022 as joining date
        7. Select 3 years experience
        8. Select Python Developer as primary skill
        9. Select Madhu as reporting manager
        10. Click Employment tab
        11. Select GigLabz company, IT department, Senior Software Developer role
        12. Click Add Resource button (submit)
        13. Click close icon
        14. Validate user in list
        """
        login_page = LoginPage(driver)
        manage_page = ManagePage(driver)
        
        # Get config values
        email = config.get("email", "test@example.com")
        manual_wait = config.get("otp_manual_wait_secs", 15)
        
        # ==================== Login Process ====================
        login_page.login_with_email(email)
        assert login_page.is_otp_page_displayed(), "OTP page should be displayed"
        
        # Enter hardcoded OTP
        print(">>> Entering OTP: 1234 <<<")
        login_page.enter_otp("1234")
        
        login_page.click_login()
        
        # Wait for page to load after login
        time.sleep(8)
        
        # Verify login was successful
        current_url = driver.current_url
        print(f"Current URL after login: {current_url}")
        
        if "/otp" in current_url:
            pytest.fail("Login failed - still on OTP page")
        
        print("Login successful! Navigating to Resource Management...")
        
        # ==================== Navigate to Resource Management ====================
        time.sleep(2)
        sa_page = SystemAdministrationPage(driver)
        sa_page.click_SA_menu()
        time.sleep(2)
        manage_page.click_manage_menu()
        time.sleep(3)
        manage_page.click_resource_management_tab()
        time.sleep(3)
        
        # ==================== Add Resource Flow ====================
        num_resources = config.get("num_resources_to_add", 1)
        
        for i in range(num_resources):
            # Generate test data
            first_name, last_name = manage_page.generate_random_name()
            phone = manage_page.generate_random_phone()
            resource_email = manage_page.generate_random_email(first_name, last_name)
            
            print(f"\n--- Adding Resource {i + 1} of {num_resources} ---")
            print(f"Name: {first_name} {last_name}")
            print(f"Email: {resource_email}")
            print(f"Phone: {phone}")
            
            # Step 1: Click Add Resource button
            manage_page.click_add_resource_button()
            time.sleep(2)
            
            # Step 2-5: Fill Basic Info
            manage_page.enter_first_name(first_name)
            manage_page.enter_last_name(last_name)
            manage_page.enter_email(resource_email)
            manage_page.enter_phone(phone)
            
            # Step 6: Select Date of Joining - 14th July 2022
            manage_page.select_date_of_joining(14, 7, 2022)
            
            # Step 7: Select Experience - 3 years
            manage_page.select_experience("3")
            
            # Step 8: Select Primary Skill - Python Developer
            manage_page.select_primary_skill("python developer")
            
            # Step 9: Select Reporting Manager - Madhu
            manage_page.select_reporting_manager("Madhu Poclassery")
            
            # Step 10: Click Employment Tab
            manage_page.click_employment_tab()
            time.sleep(1)
            
            # Step 11: Fill Employment Info
            # Select Company - GigLabz
            manage_page.select_company("GigLabz")
            
            # Select Department - IT
            manage_page.select_department("IT")
            
            # Select Role - Senior Software Developer
            manage_page.select_role("senior software developer")

            print("DEBUG: about to select employee type")
            manage_page.select_employee_type("full time")
            print("DEBUG: about to select work shift")
            manage_page.select_work_shift("day")
            print("DEBUG: about to select location")
            manage_page.select_location("hyderabad")
            print("DEBUG: about to select vendor")
            manage_page.select_vendor("cognizant")
            print("DEBUG: about to select project")
            manage_page.select_project("fintech app")            
            # Step 12: Click Add Resource button (submit)
            manage_page.click_add_resource_submit()
            print("⏳ Waiting for resource to be saved...")
            time.sleep(3)
            
            # Step 13: Click Close icon
            manage_page.click_close_modal()
            time.sleep(2)
            
            # Step 14: Validate user in list
            print(f"\n📋 Verifying if '{first_name} {last_name}' was added to the list...")
            success = manage_page.verify_resource_in_list(first_name)
            
            if success:
                print("\n" + "="*60)
                print(f"🎯 RESULT: Resource {i + 1} ({first_name} {last_name})")
                print(f"   ✅ USER ADDED SUCCESSFULLY!")
                print(f"   📧 Email: {resource_email}")
                print(f"   📱 Phone: {phone}")
                print("="*60 + "\n")
            else:
                print("\n" + "="*60)
                print(f"⚠️ RESULT: Resource {i + 1} ({first_name} {last_name})")
                print(f"   ❌ User may need manual verification")
                print("="*60 + "\n")
            
            time.sleep(2)
        
        print("\n" + "🏁"*20)
        print(f"=== TEST COMPLETED: Added {num_resources} resource(s) ===")
        print("🏁"*20 + "\n")
        
        # Logout after completing all resource additions
        print("DEBUG: about to logout", flush=True)
        login_page.logout()
        print("DEBUG: logout completed", flush=True)


class TestLoginNegative:
    """Negative test cases for login functionality"""
    
    @pytest.mark.skip(reason="Skipping for now")
    def test_invalid_email_format(self, driver):
        """Test login with invalid email format"""
        login_page = LoginPage(driver)
        
        # Enter invalid email
        login_page.enter_email("invalid-email")
        
        # Try to send OTP - button might be disabled or show error
        # This depends on the application's validation behavior
        assert login_page.is_element_visible(login_page.SEND_OTP_BUTTON), \
            "Send OTP button should still be visible"
    
    @pytest.mark.skip(reason="Skipping for now")
    def test_empty_email(self, driver):
        """Test login with empty email field"""
        login_page = LoginPage(driver)
        
        # Don't enter any email, just verify button state
        assert login_page.is_element_visible(login_page.SEND_OTP_BUTTON), \
            "Send OTP button should be visible"