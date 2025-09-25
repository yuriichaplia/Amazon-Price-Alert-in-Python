# Amazon Price Alert APP
A simple Python app that uses BeatifulSoup and SMTPLIB modules to send an email notification if a price of an item and a delivery price are lower than those specified in code.

### To get started you need to create .env file in the root folder with following variables:
MY_EMAIL=your_email <br>
MY_PASSWORD=your_email_password(app password) <br>
TO_EMAIL=email_to_which_the_notification_will_be_sent <br>
AMAZON_URL=url_to_an_item_page_on_amazon<br>
USER_AGENT=user_agent_header (e.g. something like this `Mozilla/5.0 (Windows NT 10.0; Win64; x64)`)<br>
SMTP_EMAIL='smtp.gmail.com'<br>
ITEM_PRICE=desired_item_price <br>
DELIVERY_PRICE=price_that_you_are_willing_to_pay_for_delivery <br>
##### If actual prices of an item and delivery are lower than those provided in .env file then the message will be send

#### Note, however, that Amazon changes its website structure from time to time and depending on what region you are in prices may display on different positions on websites. In this project Amazon for Japan was used, therefore, if you want to use Amazon for another country or region changes in code may be needed. 
