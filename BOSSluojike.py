import csv
import os
import time,random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import base64
import json
import requests

#定位封装
class Driver:
    def __init__(self, driver):
        self.driver = driver
    def find_xpath(self, xpath, timeout=5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(("xpath", xpath)))
    def finds_xpath(self, xpath, timeout=5):
        time.sleep(1)
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(("xpath", xpath)))
    def find_Exception(self,xpath,timeout=5):
        try:
            self.find_xpath(xpath,timeout=timeout)
            return True
        except:
            return False
    def text_exits(self,is_text):
        try:
            self.find_xpath("//*[contains(text(),'{}')]".format(is_text))
            return True
        except:
            return False



count_yzm = 0
def boss_gogo(username,password,search=False,handless=False):


    if search:
        driver_filter=webdriver.FirefoxProfile(r"C:\Users\ThreadPool\AppData\Roaming\Mozilla\Firefox\Profiles\a8gqpxr9.default-release")
        driver=webdriver.Firefox(firefox_profile=driver_filter)
        driver.get("https://login.zhipin.com/?ka=header-login")
    else:
        if handless:
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")  # 设置火狐为headless无界面模式
            options.add_argument("--disable-gpu")
            driver = webdriver.Firefox(options=options)
        else:
            driver =webdriver.Firefox()
        # 登录
        driver.get("https://login.zhipin.com/?ka=header-login")
        while "登录" in driver.title:
            driver.get("https://login.zhipin.com/?ka=header-login")
            login_regc(driver,username,password)

            if pass_discover(driver):
                print("账号不可用或者验证码执行过多次,跳过")
                return

            time.sleep(2)
        # assert_geetest_isclick(driver)
        # 循环遍历获得数据
        while not Driver(driver).find_Exception('//span[@class="job-name"]'):...
    # 实现主逻辑
    while True:
        # 薪资控制器
        # money_control(driver)
        # 循环遍历获得数据

        start_time = time.time()
        while 1:
            try:
                if time.time()<start_time+60:driver.refresh()
                g1 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_all_elements_located((By.XPATH, '//span[@class="job-name"]')))
                break
            except:
                g1 = None
        if len(g1) > 0:
            for i in g1:
                if "测试" not in i.text:continue
                i.click()
                driver.switch_to.window(driver.window_handles[-1])
                #打印岗位
                print_gangwei(driver)
                # 尝试点击立即沟通
                click_continue(driver)
                time.sleep(1)
                try:
                    driver.find_element_by_xpath('//*[@class="icon-dialog-arrow"]')
                    try:
                        driver.find_element_by_xpath('//div[@class="dialog-container"]//h3[@class="title"]')
                        driver.find_element_by_xpath('//*[@class="remindType"]//*[@type="checkbox"]').click()
                        driver.find_element_by_xpath('//span[@class="btn btn-sure"]').click()
                    except:

                        #尝试两遍
                        for i in range(3):
                            send_msg(driver)
                            driver.refresh()
                        driver.quit()
                        return
                except:
                    pass
                # 切换回原窗口
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        # 点击翻页按钮
        # 点击翻页按钮
        driver.refresh()
        time.sleep(20)
        try:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//i[@class="ui-icon-arrow-right"]/..'))).click()
            time.sleep(4)
        except:
            pass

#岗位过滤器,暂时不用
def filter_duit(driver):
    filter_list = ["无需经验", "硬件","电子"]
    join_list = []
    for i in filter_list:
        join_list.append('contains(text(),"%s")' % (i))
    xpath_find = '//*[%s]' % (" or ".join(join_list))
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, xpath_find)))
        return True
    except:
        return False

#点击沟通
def click_continue(driver):
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@class="dialog-con"]')))
        print("沟通人数以及达到上限")
        driver.quit()
        return True
    except:
        pass
    try:
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@class="btn btn-startchat"]'))).click()
        try:
            ActionChains(driver).move_by_offset(xoffset=346,yoffset=199).click().perform()
        except:pass
    except:
        pass

#打印岗位名称
def print_gangwei(driver):
    try:
        n11 = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="name"]/h1'))).text
        print("职位{}".format(n11))
    except:
        pass

# 登录三要素
def login_regc(driver,a,b):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="手机号"]'))).send_keys(a)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="密码"]'))).send_keys(b)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pwdVerrifyCode"]'))).click()
    #验证码执行


# # 循环识别验证码是否已经点击
# def assert_geetest_isclick(driver):
#     driver=Driver(driver)
#     while True:
#         try:
#             print("x")
#             driver.find_xpath( '//*[@class="sign-form sign-pwd"]//button').click()
#             break
#         except:
#             pass

#验证码破解
def pass_discover(driver):
    global count_yzm
    img = r'D:\langu_coding\python_code\bossGOGO\BOSSgetoffer\pic_path\{}.png'.format(int(time.time()*10))
    driver_o = Driver(driver)
    time.sleep(2)
    driver_o.find_xpath('//*[@class="geetest_fullpage_click_box"]').screenshot(img)
    time.sleep(2)
    result_p = base64_api(img=img)
    print("验证码坐标: {}".format(result_p))
    if count_yzm==3:
        count_yzm=0
        return True
    get_resutl = [[i.split(",")[0], i.split(",")[1]] for i in result_p.split("|")]
    count_yzm+=1
    for i in get_resutl:
        # get_pic_location = [((220 - (int(i[0]) - 10)) * -0.25) // 0.3, ((220 - (int(i[1]) - 75)) * -0.25) // 0.3]
        get_pic_location = [((210 - (int(i[0]) - 10)) * -0.25) // 0.3, ((220 - (int(i[1]) - 80)) * -0.25) // 0.3]
        ActionChains(driver) \
            .move_to_element(driver_o.find_xpath('//*[@class="geetest_item_img"]')) \
            .move_by_offset(get_pic_location[0], get_pic_location[1]).click().perform()
    driver_o.find_xpath('//*[@class="geetest_commit"]').click()
    time.sleep(1)
    try:
        driver_o.find_xpath('//div[@class="dialog-container"]/div[@class="dialog-con"]',timeout=2)
        return True
    except:pass
    try:
        driver_o.find_xpath( '//*[@class="sign-form sign-pwd"]//button').click()
    except:pass
class get_of:
    def read_file(self):
        get_str = csv.reader(os.path.abspath("/账号密码.csv"))
        next(get_str)
        return get_str
    def lagou(self,name):
        for i in self.read_file():
            if name in i[0]:
                return i[4],i[5]
    def boss(self,name):
        for i in self.read_file():
            if name in i[0]:
                return i[6],i[7]


# 薪资限制器
def money_control(driver):
    try:
        ActionChains(driver).move_to_element(WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(("xpath", '//*[@class="filter-select-box"]/div[3]')))).perform()
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//li[text()="10-20K"]'))).click()
    except:pass

#自动化简易回复 , 这部分需要接入图灵API
def send_msg(driver):
    find=Driver(driver)
    driver.get("https://www.zhipin.com/web/geek/chat")
    time.sleep(30)
    driver.implicitly_wait(5)
    red_point_gt = [i for i in find.finds_xpath("//*[@class='notice-badge' and text()>'0']", timeout=20)]
    if len(red_point_gt)<3:return
    for i in range(1,len(red_point_gt)):
        red_point_gt = [i for i in find.finds_xpath("//*[@class='notice-badge' and text()>'0']", timeout=20)]
        try:
            get_locations=red_point_gt[i].location.get("y")-168 if red_point_gt[i].location.get("y")-168>0 else 0
            driver.execute_script("document.getElementsByClassName('user-list')[0].scrollBy(0,{tex})".format(tex=get_locations))
            red_point_gt[i].click()
            if "测试" not in find.find_xpath('//*[@class="bar-position-name"]').text:
                continue
            get_chat_smg = find.find_xpath('//div[@class="chat-message"]').get_attribute("outerHTML")
            if not 'class="item-myself"' in get_chat_smg:
                send_msg_box_index = random.choice(
                    ["您好!!", "简历送到请查收!", "请问我可以去贵公司面试吗?", "您好,简历已发送请查看一下我的简历!", "我可以把我的简历发给您看看吗？"])
                find.find_xpath('//div[@class="chat-input"]').send_keys(send_msg_box_index)
                find.find_xpath('//button[@class="btn btn-primary btn-send"]').click()
            if "我想要一份您的附件简历到我的邮箱，您是否同意" in get_chat_smg and 'class="link-agree">同意</a>' in get_chat_smg:
                find.find_xpath('//*[@class="btn btn-agree"]').click()
            elif "附件简历已发送" not in get_chat_smg and 'class="link-agree disabled">同意</a>' not in get_chat_smg:
                find.find_xpath('//a[@class="btn-resume tooltip tooltip-top"]').click()
                find.find_xpath('//span[@class="btn btn-primary btn-sure"]').click()
            if "我想要和您交换微信，您是否同意" in get_chat_smg and 'class="link-agree">同意</a>' in get_chat_smg:
                find.find_xpath('//*[@class="btn btn-agree"]').click()
            if "我想要和您交换联系方式，您是否同意" in get_chat_smg and 'class="link-agree">同意</a>' in get_chat_smg:
                find.find_xpath('//*[@class="btn btn-agree"]').click()
        except:pass
        # if not find.find_Exception("//li[@class='item-myself']",timeout=1) and not find.find_Exception("//span[text()='附件简历已发送']",timeout=1) :
        #     msg_box = ["您好!!","简历送到请查收!","请问我可以去贵公司面试吗?","您好,简历已发送请查看一下我的简历!"]
        #     find.find_xpath('//div[@class="chat-input"]').send_keys(random.choice(msg_box))
        #     find.find_xpath('//button[@class="btn btn-primary btn-send"]').click()
        #     #//*[@class="btn btn-agree"]
        #     #点击发送简历
        #     try:
        #         find.find_xpath('//*[@class="btn btn-agree"]',timeout=1).click()
        #     except:pass
        #     find.find_xpath('//a[@class="btn-resume tooltip tooltip-top"]').click()
        #     find.find_xpath('//span[@class="btn btn-primary btn-sure"]').click()
        #
        # elif not find.find_Exception("//span[text()='附件简历已发送']",timeout=1):
        #     find.find_xpath('//a[@class="btn-resume tooltip tooltip-top"]').click()
        #     find.find_xpath('//span[@class="btn btn-primary btn-sure"]').click()


#图片验证码识别封装
def base64_api(uname='xxxx', pwd='xxx', img="img_path", typeid=27):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]

if __name__ == '__main__':
    ...