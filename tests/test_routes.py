import pytest
from fastapi import status
from fastapi.testclient import TestClient
from pytest_lazyfixture import lazy_fixture
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.parametrize(
    "route, status_code",
    [
        ("", status.HTTP_200_OK),
        ("/", status.HTTP_200_OK),
        ("/bad-route", status.HTTP_404_NOT_FOUND),
    ],
)
def test_route(
    client: TestClient,
    route: str,
    status_code: int,
) -> None:
    response = client.get(route)

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "driver",
    [
        lazy_fixture("chrome"),
        lazy_fixture("firefox"),
        # lazy_fixture("edge"),
        # lazy_fixture("internet_explorer"),
        # lazy_fixture("safari"),
    ],
)
def test_linked_routes(
    client: TestClient,
    driver: WebDriver,
) -> None:
    previous_routes: set[str] = set()

    # Start with the root url.
    all_routes: set[str] = {""}

    while previous_routes != all_routes:
        # Can't add to all_routes while iterating through it, temporary place for new urls.
        new_routes: set[str] = set()

        # all_routes is guaranteed to have everything in previous_routes and any new ones.
        for route in all_routes.difference(previous_routes):
            response = client.get(route)

            assert response.status_code == status.HTTP_200_OK

            driver.get(f"data:text/html;charset=utf-8,{response.content!r}")

            for a_element in driver.find_elements_by_tag_name("a"):
                a_href = a_element.get_attribute("href")

                # Ignore email addresses and files.
                if "." not in a_href:
                    new_routes.add(a_href)

            previous_routes.add(route)

        all_routes.update(new_routes)
