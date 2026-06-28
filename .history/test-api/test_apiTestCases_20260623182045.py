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
    payload={
        "title":"iPhone 9",
        "description":"An apple mobile which is nothing like apple",
        "price":549,
        "discountPercentage":12.96,
        "rating":4.69,
        "stock":94,
        "brand":"Apple",
        "category":"smartphones",
        "thumbnail":"https://i.dummyjson.com/data/products/1/thumbnail.jpg",
        "images":["https://i.dummyjson.com/data/products/1/1.jpg","https://i.dummyjson.com/data/products/1/2.jpg","https://i.dummyjson.com/data/products/1/3.jpg","https://i.dummyjson.com/data/products/1/4.jpg","https://i.dummyjson.com/data/products/1/thumbnail.jpg"]
    }
    response=context.post("http://dummyjson.com/products/add",data=payload)
    assert response.status==200
    

    