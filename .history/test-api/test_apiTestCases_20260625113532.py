import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.api
def test_getApi(playwright):
    context = playwright.request.new_context()
    response = context.get("http://dummyjson.com/products",params={"limit": 5}, headers={"Authorization": f"%{response.status}"})
    # print(response.json())
    # print(response.status) 
    # print(response.status_text)
    # assert response.status == 200
    jsonData=response.json()
    print(jsonData["products"][0]["title"])

def test_postApi(playwright):
    context = playwright.request.new_context()
    response = context.post("http://dummyjson.com/products/add",data={"title": "iPhone 9","description": "An apple mobile which is nothing like apple","price": 549,"discountPercentage": 12.96,"rating": 4.69,"stock": 94,"brand": "Apple","category": "smartphones"})
    print(response.json())
    print(response.status) 
    print(response.status_text)
    assert response.status == 200



    