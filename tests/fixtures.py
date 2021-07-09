import pytest
from fastapi.testclient import TestClient
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from main import app


@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture()
def chrome() -> WebDriver:
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.headless = True
    return webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=options,
    )


@pytest.fixture()
def firefox() -> WebDriver:
    from selenium.webdriver.firefox.options import Options
    from webdriver_manager.firefox import GeckoDriverManager

    options = Options()
    options.headless = True
    return webdriver.Firefox(
        executable_path=GeckoDriverManager().install(),
        options=options,
    )


# Not working locally, permissions don't like the cached/downloaded Edge.
@pytest.fixture()
def edge() -> WebDriver:
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    return webdriver.Edge(
        executable_path=EdgeChromiumDriverManager().install(),
    )


# Not working locally, permissions don't like the cached/downloaded IE.
@pytest.fixture()
def internet_explorer() -> WebDriver:
    from selenium.webdriver.ie.options import Options
    from webdriver_manager.microsoft import IEDriverManager

    options = Options()
    options.headless = True
    return webdriver.Ie(
        executable_path=IEDriverManager().install(),
        options=options,
    )


# Requires enabling WebDriver automation through the "Allow Remote Automation" setting in Safari's Develop menu.
@pytest.fixture()
def safari() -> WebDriver:
    return webdriver.Safari()
