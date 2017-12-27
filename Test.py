import telebot
import Recognition.TextFromImageRecognition

token = ''
tokenRead = open('token.txt', 'r')
for line in tokenRead:
    token = token + line
print(token)

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = "send me png file with text"
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['start'])
def handle_text(message):
    answer = "Hello! You are welcome!"
    bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'D:\GitProject\TextRecognitionBot\\UserFiles\\' + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        answer = Recognition.TextFromImageRecognition.textFromImageRecognition(src)
        bot.reply_to(message, "Ваш текст: " + answer)

    except Exception as e:
        bot.reply_to(message, e)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:

        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'D:\GitProject\TextRecognitionBot\\' + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        answer = Recognition.TextFromImageRecognition.textFromImageRecognition(src)
        bot.reply_to(message, "Ваш текст: " + answer)
    except Exception as e:
        bot.reply_to(message, e)


bot.polling(none_stop=True, interval=0)