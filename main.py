from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Facebook
    driver.get("https://www.facebook.com")
    time.sleep(10)  # Adjust if necessary
    print("Opened Facebook")

    # Log in to Facebook
    email = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
    email.send_keys('03481540873')  # Replace with your Facebook email
    print("Entered email")

    password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
    password.send_keys('Laibakhan48@')  # Replace with your Facebook password
    print("Entered password")

    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'login')))
    button.click()
    time.sleep(10)  # Adjust if necessary
    print("Clicked login button")

    # Wait for the page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Search Facebook"]')))
    time.sleep(5)  # Adjust if necessary
    print("Page loaded")

    # Search for the specific account using the search bar
    search_bar = driver.find_element(By.XPATH, '//*[@aria-label="Search Facebook"]')
    search_bar.send_keys('Hania Amir Official')  # Replace with the name of the Facebook account you want to search for
    search_bar.send_keys(Keys.RETURN)
    print("Performed search")

    # Wait for the search results to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@role='feed']")))
    time.sleep(5)  # Wait for search results to load
    print("Search results loaded")

    # Click on the specific account
    try:
        account_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'HaniaAmirOfficial')]"))  # Replace with correct unique part of the account URL
        )
        account_link.click()
        print("Clicked on account link")
    except Exception as e:
        print(f"Error finding account link: {e}")
        driver.quit()
        exit()

    # Wait for the account's page to load
    time.sleep(5)
    print("Account page loaded")

    # Save page source for inspection
    page_source = driver.page_source
    with open("page_source.html", "w", encoding="utf-8") as f:
        f.write(page_source)
    print("Saved page source for inspection")

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract account name
    try:
        username_element = soup.find('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1sur9pj xkrqix3 x1s688f xq9mrsl')
        user_name = username_element.text if username_element else "Username not found"
        print(f"Username: {user_name}")
    except Exception as e:
        print(f"Could not find the username: {e}")

    # Extract account description
    try:
        account_about_element = soup.find('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1nxh6w3 x1sibtaa xo1l8bm xi81zsa')
        account_about = account_about_element.text if account_about_element else "No information available."
        print(f"About: {account_about}")
    except Exception as e:
        print(f"Could not find the account description: {e}")

    # Scroll down to load all posts
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(5)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Find all posts
    posts = driver.find_elements(By.XPATH, "//div[@data-ad-preview='message']")

    # Extract post content and save to list
    posts_data = []
    for i, post in enumerate(posts):
        try:
            content = post.text
            posts_data.append({
                'post_number': i + 1,
                'content': content
            })
            print(f"Post {i + 1}: {content}")
        except Exception as e:
            print(f"Error extracting post content: {e}")
            continue

    # Save the account name, about, and post data to a JSON file
    data = {
        'account_name': user_name,
        'about': account_about,
        'posts': posts_data
    }

    with open('facebook_posts.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Saved posts to facebook_posts.json")
    print(f"Total number of posts: {len(posts_data)}")

finally:
    # Close the WebDriver
    driver.quit()
    print("Closed WebDriver")
