import os
from keep_alive import keep_alive
import telebot
from random import randint, seed

def input_message(input_text):
    en_msg = ""
    hexa_msg = "enc_msg = "
    seed(1000)
    for i in input_text:
        key= randint(1,250)
        asc_msg= ord(i)
        xor1= asc_msg ^ key
        msg1 =chr(xor1)
        en_msg += msg1
    for j in en_msg:
        hexa = hex(ord(j))
        hexa_msg += hexa[2:].zfill(2)
    return hexa_msg

def output_message(output_text):
    de_msg = ""
    outString = ""
    seed(1000)
    con_text = output_text[10:]
    if len(con_text)%2 != 0:
        return "please enter correct encrypted message"
    else:
        hexa = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(0, len(con_text), 2):
            subStr = con_text[i] + con_text[i+1]
            if con_text[i] in hexa and con_text[i+1] in hexa:
                x = chr(int(subStr, 16))
                outString += x
            else:
                return "please enter correct encrypted message"
        for j in outString:
            key= randint(1,250)
            asc_msg= ord(j)
            xor1= asc_msg ^ key
            msg1 =chr(xor1)
            de_msg += msg1
        return de_msg

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

keep_alive()

@bot.message_handler(commands = ['start', 'greet'])
def start(message):
  bot.send_message(message.chat.id, "Hello there! Welcome to @Testbot225_bot.This bot can encrypt and decrypt your texts. Type a message to encrypt it. send the encrypted message to decrypt and get original format of it")

@bot.message_handler(commands = ['help'])
def help(message):
  bot.reply_to(message, "1) When you decrypt the message sent by any other person, make sure randint and seed are same as yours (250,1000).\n2) Before Decryption, check whether 'enc_msg = ' is present infront of encrypted message")

@bot.message_handler(func=lambda m:True)
def handle(message):
  if message.text[0:10] == 'enc_msg = ':
    bot.reply_to(message, output_message(message.text))
  else:
    bot.reply_to(message, input_message(message.text))
    

@bot.message_handler(content_types=['document','audio','sticker','photo'])
def excep_handle(message):
  bot.reply_to(message, "Sorry about that, This bot currently operating with only texts. Please retry with text.")
   
bot.polling()