from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 20)
def login(user,password):
    url = 'https://www.tmall.hk/wow/member-club/act/login?redirectURL=https%3A%2F%2Fwww.tmall.hk%2F%3Fali_trackid%3D2%3Amm_26632258_3504122_57428267%3A1501946231_265_1618700379%26upsid%3D456935998a557ebb76e8ff147f1c8820%26clk1%3D456935998a557ebb76e8ff147f1c8820'
    browser.get(url)
    element1=browser.find_element_by_xpath("//div[@class='form-content']/iframe[@id='J_loginIframe']")
    browser.switch_to_frame(element1)
    browser.maximize_window()
    try:
        element = browser.find_element_by_xpath("//div[@id='J_LoginBox']/div[@class='hd']/div[@class='login-switch']/i[@class='iconfont static']")
        element.click()
    finally:
        suser = browser.find_element_by_xpath("//span[@class='ph-label']")
        suser.click()
        time.sleep(1)
        suser.send_keys(user)
        sword = browser.find_element_by_xpath("//span[@id='J_StandardPwd']")
        sword.click()
        time.sleep(1)
        sword.send_keys(password)
        sword.send_keys(Keys.RETURN)


def product_name(keword):
    browser.switch_to_default_content()
    element = browser.find_element_by_xpath("//div[@class='s-combobox-input-wrap']/input[@class='s-combobox-input']")
    element.clear()
    element.send_keys(keword)
    element.send_keys(Keys.RETURN)

def product_brand(browser):
    element = browser.find_element_by_xpath("//div[@class='j_Brand attr']/div/ul")
    brd=element.text
    s=brd.split("\n")
    return s
def product_class(browser):
    element = browser.find_element_by_xpath("//div[@class='j_Cate attr']/div/div/a")
    element.click()
    element = browser.find_element_by_xpath("//div[@class='j_Cate attr']/div/ul")
    brd=element.text
    s=brd.split("\n")
    return s
def product_names(browser):
    element = browser.find_element_by_xpath("//div[@class='propAttrs j_nav_prop']/div[@class='j_Prop attr']/div/ul")
    brd = element.text
    s = brd.split("\n")
    return s

def whichprodut(i):
    s=browser.window_handles
    browser.switch_to_window(s[0])
    element = browser.find_elements_by_xpath("//div[@id='J_ItemList']/div")
    element[i].click()
    time.sleep(1)
    if i==0:return len(element)

def generalinf():
    s = browser.window_handles
    browser.switch_to_window(s[1])
    try:
        element1 = browser.find_element_by_xpath("//div[@class='tb-wrap']")
    except:
        element1 = browser.find_element_by_xpath("//div[@class='tb-wrap meilihui-wrap']")
    element2= browser.find_element_by_xpath("//span[@id='J_CollectCount']")
    brd = element1.text+element2.text
    return brd

def storeinf():
    js = ["var q=document.documentElement.scrollTop=810","var q=document.documentElement.scrollTop=870","var q=document.documentElement.scrollTop=910"]
    browser.execute_script(js[0])
    browser.execute_script(js[1])
    browser.execute_script(js[2])
    time.sleep(1)
    element0 = browser.find_element_by_xpath("//div[@class='shop-intro']/div[@class='main-info']/a")
    element0.click()
    time.sleep(4)
    s = browser.window_handles
    browser.switch_to_window(s[2])
    element1 = browser.find_element_by_xpath("//ul[@class='dsr-info']")
    element2 = browser.find_element_by_xpath("//div[@class='left-box']")
    element3 = browser.find_element_by_xpath("//div[@class='charge']")
    sddf=element1.text+"\\n"+element2.text+"\\n"+element3.text
    browser.close()
    return sddf

def page(x):
    js = "var q=document.documentElement.scrollTop=9030"
    browser.execute_script(js)
    element0 = browser.find_element_by_xpath("//input[@class='ui-page-skipTo']")
    element0.clear()
    element0.send_keys(x)
    element0.send_keys(Keys.RETURN)
    time.sleep(3)


def comment():
    s = browser.window_handles
    browser.switch_to_window(s[1])
    js = "var q=document.documentElement.scrollTop=5000"
    browser.execute_script(js)
    wait.until(EC.visibility_of_any_elements_located((By.XPATH, "//div[@id='mainwrap']/div/ul/li")))[1].click()
    time.sleep(7)
    T = True
    a = []
    cot = 0
    while T:
        js = "var q=document.documentElement.scrollTop=5000"
        browser.execute_script(js)
        alarn = browser.find_elements_by_xpath("//body/div[14]")
        if len(alarn) == 1:
            try:
                element3 = browser.find_element_by_xpath("//body/div[14]/a")
                element3.click()
                print("警告")
            except:
                alarn=""
            else:
                element = browser.find_elements_by_xpath("//div[@class='rate-page']/div[@class='rate-paginator']/a")
                js1 = "var q=document.body.clientHeight;return(q)"
                i = browser.execute_script(js1) - 3600
                js = "var q=document.documentElement.scrollTop=" + str(i)
                browser.execute_script(js)
                element[len(element) - 1].click()
                time.sleep(1)
        element2 = browser.find_elements_by_xpath("//div[@class='rate-grid']/table/tbody/tr")
        for i in range(len(element2)):
            a.append(element2[i].text)
        if len(element2)>4:
            browser.execute_script("arguments[0].scrollIntoView();", element2[len(element2) - 3])
        else:
            browser.execute_script("arguments[0].scrollIntoView();", element2[len(element2) - 1])
        element2[len(element2) - 1].click()
        element = browser.find_elements_by_xpath("//div[@class='rate-page']/div[@class='rate-paginator']/a")
        if len(element)==0:
            T = False
            continue
        if element[len(element) - 1].text == '下一页>>':
            cot = cot + 1
            print("第" + str(cot) + "页")
            element[len(element) - 1].click()
        else:
            T = False
        time.sleep(2)
        browser.switch_to_alert()
    browser.close()
    return a
