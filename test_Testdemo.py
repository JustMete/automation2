from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
import pytest

 
class Test_class(): 

    USERNAME_INPUT_SELECTOR = "user-name"
    PASSWORD_INPUT_SELECTOR = "password"
    LOGIN_BUTTON_SELECTOR = "login-button"


    @pytest.fixture()
    def setup(self):
        print("testi başlıyor..")
        self.driver = webdriver.Chrome() 
        self.wait = WebDriverWait(self.driver, 10)  #
        self.driver.get("https://www.saucedemo.com/") 
        self.driver.maximize_window()
        yield
        self.driver.close()

##-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def test_case1(self,setup):  
        loginButton = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR) 
        loginButton.click()
        error_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"error-message-container")))
        expected_message = "Epic sadface: Username is required" 
        assert error_message.text == expected_message
        print("1. test başarılı!")

##-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    def test_case2(self,setup):  
        fill_username = self.driver.find_element(By.ID,self.USERNAME_INPUT_SELECTOR) 
        fill_username.send_keys("standard_user") 
        loginButton = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR) 
        loginButton.click() 
        error_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"error-message-container")))
        expected_message = "Epic sadface: Password is required" 
        assert error_message.text == expected_message
        print("2. test başarılı!")

##-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_case3(self,setup):
        fill_username = self.driver.find_element(By.ID,self.USERNAME_INPUT_SELECTOR)
        fill_username.send_keys("locked_out_user")
        fill_password = self.driver.find_element(By.ID,self.PASSWORD_INPUT_SELECTOR)
        fill_password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR)
        loginButton.click() 
        error_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"error-message-container")))
        expected_message = "Epic sadface: Sorry, this user has been locked out." 
        assert error_message.text == expected_message
        print("3. test başarılı!")

##-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_case4(self,setup):
        fill_username = self.driver.find_element(By.ID,self.USERNAME_INPUT_SELECTOR)
        fill_username.send_keys("standard_user")
        fill_password = self.driver.find_element(By.ID,self.PASSWORD_INPUT_SELECTOR)
        fill_password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR)
        loginButton.click()
        self.wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
        check_item = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert 6 == len(check_item)
        print("4. test başarılı!")

## kullanıcı başarılı bir şekilde giriş yapıp daha sonra başarılı bir şekilde çıkış yapabilmelidir.
    def test_case5(self,setup):
        fill_username = self.driver.find_element(By.ID,self.USERNAME_INPUT_SELECTOR)
        fill_username.send_keys("standard_user")
        fill_password = self.driver.find_element(By.ID,self.PASSWORD_INPUT_SELECTOR)
        fill_password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR)
        login_button.click()
        hamburger_menu = self.wait.until(EC.visibility_of_element_located((By.ID,"react-burger-menu-btn")))
        hamburger_menu.click()
        logout_button = self.wait.until(EC.visibility_of_element_located((By.ID,"logout_sidebar_link")))
        logout_button.click()
        login_button_value = self.wait.until(EC.visibility_of_element_located((By.ID,"login-button"))).get_attribute("value")
        expected_value = "Login"
        assert login_button_value == expected_value
        print("5. test başarılı!")
      
##-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra footer içerisinde sosyal medya ikonlarının varlığı kontrol edilmeli.
    def test_case6(self,setup):
        fill_username = self.driver.find_element(By.ID,self.USERNAME_INPUT_SELECTOR)
        fill_username.send_keys("standard_user")
        fill_password = self.driver.find_element(By.ID,self.PASSWORD_INPUT_SELECTOR)
        fill_password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR)
        loginButton.click()
        social_twitter = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"social_twitter")))
        social_facebook = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"social_facebook"))) 
        social_linkedin = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"social_linkedin")))       
        print("6. test başarılı!")

##-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra listedeki ilk ürün sepete eklenebilmelidir.
    def test_case7(self,setup):
        fill_username = self.driver.find_element(By.ID,self.USERNAME_INPUT_SELECTOR)
        fill_username.send_keys("standard_user")
        fill_password = self.driver.find_element(By.ID,self.PASSWORD_INPUT_SELECTOR)
        fill_password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR)
        loginButton.click()
        first_add_card_button = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='inventory_item'][1]//button"))) 
        first_add_card_button.click()   
        shopping_card_badge = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        assert shopping_card_badge.text == "1"
        first_add_card_button = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='inventory_item'][1]//button"))) 
        assert first_add_card_button.text == "Remove"
        print("7. test başarılı!")

##-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra ilk 3 ürün ayrı ayrı sepete eklenip çıkarılabilmelidir.
    @pytest.mark.parametrize("card_number", [
        "1","2","3"
    ])
    def test_case8(self,setup,card_number):
        fill_username = self.driver.find_element(By.ID,self.USERNAME_INPUT_SELECTOR)
        fill_username.send_keys("standard_user")
        fill_password = self.driver.find_element(By.ID,self.PASSWORD_INPUT_SELECTOR)
        fill_password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR)
        loginButton.click()
        first_add_card_button = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='inventory_item']["+card_number+"]//button"))) 
        first_add_card_button.click()   
        shopping_card_badge = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        assert shopping_card_badge.text == "1"
        first_add_card_button = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='inventory_item']["+card_number+"]//button"))) 
        assert first_add_card_button.text == "Remove"
        shopping_card_badge.click()
        sleep(1)
        remove_item_from_basket = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='cart_item']//button"))) 
        remove_item_from_basket.click()   
        shopping_card_badge = self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        print("8. test başarılı!")
 


## EXCEL DATA TEST

    def read_data_from_excel(file_path):
        df = pd.read_excel(file_path)
        return df.values.tolist()

    # Excel dosyası yolu
    excel_file_path = "data/test_data.xlsx"

    # Verileri oku
    test_data = read_data_from_excel(excel_file_path)

##-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra excelden okunan ürün sıra numarası ve ürün isimleri karşılaştırılmalı
    @pytest.mark.parametrize("product_list_number, product_name", test_data)
    def test_case9(self,setup,product_list_number, product_name):
        fill_username = self.driver.find_element(By.ID,self.USERNAME_INPUT_SELECTOR)
        fill_username.send_keys("standard_user")
        fill_password = self.driver.find_element(By.ID,self.PASSWORD_INPUT_SELECTOR)
        fill_password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR)
        loginButton.click()
        inventory_item_xpath = "//div[@class='inventory_item']["+str(product_list_number)+"]//div[contains(@class,'inventory_item_name')]"
        inventory_item_name = self.driver.find_element(By.XPATH,inventory_item_xpath)
        
        assert inventory_item_name.text == product_name
        print("9. test başarılı!") 


 ## JSON DATA TEST       
    with open("data/test_data.json", "r") as file:
        data = json.load(file)

##-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra excelden okunan ürün sıra numarası ve ürün isimleri karşılaştırılmalı
    def test_case10(self,setup):
        fill_username = self.driver.find_element(By.ID,self.USERNAME_INPUT_SELECTOR)
        fill_username.send_keys("standard_user")
        fill_password = self.driver.find_element(By.ID,self.PASSWORD_INPUT_SELECTOR)
        fill_password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,self.LOGIN_BUTTON_SELECTOR)
        loginButton.click()  
        
        i = 1
        for product in self.data["products"]:
            inventory_item_xpath = "//div[@class='inventory_item']["+str(i)+"]//div[contains(@class,'inventory_item_name')]"
            inventory_item_name = self.driver.find_element(By.XPATH,inventory_item_xpath)
            assert product == inventory_item_name.text
            i+=1
        print("10. test başarılı!")