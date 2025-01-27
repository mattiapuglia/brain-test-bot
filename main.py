from telegram.ext import (Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler)
import logging
from src.handlers.start import start
from src.handlers.quiz import quiz
from src.handlers.risposta import risposta
from src.handlers.categoria import categoria, categorie
from src.handlers.difficolta import difficolta, livelli
from src.handlers.add_commands import add_commands
from src.handlers.livello_selezionato import livello_selezionato
from src.handlers.categoria_selezionata import categoria_selezionata
from src.handlers.info import info


with open("token.txt", "r", encoding="utf-8") as f:
    TOKEN = f.read().strip()


def main() -> None:
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logging.info('Starting bot...')

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

# Handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('difficolta', difficolta))
    dp.add_handler(CommandHandler('categoria', categoria))
    dp.add_handler(CommandHandler('info', info))
    dp.add_handler(CommandHandler('quiz', quiz, pass_job_queue=True))

    dp.add_handler(MessageHandler(Filters.text & Filters.regex(f"({'|'.join(livelli)})"), livello_selezionato))
    dp.add_handler(MessageHandler(Filters.text & Filters.regex(f"({'|'.join(categorie)})"), categoria_selezionata))
    dp.add_handler(CallbackQueryHandler(risposta))

    add_commands(updater)

    updater.start_polling()
    updater.idle()


def init() -> None:
    if __name__=="__main__":
        main()

init()
