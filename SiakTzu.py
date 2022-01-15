from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import time
import datetime

options = Options()
driver = webdriver.Firefox(options=options)
login_url = "https://academic.ui.ac.id/main/Authentication/"
homepage_url = "https://academic.ui.ac.id/main/Welcome/"
logout_url = "https://academic.ui.ac.id/main/Authentication/Logout"
siak_url = "https://academic.ui.ac.id/main/CoursePlan/CoursePlanEdit"
# siak_url = "file:///C:/Users/ASUS/Desktop/SiakTzu/Web/Penambahan%20IRS%20-%20Dennis%20Al%20Baihaqi%20Walangadi%20(1906400141)%3b%20Kurikulum%2009.00.12.01-2016%20-%20SIAK%20NG.html"

down_string = "Universitas Indonesia"
matkul_code = {"620020-4": "DDP 2 - B",
               "620207-4": "PSD - A",
               "620077-3": "MatDas 1-A",
               "620137-3": "MD 2 - E",
               "620289-3": "CP",
               "620173-6": "MPKT A - C"}
# matkul_code = { "607788-4": "DDP 1 - A",
#                 "608186-3": "MD 1 - G"}

# fill your login credentials here
Username = ""
Password = ""
refresh_rate = 1
display_name = "Hocky Yudhiono" # yang ditampilin di pojok kanan atas siak. ex: Galangkangin Gotera

def logout_page():
    print("Logging out!")
    driver.get(logout_url)
    time.sleep(0.1)

def login_page():
    #driver.get(login_url)

    username = driver.find_element_by_name("u")
    username.clear()
    username.send_keys(Username)
    time.sleep(0.1)

    password = driver.find_element_by_name("p")
    password.clear()
    password.send_keys(Password)
    time.sleep(0.1)
    driver.find_element_by_xpath("//input[@value='Login']").click()
    time.sleep(2)

def war_page():
    # driver.get(siak_url)
    time.sleep(5)
    for kode, name in matkul_code.items():

        # antisipasi salah masukkin kode
        try:
            radio_input = driver.find_element_by_xpath(f"//input[@value='{kode}']")
            if(not radio_input.is_selected()): 
                radio_input.click()
                print(f"{name} dipilih! (kode: {kode})")
                time.sleep(0.1)
            else:
                print(f"{name} sudah dipilih! (kode: {kode})")
        except:
            print(f"{name} tidak ada! (kode: {kode})")
            time.sleep(10)

    button = driver.find_element_by_xpath("//input[@value='Simpan IRS']")
    button.click()

if __name__ == "__main__":
    error = True
    while(True):
        try:
            if(error):
                error = False
                driver.get(login_url)
            refresh_rate = 10
            if(datetime.datetime.now().minute >= 50): refresh_rate = 3
            if(datetime.datetime.now().minute >= 55 or datetime.datetime.now().minute <= 5): refresh_rate = 0.5
            time.sleep(refresh_rate)
            print(datetime.datetime.now())
            # print(driver.current_url)

            # refresh manual bre
            if(driver.current_url != "https://academic.ui.ac.id/main/Welcome/" and not "Magister Kriminologi" in driver.page_source):
                print("Trying to login bro!")
                driver.get(login_url)
                continue
            elif(driver.current_url != "https://academic.ui.ac.id/main/Welcome/"):
                login_page()
                time.sleep(refresh_rate)
                print(datetime.datetime.now())
                print("Sended login request bro!")
            if(not display_name in driver.page_source):
                print("Siak down bro!")
                time.sleep(0.2)
                driver.get(login_url)
                continue
            if("guest" in driver.page_source):
                print("Role guest bro!")
                time.sleep(0.2)
                logout_page()
                driver.get(login_url)
                continue
            print("BOI SAFELY LOGGED IN!")
            # case di homepage
            driver.get(siak_url)
            # logout, belom bisa ngisi
            if not "Basis Data" in driver.page_source:
                print("BELUM BISA NGISI")
                logout_page()
                driver.get(login_url)
                continue
            war_page()
            # kalau gagal, ulang lagi ngisinya
            if (not display_name in driver.page_source):
                print("ngulang isi bre")
                driver.get(siak_url)
                time.sleep(0.5)
                continue
            print("SUKSESS")
            break # SUKSES!!!
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Error happened")
            time.sleep(0.5)
            error = True
            continue