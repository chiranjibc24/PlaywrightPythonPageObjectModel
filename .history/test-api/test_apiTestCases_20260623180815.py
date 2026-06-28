import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.api
def test_getApi(playwright):
    context=playwright.request.new_context()
    response=context.get("http://dummyjson.com/product",params={"limit":5})
    # print(response.json())
    # print(response.status)
    # print(response.status_text)   
    assert response.status==200
    jsonData=response.json()
    print(jsonData["products"][0]["title"])


@pytest.mark.api
def test_postApi(playwright):
    context=playwright.request.new_context()
    
    