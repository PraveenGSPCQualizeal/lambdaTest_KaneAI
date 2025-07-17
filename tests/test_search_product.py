from pages.search_page import SearchPage

def test_search_macbook(driver):
    page = SearchPage(driver)
    page.open("https://ecommerce-playground.lambdatest.io")
    page.search_product("Macbook")
    assert page.get_product_count() > 0, "No products found!"
