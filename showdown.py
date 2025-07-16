from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from time import sleep

from selenium.common.exceptions import NoSuchElementException

class Showdown:
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://play.pokemonshowdown.com/')
        # self.driver.maximize_window()
        sleep(3)
    
    def login(self):
        login = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/button[1]')
        login.click()
        sleep(1)
        
        load_dotenv(dotenv_path='.venv/.env')
        user_entry = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/form/p[1]/label/input')
        user_entry.send_keys(os.getenv("SHOWDOWN_USERNAME"))
        
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/form/p[2]/button[1]/strong').click()
        sleep(1)
        
        password_entry = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/form/p[4]/label/input')
        password_entry.send_keys(os.getenv("SHOWDOWN_PASSWORD"))
        
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/form/p[5]/button[1]/strong').click()
        sleep(1)

    def find_randbat(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div[1]/form/p[5]/button/strong').click()
        sleep(20)
        
    def toggle_timer(self):
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[1]/button').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/p/button/strong').click()
        
    def toggle_sound(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/button[1]').click() # sound button
        sleep(0.1)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/p[4]').click() # checkbox
        sleep(0.1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/button[1]').click() # sound button
        
    def exit_match(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/ul[2]/li/button').click()
        
    def select_move(self, moveslot):
        self.driver.find_element(By.XPATH, f'/html/body/div[4]/div[5]/div/div[2]/div[2]/button[{moveslot}]').click()
                                          #  /html/body/div[4]/div[5]/div/div[2]/div[2]/button[1]
        
    def toggle_gimmick(self):
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[2]/div[2]/div[1]/label').click()
        
    def swap_out(self, partyslot):
        self.driver.find_element(By.XPATH, f'/html/body/div[4]/div[5]/div/div[3]/div[2]/button[{partyslot}]').click()
                                          #  /html/body/div[4]/div[5]/div/div[3]/div[2]/button[2]
                                          #  /html/body/div[4]/div[5]/div/div[3]/div[2]/button[3]
        
        
        
        
        
    
if __name__ == '__main__':
    
    showdown = Showdown()
    showdown.login()
    while True:
        try:
            action = int(input())
            if action == 2:
                showdown.find_randbat()
            if action == 3:
                showdown.toggle_timer()
            if action == 4:
                moveslot = input('which moveslot')
                moveslot = int(moveslot)
                showdown.select_move(moveslot)
            if action == 5:
                partyslot = input('which partyslot')
                partyslot = int(partyslot)
                showdown.swap_out(partyslot)
            if action == 6:
                showdown.toggle_sound()
            if action == 7:
                showdown.exit_match()
            if action == 8:
                showdown.toggle_gimmick()
        except NoSuchElementException:
            print('oopsie')
            