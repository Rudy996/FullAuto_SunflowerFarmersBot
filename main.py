from selenium import webdriver
import time



options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_extension("MetaMask.crx")




def pizda():

    print("Start")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.get("https://sunflower-farmers.com/play/")
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id='welcome']/div/span").click()
    print("Поиск ошибки при входе")
    time.sleep(30)
    try:
        error = driver.find_element_by_id("error-title").is_enabled()
        print(error)
        time.sleep(5)
        while error == True:
            print("Йобанный полигон за 2 рубля")
            time.sleep(2)
            driver.refresh()
            time.sleep(5)
            driver.find_element_by_xpath("//div[@id='welcome']/div/span").click()
            time.sleep(30)
            error = driver.find_element_by_id("error-title").is_enabled()
    except:
        print("Вошли в аккаунт")
        print("Начало работы через 30 секунд")
        time.sleep(30)
        while True:
            i = 0
            b = 0
            while b != cikl:
                i = i + 1
                print(f"Цикл {i}")
                driver.find_element_by_xpath("//div[@id='container']/div[601]/div[6]/div/img[2]").click()
                driver.find_element_by_xpath("//div[@id='container']/div[601]/div[6]/div/div[2]").click()
                time.sleep(0.1)
                driver.find_element_by_xpath("//div[@id='container']/div[601]/div[8]/div/img[2]").click()
                driver.find_element_by_xpath("//div[@id='container']/div[601]/div[8]/div/div[2]").click()
                time.sleep(0.1)
                driver.find_element_by_xpath("//div[@id='first-sunflower']/div/img[2]").click()
                driver.find_element_by_xpath("//div[@id='first-sunflower']/div/div[2]/div").click()
                # driver.find_element_by_xpath("//div[@id='first-sunflower']/div/div[2]/div[2]')]").click()
                time.sleep(0.1)
                driver.find_element_by_xpath("//div[@id='container']/div[601]/div[10]/div/img[2]").click()
                driver.find_element_by_xpath("//div[@id='container']/div[601]/div[10]/div").click()
                time.sleep(0.1)
                driver.find_element_by_xpath("//div[@id='container']/div[601]/div[7]/div/img[2]").click()
                driver.find_element_by_xpath("//div[@id='container']/div[601]/div[7]/div/div[2]").click()
                time.sleep(cd)
                b = b + 1

            driver.find_element_by_xpath("//span[@id='save-button']/div/div").click()
            print("Начинаю сейв")
            time.sleep(5)
            try:
                print("Поиск ошибки")
                time.sleep(10)
                nahui = driver.find_element_by_id("error-title").is_enabled()
                print(nahui)
                time.sleep(5)
                while nahui == True:
                    print("Ошибка найдена")
                    time.sleep(2)
                    driver.refresh()
                    time.sleep(5)
                    driver.switch_to.alert.accept()
                    time.sleep(10)
                    Farm()
            except:
                print("Ошибка не найдена")
                time.sleep(10)
                price = driver.find_element_by_xpath("//div[@id='saving']/h2")
                pryx = price.text
                pric = float(pryx)
                time.sleep(5)
                while pric < comsa:
                    driver.find_element_by_xpath("//div[@id='save-error-buttons']/div").click()
                    time.sleep(5)
                    driver.execute_script("window.open('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#');")
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[2])
                    time.sleep(5)
                    time.sleep(0.5)
                    driver.refresh()
                    time.sleep(0.5)
                    driver.refresh()
                    time.sleep(0.5)
                    time.sleep(3)
                    driver.find_element_by_class_name("btn-primary").click()
                    time.sleep(5)
                    driver.close()
                    time.sleep(5)

def Farm():
    try:
        pizda()
    except:
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        driver.get("https://sunflower-farmers.com/play/")
        print("Alera подтвердить бы")
        time.sleep(5)
        driver.switch_to.alert.accept()
        time.sleep(5)
        print("Стартуем по новой через 10 секунд")
        time.sleep(10)
        Farm()


try:
    driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe",
                              options=options)
    private = input("You Private Key: ")
    passw = input("Password MetaMask: ")
    cd = int(input("Кд: "))
    cikl = int(input("Кол-во Циклов: "))
    comsa = float(input("Максимальная комиссия в  GWEI: "))
    # private = ("")
    # passw = ("")
    # cd = 60
    # cikl = 1
    # comsa = 1000

    driver.get("https://sunflower-farmers.com/play/")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
    print("Начинаем настройку MetaMask")
    time.sleep(5)
    item = driver.find_element_by_xpath("//button[@role='button']")
    print(item)
    print(item.text)
    item.click()
    time.sleep(3)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/select-action")
    time.sleep(2)
    # item2 = driver.find_element_by_xpath("//button[@class='first-time-flow__button']")
    driver.find_element_by_class_name("first-time-flow__button").click()
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/metametrics-opt-in")
    time.sleep(2)
    driver.find_element_by_xpath("//button[@data-testid='page-container-footer-next']").click()
    time.sleep(2)
    driver.get(
        "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")
    time.sleep(2)
    print("Начинаем импортировать ключи и добавлять пароль")
    clu4iki = driver.find_element_by_xpath("//input[@type='password']")
    # clu4iki = driver.find_element_by_xpath("MuiInput-input")
    clu4iki.send_keys(private)
    time.sleep(1)
    password1 = driver.find_element_by_id("password")
    password1.send_keys(passw)
    password2 = driver.find_element_by_id("confirm-password")
    password2.send_keys(passw)
    print("Были импортированны ключи и добавлен пароль")
    time.sleep(2)
    driver.find_element_by_class_name("first-time-flow__terms").click()
    time.sleep(2)
    driver.find_element_by_class_name("first-time-flow__button").click()
    time.sleep(5)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/end-of-flow")
    time.sleep(5)
    driver.find_element_by_class_name("popover-header__button").click()
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network")
    time.sleep(2)
    elems = driver.find_elements_by_class_name("form-field__input")
    print("Начинаем добавлять сеть Polygon")
    time.sleep(2)
    elems[0].send_keys("Matic Mainnet")
    elems[1].send_keys("https://polygon-rpc.com/")
    elems[2].send_keys("137")
    elems[3].send_keys("MATIC")
    elems[4].send_keys("https://explorer.matic.network/")
    print("Сеть Polygon добавлена")
    time.sleep(5)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(30)
    driver.get("https://sunflower-farmers.com/play/")
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id='welcome']/div/span").click()
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
    time.sleep(2)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(3)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(5)

    Farm()




except Exception as ex:
    print(ex)
    print("Мужики, я уже реально хуй знает, чё оно крашнулось. Пробуйте фиксить сами")
finally:
    driver.close()
    driver.quit()
