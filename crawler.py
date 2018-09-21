# Import the libraries
from selenium import webdriver
import time
import os

# URL of page
url = "http://www.indiabix.com/c-programming/declarations-and-initializations/"

# Declare Chrome object
browser = webdriver.Chrome("chromedriver")

# Fetch the webpage
browser.get(url)

# Find title of the page
title = browser.title

# Clean the title
title = title.split("-")[0].lower().replace(" ", "_")

# Create a directory to store images
if not os.path.exists(title):
    os.mkdir(title)

k = 0

file = open(title + ".csv", "a+")
file.write("Question, A, B, C, D, Correct")
file.write("\n")

while True:
    
    # Scrape the questions
    questions = browser.find_elements_by_class_name("bix-td-qtxt")
    questions = [question.text for question in questions]
    
    # Scrape the options
    options = browser.find_elements_by_class_name("bix-tbl-options")
    options = [option.text.split("\n") for option in options]
    
    opts = []
    
    for option in options:
        opt = []
        flag = False
        for o in option:
            try:
                opt.append(o[o.index('.')+2:])
            except:
                opt = []
        if(not flag):
            opts.append(opt)
        
    # Click the view answers
    view_answers = browser.find_elements_by_class_name("answer")
    for i in range(len(view_answers)):
        view_answers[i].click()
        time.sleep(2)
        
    # Scrape the answers
    answers = browser.find_elements_by_class_name("jq-hdnakqb")
    answers = [answer.text for answer in answers]
    
    idx = []
    
    for i in range(len(questions)):
        if(len(opts[i]) < 4):
            idx.append(i)
            continue
        else:
            file.write(questions[i].replace(",", "") + ",")
            for j in range(len(opts[i])):
                file.write(opts[i][j].replace(",", "") + ",")
            file.write(answers[i] + "\n")
    
    # Screenshot the explanations
    explanations = browser.find_elements_by_class_name("bix-ans-description")
    for i in range(len(explanations)):
        if(len(idx) > 0 and i in idx):
            continue
        else:
            browser.execute_script("arguments[0].scrollIntoView();", explanations[i])
            if "No answer" not in explanations[i].text:    
                browser.get_screenshot_as_file(title + '/image' + str(k) + '.png')
                time.sleep(2)
            k += 1
        
    # Move to next page
    try:          
        browser.find_element_by_link_text("Next »").click()
    except:
        break
    
file.close()

# Close the browser session
browser.close()