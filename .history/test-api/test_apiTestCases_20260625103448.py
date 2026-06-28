import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.api
def test_getApi(playwright):
    context = playwright.request.new_context()
    response = context.get("http://dummyjson.com/products")
    # print(response.json())
    # print(response.status)
    # print(response.status_text)
    assert response.status == 200
    print(response["products"])





    