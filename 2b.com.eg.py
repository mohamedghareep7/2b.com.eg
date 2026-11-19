from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()

all_products = []

for pages in range(1,4):
    print("page :" , pages)
    driver.get(f"https://2b.com.eg/en/computers/laptops.html?p={pages}")

    big_container = driver.find_element(By.XPATH , '//div[@class="products wrapper grid columns5 products-grid   "]')
    # print(big_container.get_attribute("outerHTML"))

    container = big_container.find_elements(By.XPATH , './/div[@class="product-item-info type3"]')

    for item in container:
        description = item.find_element(By.XPATH , './/a[@class="product-item-link"]').text
        print('description :' , description)

        price_container = item.find_element(By.XPATH , './/div[@class="price-box price-final_price"]')

        current_price = price_container.find_elements(By.XPATH , './/span[@class="price"]')
        current_price = current_price[1].text
        print('current_price :' , current_price)

        try:
            price_container = item.find_element(By.XPATH , './/div[@class="price-box price-final_price"]')
            discount = price_container.find_elements(By.XPATH , './/span[@class="price"]')
            discount = discount[0].text
            print('price befor descount :' , discount)
        except:
            discount = "no discount on item"
            print('price befor descount :' , discount)

        try:
            Discount_amount = item.find_element(By.XPATH , './/div[@class="discount-info message"]').text
            print('Discount amount :' , Discount_amount)
        except:
            Discount_amount = 'not found on website'
            print('Discount amount :' , Discount_amount)

        # try:
        #     stock = item.find_element(By.XPATH , './/div[contains(@class,"discount-info"))]').text
        #     # print(item.get_attribute("outerHTML"))
        #     print('stock :' , stock)
        # except:
        #     stock = 'Not available'
        #     # print(item.get_attribute("outerHTML"))
        #     print('stock :' , stock)

        try:
            product_link = item.find_element(By.XPATH , './/div[@class="product photo product-item-photo"]//a').get_attribute("href")
            print('product_link :' , product_link)
        except:
            product_link = "no link found"
            print('product_link :' , product_link)

        try:
            product_image = item.find_element(By.XPATH , './/img[@class="product-image-photo default_image "]').get_attribute("src")
            print('product_image :' , product_image)
        except:
            product_image = 'no image found'
            print('product_image :' , product_image)
        
        print("="*20 )

        dict_products = {
            "description" : description ,
            "current_price" : current_price ,
            "discount" : discount ,
            "Discount_amount" : Discount_amount ,
            "product_link" : product_link ,
            "product_image" : product_image
        }

        all_products.append(dict_products)

header = all_products[0].keys()
path = "all products.csv"
with open (path , "w" , encoding="utf-8" , newline="") as file :
    writer = csv.DictWriter(file , header)
    writer.writeheader()
    writer.writerows(all_products)


