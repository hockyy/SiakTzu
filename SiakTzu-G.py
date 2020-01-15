from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
login_url = "https://academic.ui.ac.id/main/Authentication/"
homepage_url = "https://academic.ui.ac.id/main/Welcome/"
logout_url = "https://academic.ui.ac.id/main/Authentication/Logout"
#siak_url = "https://academic.ui.ac.id/main/CoursePlan/CoursePlanEdit"
siak_url = "file:///home/hiddentesla/GitRepos/PPW/SiakTzu/Web/Penambahan%20IRS%20-%20Dennis%20Al%20Baihaqi%20Walangadi%20(1906400141)%3B%20Kurikulum%2009.00.12.01-2016%20CoursePlanEdit%20-%20SIAK%20NG.html"

down_string = "Universitas Indonesia"
matkul_code = {"608483-4": "SDA-A",
               "608238-3": "Basdat Lanjut",
               "608450-4": "DAA",
               "123456-1": "Dasar-Dasar Raiton"}

# fill your login credentials here
user = ""
passw = ""
display_name = "" # yang ditampilin di pojok kanan atas siak. ex: Galangkangin Gotera

def logout_page():
    driver.get(logout_url)
    time.sleep(0.5)

def login_page():
    #driver.get(login_url)

    username = driver.find_element_by_name("u")
    username.clear()
    username.send_keys(user)
    time.sleep(0.1)

    password = driver.find_element_by_name("p")
    password.clear()
    password.send_keys(passw)
    time.sleep(0.1)
    driver.find_element_by_xpath("//input[@value='Login']").click()
    time.sleep(2)

def war_page():
    #driver.get(siak_url)
    time.sleep(5)
    for kode, name in matkul_code.items():

        # antisipasi salah masukkin kode
        try:
            radio_input = driver.find_element_by_xpath(f"//input[@value='{kode}']")
            if(not radio_input.is_selected()): 
                radio_input.click()
                print(f"{name} dipilih! (kode: {kode})")
                time.sleep(0.1)
            else :
                print(f"{name} sudah dipilih! (kode: {kode})")
        except:
            print(f"{name} tidak ada! (kode: {kode})")
            time.sleep(5)

    button = driver.find_element_by_xpath("//input[@value='Simpan IRS']")
    button.click()

if __name__ == "__main__":
    #new_term = "Tahun Ajaran 2019/2020 Term 1"
    driver.get(login_url)
    time.sleep(0.5)

    while(True):

       # print(driver.current_url)

        # refresh manual bre
        while(not display_name in driver.page_source and 
              not "Magister Kriminologi" in driver.page_source):
            pass

        # login
        if "Magister Kriminologi" in driver.page_source:
            login_page()
            continue

        # case di homepage
        if driver.current_url == homepage_url:
            driver.get(siak_url)
            time.sleep(0.5)
            continue

        # case di tempat irs
        if "CoursePlanEdit" in siak_url:

            # logout, belom bisa ngisi
            if not "Basis Data" in driver.page_source:
                print("BELUM BISA NGISI")
                logout_page()
                continue

            war_page()
            time.sleep(2)

            # kalau gagal, ulang lagi ngisinya
            if (not display_name in driver.page_source):
                print("ngulang isi bre")
                driver.get(siak_url)
                time.sleep(0.5)
                continue

            print("SUKSESS")
            break # SUKSES!!!

            