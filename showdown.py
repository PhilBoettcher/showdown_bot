from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from time import sleep

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

        
        
        
        
        
        
    


# Showdown().login()