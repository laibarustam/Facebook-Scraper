
---

# Facebook Scraper Using Selenium and BeautifulSoup

A web scraper built using Python, Selenium, and BeautifulSoup that logs into Facebook, searches for a specific account, and extracts details such as the account name, about section, and posts. The extracted data is saved in a structured JSON file.

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)

  * [Clone the Repository](#clone-the-repository)
  * [Install Dependencies](#install-dependencies)
  * [Configure Facebook Login](#configure-facebook-login)
* [How to Run the Scraper](#how-to-run-the-scraper)
* [Code Explanation](#code-explanation)
* [Known Issues](#known-issues)
* [Contributing](#contributing)
* [Contact](#contact)

## Features

* **Automated Login**: The scraper automatically logs into Facebook using a provided email and password.
* **Account Search**: Searches for a specific Facebook account by name.
* **Data Extraction**: Extracts account name, about description, and posts from the Facebook account's page.
* **Page Scrolling**: Automatically scrolls down the page to load all posts.
* **Data Storage**: Saves the extracted data (account name, about, and posts) to a structured JSON file.
* **Error Handling**: Handles errors gracefully during data extraction, logging relevant messages.

## Requirements

Before running the scraper, ensure the following prerequisites are met:

* **Python 3.x**: Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/downloads/).
* **Selenium**: For browser automation.
* **BeautifulSoup**: For parsing HTML data.
* **WebDriver**: You'll need the Chrome WebDriver, compatible with your Chrome version.
* **Chrome Browser**: Installed on your machine.

### Install the Required Libraries

Run the following command to install the necessary dependencies:

```bash
pip install selenium beautifulsoup4
```

## Installation

### Clone the Repository

1. First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/facebook-scraper.git
cd facebook-scraper
```

### Install Dependencies

2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

3. **Download ChromeDriver**:

   * Download the appropriate version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) based on your installed version of Chrome.
   * Place the `chromedriver` executable in the project directory or specify its path in the script.

### Configure Facebook Login

1. **Facebook Credentials**: Replace the following lines with your Facebook login credentials in the script (`facebook_scraper.py`):

```python
email.send_keys('your-email@example.com')
password.send_keys('your-password')
```

## How to Run the Scraper

Once you have installed the dependencies and configured the scraper, you can run it using the following command:

```bash
python facebook_scraper.py
```

* The script will open Chrome, log into Facebook, search for the specified account, and scrape the account’s details and posts.
* The results will be saved in `facebook_posts.json`.

### Example Output

The output JSON file (`facebook_posts.json`) will have the following structure:

```json
{
    "account_name": "Hania Amir Official",
    "about": "No information available.",
    "posts": [
        {
            "post_number": 1,
            "content": "Post content here"
        },
        {
            "post_number": 2,
            "content": "Post content here"
        }
    ]
}
```

## Code Explanation

### 1. Logging In

* The script uses Selenium to automate the login process by filling in the email and password fields and clicking the login button.
* The login process waits for the elements to be clickable and then submits the credentials.

### 2. Searching for an Account

* Once logged in, the script waits for the search bar to load and performs a search for the specified Facebook account.

### 3. Extracting Account Data

* The script uses BeautifulSoup to parse the page source and extract the account name and about description.
* If the elements are not found, error messages are logged.

### 4. Scrolling and Extracting Posts

* The script simulates scrolling down the page to load more posts. It waits for the page to load, then collects the post content.
* All the posts are stored in a list, and the information is saved into a JSON file.

### 5. Saving Data

* The extracted data (account name, about section, and posts) is saved in a structured JSON format for later use.

## Known Issues

* **Login Failures**: The login process may fail if Facebook's security checks change. Consider using two-factor authentication or handling CAPTCHA.
* **Dynamic Content**: Facebook may change its structure or class names, which could break the scraper. Update the XPaths and class names if necessary.
* **ChromeDriver Compatibility**: Ensure that the ChromeDriver version matches your Chrome browser version.

## Contributing

Contributions are welcome! If you'd like to improve the scraper or add new features, feel free to fork the repository, make changes, and submit a pull request.

### How to Contribute

1. Fork the repository.
2. Clone your forked repository:

```bash
git clone https://github.com/yourusername/facebook-scraper.git
```

3. Create a new branch:

```bash
git checkout -b new-feature
```

4. Make your changes and commit them:

```bash
git commit -m "Add new feature"
```

5. Push your changes:

```bash
git push origin new-feature
```

6. Submit a pull request from your fork to the main repository.

## Contact

If you have any questions or feedback, feel free to open an issue or contact me directly at \[(laibarustam858@gmail.com)].

---

