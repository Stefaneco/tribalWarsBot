from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import re
import sys
import time

import disco
import config
import bot


def check_ip():
    driver.get("https://whatsmyip.com/")
    driver.implicitly_wait(4)
    words = driver.find_element(By.ID,"shownIpv4")
    if words.text != config.proxy:
        print("Ip not matching config proxy IP!")
        sys.exit()

    

def login():      
    driver.get("https://www.plemiona.pl/")
    driver.find_element(By.ID, 'user').send_keys(config.user)
    driver.find_element(By.ID, 'password').send_keys(config.password)
    driver.implicitly_wait(12)
    login_button = driver.find_elements(By.CLASS_NAME, 'btn-login')
    login_button[0].click()
    time.sleep(1)
    driver.get(config.world)    

def send_nottification(marks):
    new_labels = driver.find_elements(By.CLASS_NAME, 'quickedit-label')
    amount = len(marks)
    msg = "" + str(amount) + " nowe ataki!"
    for mark in marks:
            msg += " | " + new_labels[mark].text
    disco.send(msg)


def check_for_new_attacks():
    try:
        attacks = int(driver.find_element(By.ID, 'incomings_amount').text)
    except:
        attacks = 0
    if attacks != 0 and config.attacks < attacks:
        driver.find_element(By.ID, 'incomings_amount').click()
        labels = driver.find_elements(By.CLASS_NAME, 'quickedit-label')
        marks = list()
        number = 0
        for label in labels:
            if(label.text == 'Atak'):
                marks.append(number)
            number += 1
        if len(marks) != 0:
            driver.find_element(By.CLASS_NAME, "selectAll").click()
            driver.find_element_by_name("label").click()
            send_nottification(marks)
            #time.sleep(1)
    config.attacks = attacks


def check_for_dodge():
    labels = driver.find_elements(By.CLASS_NAME, 'quickedit-label')
    number = 2
    to_dodge = True
    dodge_target = "0"
    #print(len(labels)+2)
    length = len(labels)+2
    while (number<length and to_dodge):
        driver.implicitly_wait(5)
        href_id = driver.find_element_by_xpath("//*[@id=\"incomings_table\"]/tbody/tr["+str(number)+"]/td[1]/span/span/a[1]").get_attribute("href")
        href_id = re.search('info_command&id=[0-9]+', href_id).group()
        dodge_bool = True
        if len(config.attack_href) != 0:
            for href in config.attack_href:
                if href == href_id:
                    dodge_bool = False

        if dodge_bool:
            text = driver.find_element_by_xpath("//*[@id=\"incomings_table\"]/tbody/tr["+ str(number) +"]/td[7]/span").text
            if len(text) == 7:
                hours = int(text[0])
            else:
                hours = int(text[0:2])
            seconds = int(text[-2:])
            minutes = int(text[-5:-3])
            #print(str(hours) + " " + str(minutes) + " " + str(seconds) + " ")
            if hours > 0 or minutes > 0 or seconds > 55:
                to_dodge = False
            else:
                config.attack_href.append(href_id)
                time_left = seconds + minutes*60 + hours*3600
                time_check = time.time()
                if dodge_target == "0":
                    driver.find_element_by_xpath("//*[@id=\"menu_row\"]/td[10]/a").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"content_value\"]/table/tbody/tr/td[3]/a").click()
                    try:
                        if driver.find_element_by_xpath("//*[@id=\"form_rights\"]/table/tbody/tr[2]/td[1]/a").text != config.user:
                            driver.find_element_by_xpath("//*[@id=\"form_rights\"]/table/tbody/tr[2]/td[1]/a").click()
                        else:
                            driver.find_element_by_xpath("//*[@id=\"form_rights\"]/table/tbody/tr[3]/td[1]/a").click()
                    except:
                        if driver.find_element_by_xpath("//*[@id=\"ally_content\"]/table/tbody/tr[2]/td[1]/a").text != config.user:
                            driver.find_element_by_xpath("//*[@id=\"ally_content\"]/table/tbody/tr[2]/td[1]/a").click()
                        else:
                            driver.find_element_by_xpath("//*[@id=\"ally_content\"]/table/tbody/tr[3]/td[1]/a").click()
                    dodge_target = re.search('[0-9]+\|[0-9]+', driver.find_element_by_xpath("//*[@id=\"villages_list\"]/tbody/tr[1]").text).group()       
                village_xpath = "//*[@id=\"incomings_table\"]/tbody/tr["+str(number)+"]/td[2]/a"
                time.sleep(1)
                #print(text)
                dodge(village_xpath,dodge_target,time_check, time_left)
        number += 1


def dodge(village_xpath,target, time_check, time_left):
    #Send
    driver.implicitly_wait(12)
    driver.find_element(By.ID, 'incomings_amount').click()
    time.sleep(1)
    driver.implicitly_wait(12)
    driver.find_element_by_xpath(village_xpath).click()

    village_url = driver.current_url
    
    time.sleep(1)
    driver.implicitly_wait(12)
    driver.find_element_by_xpath("//*[@id=\"l_place\"]/td[2]/a").click()
    time.sleep(1)
    driver.implicitly_wait(12)
    driver.find_element(By.ID, 'selectAllUnits').click()
    #print(target)
    spot = '/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/div[1]/table/tbody/tr[1]/td/div[2]/input'
    driver.implicitly_wait(12)
    driver.find_element_by_xpath(spot).send_keys(target)
    time.sleep(4)
    driver.implicitly_wait(12)
    if driver.find_element_by_xpath("//*[@id=\"units_entry_all_spear\"]").text != "(0)":
        driver.find_element(By.ID, 'target_support').click()
        time.sleep(2)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id=\"troop_confirm_go\"]").click()

        time_difference = time.time() - time_check
        time_left -= time_difference 
        time_to_cancel = time_left/2 + 1

        new = True

        for item in config.village_url:
            if item == village_url:
                index = config.village_url.index(village_url)
                config.time_to_cancel[index] = time_to_cancel - (time.time() - config.time_dodge[index])
                new = False
                break

        if new:
            config.time_to_cancel.append(time_to_cancel)
            config.village_url.append(village_url)
            config.time_dodge.append(time.time())

    driver.find_element(By.ID, 'incomings_amount').click()

    

def cancel_dodge():
    if len(config.time_to_cancel) != 0:
        for item in config.time_to_cancel:
            index = config.time_to_cancel.index(item)
            if item < (time.time()-config.time_dodge[index]):
                print('cancel')
                driver.get(config.village_url[index])
                driver.find_element(By.CLASS_NAME, "command-cancel").click()
                config.time_dodge[index] = 0
                config.time_to_cancel[index] = 0
                config.village_url[index] = "0"
        driver.find_element(By.ID, 'incomings_amount').click()

    
    leng = 0
    while leng != len(config.time_dodge):
        leng = len(config.time_dodge)
        try:
            config.time_dodge.remove(0)
            config.time_to_cancel.remove(0)
            config.village_url.remove("0")
        except:
            pass



def get_game_data():
    
    config.villages = list()

    idd = re.search('id\":[0-9]+', driver.page_source).group()
    idd = re.search('[0-9]+', idd).group()

    driver.get('https://pl141.plemiona.pl/game.php?village='+idd+'&screen=overview_villages&mode=buildings&group=0&')

    #driver.find_element_by_xpath('//*[@id="menu_row"]/td[2]/a').click()
    #driver.find_element_by_xpath('//*[@id="overview_menu"]/tbody/tr/td[7]/a').click()
    try:
        queue = driver.find_elements(By.CLASS_NAME, 'queueRow')
    except:
        pass
    inner = '''<td>
                    </td>'''
    supp = re.search('villages\":\"[0-9]+', driver.page_source).group()
    number_of_vill = int(re.search('[0-9]+', supp).group())
    number = 0
    while number < number_of_vill:
        idd = re.search('id\":[0-9]+', driver.page_source).group()
        idd = int(re.search('[0-9]+', idd).group())
        wood = re.search('wood\":[0-9]+', driver.page_source).group()
        wood = int(re.search('[0-9]+', wood).group())
        stone = re.search('stone\":[0-9]+', driver.page_source).group()
        stone = int(re.search('[0-9]+', stone).group())
        iron = re.search('iron\":[0-9]+', driver.page_source).group()
        iron = int(re.search('[0-9]+', iron).group())
        supp = re.search('pop\":[0-9]+', driver.page_source).group()
        pop = int(re.search('[0-9]+', supp).group())
        supp = re.search('pop_max\":[0-9]+', driver.page_source).group()
        pop_max = int(re.search('[0-9]+', supp).group())
        supp = re.search('storage_max\":[0-9]+', driver.page_source).group()
        storage_max = int(re.search('[0-9]+', supp).group())
        supp = re.search('main\":\"[0-9]+', driver.page_source).group()
        main = int(re.search('[0-9]+', supp).group())
        supp = re.search('barracks\":\"[0-9]+', driver.page_source).group()
        barracks = int(re.search('[0-9]+', supp).group())
        supp = re.search('stable\":\"[0-9]+', driver.page_source).group()
        stable = int(re.search('[0-9]+', supp).group())
        supp = re.search('garage\":\"[0-9]+', driver.page_source).group()
        garage = int(re.search('[0-9]+', supp).group())
        supp = re.search('snob\":\"[0-9]+', driver.page_source).group()
        snob = int(re.search('[0-9]+', supp).group())
        supp = re.search('smith\":\"[0-9]+', driver.page_source).group()
        smith = int(re.search('[0-9]+', supp).group())
        supp = re.search('place\":\"[0-9]+', driver.page_source).group()
        place = int(re.search('[0-9]+', supp).group())
        supp = re.search('statue\":\"[0-9]+', driver.page_source).group()
        statue = int(re.search('[0-9]+', supp).group())
        supp = re.search('market\":\"[0-9]+', driver.page_source).group()
        market = int(re.search('[0-9]+', supp).group())
        supp = re.search('wood\":\"[0-9]+', driver.page_source).group()
        wood_b = int(re.search('[0-9]+', supp).group())
        supp = re.search('stone\":\"[0-9]+', driver.page_source).group()
        stone_b = int(re.search('[0-9]+', supp).group())
        supp = re.search('iron\":\"[0-9]+', driver.page_source).group()
        iron_b = int(re.search('[0-9]+', supp).group())
        supp = re.search('farm\":\"[0-9]+', driver.page_source).group()
        farm = int(re.search('[0-9]+', supp).group())
        supp = re.search('storage\":\"[0-9]+', driver.page_source).group()
        storage = int(re.search('[0-9]+', supp).group())
        supp = re.search('wall\":\"[0-9]+', driver.page_source).group()
        wall = int(re.search('[0-9]+', supp).group())

        if inner==driver.find_element_by_xpath('//*[@id="v_'+str(idd)+'"]/td[20]').get_attribute('outerHTML'):
            upgrading=False
        else:
            upgrading=True

        config.add_village(list(),upgrading,idd,wood,stone,iron,main,barracks,stable,garage,snob,smith,place,statue,market,wood_b,stone_b,iron_b,farm,storage,wall,storage_max,pop_max,pop)
        driver.find_element_by_xpath("//*[@id=\"village_switch_right\"]/span").click()
        number+=1



def build():
    orders = bot.main()
    print(orders)
    for command in orders:
        if command != 100:
            driver.get('https://pl141.plemiona.pl/game.php?village='+str(command[1])+'&screen=overview')
            if command[0] == 0:
                driver.find_element_by_xpath('//*[@id="upgrade_level_main"]').click()
            if command[0] == 1:
                driver.find_element_by_xpath('//*[@id="upgrade_level_barracks"]').click()
            if command[0] == 2:
                driver.find_element_by_xpath('//*[@id="upgrade_level_stable"]').click()
            if command[0] == 3:
                driver.find_element_by_xpath('//*[@id="upgrade_level_garage"]').click()
            if command[0] == 4:
                driver.find_element_by_xpath('//*[@id="upgrade_level_smith"]').click()
            if command[0] == 5:
                driver.find_element_by_xpath('//*[@id="upgrade_level_place"]').click()
            if command[0] == 6:
                driver.find_element_by_xpath('//*[@id="upgrade_level_market"]').click()
            if command[0] == 7:
                driver.find_element_by_xpath('//*[@id="upgrade_level_wood"]').click()
            if command[0] == 8:
                driver.find_element_by_xpath('//*[@id="upgrade_level_stone"]').click()
            if command[0] == 9:
                driver.find_element_by_xpath('//*[@id="upgrade_level_iron"]').click()
            if command[0] == 10:
                driver.find_element_by_xpath('//*[@id="upgrade_level_farm"]').click()
            if command[0] == 11:
                driver.find_element_by_xpath('//*[@id="upgrade_level_storage"]').click()
            if command[0] == 12:
                driver.find_element_by_xpath('//*[@id="upgrade_level_wall"]').click()
            if command[0] == 13:
                driver.find_element_by_xpath('//*[@id="upgrade_level_snob"]').click()
            if command[0] == 14:
                driver.find_element_by_xpath('//*[@id="upgrade_level_statue"]').click()

def recruitment():
    driver.get('https://pl141.plemiona.pl/game.php?village='+str(config.villages[0].idd)+'&screen=train&mode=mass&group='+config.group_def+'&')
    driver.find_element_by_xpath('//*[@id="content_value"]/div[2]/div[2]/input[3]').click()
    driver.find_element_by_xpath('//*[@id="mass_train_form"]/input[1]').click()
    driver.get('https://pl141.plemiona.pl/game.php?village='+str(config.villages[0].idd)+'&screen=train&mode=mass&group='+config.group_off+'&')
    driver.find_element_by_xpath('//*[@id="content_value"]/div[2]/div[2]/input[3]').click()
    driver.find_element_by_xpath('//*[@id="mass_train_form"]/input[1]').click()

#------------------CODE--------------------


#driver = webdriver.Firefox(executable_path ="D:\\Python_all\\browsers\\geckodriver.exe")
driver = webdriver.Firefox(executable_path ="C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python37\\geckodriver.exe")

#check_ip()
login()

while True:
    #check_for_new_attacks()
    #if config.attacks != 0:
        #check_for_dodge()
        #cancel_dodge()
    get_game_data()
    build()
    recruitment()
    time.sleep(20)
