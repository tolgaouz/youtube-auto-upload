import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from cookies import chrome_cookies
  
class Uploader():

  """

  Uploader object which would handle all the upload functions
  as well as browser automation via Selenium
  
  
  """
  def init_video(self,filepath):

    """

    A function to read below parameters from json file:
    Title *Required
    Description,
    Tags,
    Category,
    Age Restrictions

    Which are held in a json file. Initiate an object with passing the 
    file path as the parameter.

    """

    # If only the filename is given, add the extension
    if not ('.json' in filepath):
      filepath+='.json'
    with open(filepath,'w') as fl:
      data = json.load(fl)
    return data

  def __init__(self,visible=False):
    # Initialize the browser object
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    if visible:
      chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1280,800")
    self.browser = webdriver.Chrome(chrome_options=chrome_options)
  
  def get_cookies(self):

    """

    Gets cookies from user's default chrome browser,
    User has to be logged in to YouTube in default Chrome Browser
    for this function to return cookies.

    """
    self.cookies = chrome_cookies('https://www.youtube.com')
    return cookies
    
  def inject_cookies(self):

    """

    Inject cookies to the browser object

    """
    # Go to youtube.com so that we can inject the cookies
    self.browser.get('https://www.youtube.com')
    
    # inject cookies to the Chrome Browser that is used by Selenium
    for c in cookies:
        # set expiry date to infinity or something
        c['expiry'] = 33333333333
        self.browser.add_cookie(c)

  def upload_video(self,filepath):

    """

    Gets video data, then uploads it by automating clicks and actions on Selenium
    WebDriver object.

    """
    # read video data
    data = self.init_video(filepath)
    # if title is not in data, return immediately
    if 'title' not in data.keys():
      raise Exception('Field Required (title and video_path are required)')
    # navigate to the upload page
    browser.get('https://studio.youtube.com/')
    # click on 'Create' button
    browser.find_element_by_id('create-icon').click()
    # Click on 'Upload Video'
    browser.find_element_by_css_selector('paper-listbox > paper-item').click()
    # Get Input Element
    browser.find_element_by_css_selector('input[name="Filedata"]').send_keys(data['video_path'])
    # Title
    browser.find_element_by_id('textbox').send_keys(data.title)
    # Desc
    browser.find_element_by_class_name('description-textarea').find_element_by_css_selector('div#textbox').send_keys(data.desc)

    ## TODO: Add Other functionalities here!
    ## TODO: Add info about video upload here!

    # Next
    browser.find_element_by_id('next-button').click()
    browser.find_element_by_id('next-button').click()

    visibilities = ['PUBLIC','UNLISTED','PRIVATE']
    browser.find_element_by_css_selector('paper-radio-button[name="'+visibilities[0]+'"]').click()  

    # Done
    browser.find_element_by_id('done-button').click()
