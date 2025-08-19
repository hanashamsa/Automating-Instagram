# Instagram Automation Bot

This project is a **Python-based Instagram automation bot** built with **Selenium**. It automates the following tasks:

* Logging into Instagram using credentials stored in a `.env` file.
* Handling the **cookies consent popup** (accept all cookies).
* Entering **username and password correctly** with controlled delays.
* Dismissing the **“Save Your Login Info”** and **“Turn On Notifications”** popups.
* Liking the **first post** on the feed automatically.

---

##  Features

* Secure credential storage using `.env`.
* Automated interaction with Instagram web UI.
* Handles common popups (cookies, login save prompt, notifications).
* Performs a like action on the first visible post.
* Clean and extendable codebase for adding more actions.

---

##  Project Structure


instagram-bot/


* **`.env`** → Stores Instagram username & password.
* **`main.py`** → Main automation script.
* **`requirements.txt`** → Dependencies.
* **`README.md`** → Project documentation.

---

##  Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/instagram-bot.git
cd instagram-bot
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a `.env` file in the project root:

```
INSTA_USERNAME=your_username
INSTA_PASSWORD=your_password
```


---

##  Usage

Run the script:

```bash
python main.py
```

The bot will:

1. Open Instagram in Chrome.
2. Accept all cookies.
3. Log in using your credentials.
4. Dismiss popups like *“Save login info”* and *“Turn on notifications”*.
5. Like the first post on your feed.

---

##  Requirements

* Python **3.8+**
* Google Chrome (latest version)
* [ChromeDriver](https://chromedriver.chromium.org/downloads) (matching your Chrome version)
* Selenium

Install Selenium with:

```bash
pip install selenium
```

---

## Disclaimer

This project is for **educational purposes only**.
Automating Instagram may violate its [Terms of Service](https://help.instagram.com/581066165581870). Use responsibly at your own risk.


