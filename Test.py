import telebot
import Recognition.TextFromImageRecognition

token = ''
tokenRead = open('token.txt', 'r')  # copy the token from the file
for line in tokenRead:
    token = token + line

bot = telebot.TeleBot(token)  # activate the bot
print('bot is active')


@bot.message_handler(commands=['help'])  # answer to help command
def handle_text(message):
    answer = "send me image file with text"
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['start'])  # answer to start command
def handle_text(message):
    answer = "Hello! You are welcome!"
    bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['document'])  # response in the case of an image of a document
def handle_docs_photo(message):
    try:

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'D:\GitProject\TextRecognitionBot\\UserFiles\\' + message.document.file_name  # download file
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        answer = Recognition.TextFromImageRecognition.textFromImageRecognition(src)
        bot.reply_to(message, "Your Text: " + answer)

    except Exception as e:
        bot.reply_to(message, e)


@bot.message_handler(content_types=['photo'])  # response in the case of an image of a photo
def handle_photo(message):
    try:

        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'D:\GitProject\TextRecognitionBot\\' + file_info.file_path  # download file
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        answer = Recognition.TextFromImageRecognition.textFromImageRecognition(src)
        bot.reply_to(message, "Your Text: " + answer)
    except Exception as e:
        bot.reply_to(message, e)


bot.polling(none_stop=True, interval=0)
