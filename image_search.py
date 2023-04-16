from selenium import webdriver
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By

def image_search(image_path):
    """This function will take an image path and return the top 5 search results from google vision

    Args:
        image_path (str): The string of an image path.

    Returns:
        list: List of dictionaries comprised of name, image link and url.
    """

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.page_load_strategy = 'none'
    # chrome_path = ChromeDriverManager().install() 
    # chrome_service = Service(chrome_path) 
    # driver = Chrome(options=options, service=chrome_service)
    driver = Chrome(options=options)

    driver.implicitly_wait(5)
    # driver = webdriver.Chrome(chrome_path)
    # driver.implicitly_wait(5)

    #path of webdriver executable
    # webdriver_path = "/image_search"

    #new Chrome webdriver instance
    # driver = webdriver.Chrome(webdriver_path)

    driver.get("https://www.google.com/imghp")
    driver.maximize_window()  
      
    # find the "Search by image" icon and click it
    search_by_image_icon = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]")
    search_by_image_icon.click()

    # wait for the search options to appear
    driver.implicitly_wait(3)

    # click on the "Paste image link" option
    paste_image_link_option = driver.find_element(By.XPATH, '//*[@id="ow6"]/div[3]/c-wiz/div[2]/div/div[3]/div[2]/c-wiz/div[2]/input')
    paste_image_link_option.click()

    # paste the image link
    paste_image_link_option.clear()
    paste_image_link_option.send_keys(image_path)

    # click the "Search" button to start the search
    search_button = driver.find_element(By.XPATH, "//div[text()='Search']")
    search_button.click()

    # wait for the search results to load
    driver.implicitly_wait(5)

    #save the first five search results by its url and image link
    top5_search_results = []
    for i in range(1, 6):
        href_result = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/div/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div[{}]/div/a'.format(i))
        url = href_result.get_attribute("href")
        image_result = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/div/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div[{}]/div/a/div'.format(i))
        image_link = image_result.get_attribute("data-thumbnail-url")
        product_name = image_result.get_attribute("data-item-title")
        top5_search_results.append({"product": product_name, "image": image_link, "url": url})

    # print(top5_search_results)
    return top5_search_results

# image_path = 'https://cdn0.woolworths.media/content/wowproductimages/medium/038121.jpg'
# image_search(image_path)