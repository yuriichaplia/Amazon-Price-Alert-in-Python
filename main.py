import smtplib
import requests
from os import environ
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

TO_EMAIL = environ["TO_EMAIL"]
MY_EMAIL = environ["MY_EMAIL"]
SMTP_EMAIL = environ["SMTP_EMAIL"]
AMAZON_URL = environ["AMAZON_URL"]
MY_PASSWORD = environ["MY_PASSWORD"]

headers = {
    'USER-AGENT': environ["USER_AGENT"],
    'ACCEPT-LANGUAGE': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7'
}

response = requests.get(AMAZON_URL, headers=headers)
content = response.text

soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())

try:
    price: float = float(
        soup.find(name="span", class_="a-price-whole").get_text().replace(",", "")
        + soup.find(name="span", class_="a-price-fraction").get_text())
except AttributeError:
    price: float = float(soup.find(name="span", class_="a-price-whole").get_text().replace(",", ""))

try:
    delivery: float = float(
        soup.find(name="div", id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE")
        .get_text().split(" ")[1]
        .split("¥")[1]
        .replace(",", ""))
except (AttributeError, IndexError, ValueError):
    delivery: float = 0.0

product_title: str = soup.find(name="span", id="productTitle").get_text().strip()

msg = MIMEMultipart()
msg['From'] = MY_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = "Amazon Price Alert!"

body: str = f"{product_title} is now ¥{price} with the delivery price ¥{delivery}\n{AMAZON_URL}"
msg.attach(MIMEText(body, "plain", "utf-8"))

ITEM_PRICE = 7000
DELIVERY_PRICE = 4000
if price < ITEM_PRICE and delivery < DELIVERY_PRICE:
    with smtplib.SMTP(SMTP_EMAIL, port=587) as connection:
        connection.starttls()
        connection.login(
            user = MY_EMAIL,
            password = MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = TO_EMAIL,
            msg = msg.as_string())
