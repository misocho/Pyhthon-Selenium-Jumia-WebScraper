import csv
from selenium import webdriver


max_page_num = 24
max_page_dig = 2

with open('dataFrame.csv', 'w') as f:
   f.write("product name, product price \n")
    
def format_row(*fields):
    row = ''
    for field in fields:
        if row:
            row = row + ', ' + ''.join(field.split(','))
        else:
            row = ''.join(field.split(','))
    return row

def format_row_price(*fields):
    row = ''
    for field in fields:
        if row:
            row = row + ', ' + ''.join(field.split('KSh '))
        else:
            row = ''.join(field.split('KSh '))
    return float(row)
#open firefox browser and navigate to webpage

driver = webdriver.Firefox()
product_name = []
product_price = []
for i in range (7, max_page_num + 1):
    page_loc = "?page="
    url = 'https://www.jumia.co.ke/mobile-phones/' + page_loc + str(i)
    
    driver.get(url)
    
    brand = driver.find_elements_by_class_name("brand")
    name = driver.find_elements_by_class_name("name")
    price = driver.find_elements_by_class_name('price')
    
    num_brand_name = len(brand)
    for i in range(num_brand_name):
        product_name.append(brand[i].text + " " + name[i].text)
    
    for x in range(0, len(brand) + 1, 2):
        product_price.append(price[x].text)
    
    with open('dataFrame.csv', 'a') as f:
        for i in range(len(product_price)):
           f.write(format_row(product_name[i]) + "," + 
                   str(format_row_price(format_row(product_price[i]))/ 100) + "\n")
    

driver.close()
    
print ('done')
