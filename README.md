# TelegramBot
### This Telegram Bot helps to Encrypt and Decrypt a message sent by an user.
Find it on Telegram as [TestBot](http://t.me/Testbot225_bot)
## Index

* [Introduction](#introduction of testbot)
* [Repl.it](#repl.it)
* [Libraries](#libraries)
* [Keep_Alive](#keep_alive)
* [UptimeRobot](#uptimerobot)
* [Conclusion](#conclusion)

## Introduction of TestBot
* This Bot is designed to Encrypt and Decrypt the messages
* Encryption and Decryption process is done by Xor'ing a message and a key.
* Key is a integer value which is randomly ganerated from random function.
* Seed saves(remembers) the current value of randomly generated key in the process.
* During Encryption, each character of Input message is converted to its ascii value and xor'ed with key.
* appending every xor'ed word is appended and combined to one single word. Then it is coverted to hexadecimal for easy decryption. 
* So, Bot sends the encrypted message in hexadecimal format.
* During Decryption, hexadecimal string is coverted to normol string and then xor'ing each character of encrypted message and key gives decrypted message.

## Repl.it
* Repl.it is a free online IDE(integrated development environment) that allows users to write their own programs and code in any language.
* sign up to Repl.it [Here](https://replit.com)
* In Repl.it, we can run our code and at a same time can create a server which runs our code forever.

## Libraries
* Import os - The OS module in Python provides functions for creating and removing a directory(folder), fetchng its contents, changing and identifying the current directory etc..
* Import telebot - Telebot library is used to interact the code with our telegram bot. Refer [TelebotAPI](https://pypi.org/project/pyTelegramBotAPI/) to know how to create your own telegram bot and operate with it.
* Import Random - Random library is used to generate any random numbers. In this code we use random function to generate a random key for each character.
* Import keep_alive - This Library is used to create the server.

## keep_alive 
* flask is used to make the server. Refer [Flask](https://github.com/pallets/flask/) Here.
* thread allows us to do multiple things at once. Here it allows the server to run continously and runs the python code at a same time.
* So, keep_alive runs both server and main.py file at a same time

## main.py
* In main.py file we have a function called input_message for Encryption, and a function called output_message for Decryption.
* API_KEY is a secret key of our telegram bot.
* Message Handlers are used to take response from Bot for certain commands.
* It detects the message sent by user is a text or command and responds accordingly. Check the code for details

## Uptimerobot
* The server in repl.it runs the code about an hour and then the server goes down.
* UptimeRobot is a free service which basically pings our site every 5 minutes.
* During the pinging, it makes repl think that our server is getting some activity on it, so it doesn't shut the server down.
* Register for UptimeRobot [Here](https://uptimerobot.com/)

## Conclusion
