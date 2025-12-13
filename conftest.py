import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


def load_config():
    """Load configuration from YAML file"""
    with open("utils/config.yaml", "r") as file:
        return yaml.safe_load(file)


@pytest.fixture(scope="function")
def driver():
    """Setup and teardown for WebDriver"""
    config = load_config()
    
    # Chrome options
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    # Uncomment below for headless mode
    # chrome_options.add_argument("--headless")
    
    # Initialize driver
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    # Set implicit wait from config
    driver.implicitly_wait(config.get("implicit_wait", 5))
    
    # Navigate to base URL
    driver.get(config["base_url"])
    
    yield driver
    
    # Teardown
    driver.quit()


@pytest.fixture(scope="function")
def config():
    """Load and return configuration"""
    return load_config()
