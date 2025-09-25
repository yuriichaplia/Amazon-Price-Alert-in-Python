# Amazon Price Alert APP
A simple Python app that uses BeatifulSoup and SMTPLIB modules to send an email notification if a price of an item and a delivery price are lower than those specified in code.

### To get started you need to create .env file in the root folder with following variables:
MY_EMAIL=your_email
MY_PASSWORD=your_email_password(app password)
TO_EMAIL=email_to_which_the_notification_will_be_sent
AMAZON_URL=url_to_an_item_page_on_amazon
USER_AGENT=user_agent_header (e.g. something like this `Mozilla/5.0 (Windows NT 10.0; Win64; x64)`)
SMTP_EMAIL='smtp.gmail.com'
