
from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes

TOKEN:Final="6563356916:AAGS-2dXsPQN_1Yknc6BUx4vhCLDkhMe15Y"
BOT_USERNAME: Final ="@Open_Budjet_01bot"

async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! Iam a open budjet!")

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a banana! Please type sonthing so I con respond!")


async def custom_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")







