import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.api
def test_getApi(playwright):
    context = playwright.request.new_context()
    response = context.get("http://dummyjson.com/products",params={"limit": 5})
    # print(response.json())
    # print(response.status) 
    # print(response.status_text)
    # assert response.status == 200
    jsonData=response.json()
    print(jsonData["products"][0]["title"])

@pytest.mark.api
def test_postApi(playwright):
    context = playwright.request.new_context()
    body={
            "title": "Test Product 123",
            "price": 1000
         }

    response = context.post("https://dummyjson.com/products/add", data=body)
    assert response.status==201
    jsonResponse = response.json()
    print(jsonResponse["id"])


#put, patch and delete

def test_putApi(playwright):
    context=playwright.request.new_context()
    