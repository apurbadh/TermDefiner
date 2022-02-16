import wikipedia
from selenium.webdriver import Chrome
import os
from time import sleep 

PATH = os.path.join(os.getcwd(), 'driver', 'chromedriver')


def open_website(url):
    browser = Chrome(executable_path=PATH)
    browser.get(url)
    sleep(100)


def main():

    user_word = input("Enter a term you want to get defination : ")
    
    word = wikipedia.page(user_word)
    
    if user_word.title() == word.title:
        
        print(word.summary)
        
    else:
        
        yon = input(f"Did you mean {word.title} (Y/n) ?")
        
        if yon.upper() == 'Y':
            
            print(word.summary)
        
        else:
            
            search_res = wikipedia.search(user_word)
            
            for i in range(len(search_res)):
                print(f"{i + 1}. {search_res[i]}")
                
            
            user_num = int(input("Which of the above did you mean ? "))
            word = wikipedia.page(search_res[user_num - 1])
            
            print(word.summary)
            
    ch = input("Do you want to open the wikipedia page (Y/n) ? ")
    
    if ch.upper() == 'Y':
        open_website(word.url)



main()