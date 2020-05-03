import pyowm
import telebot

x = "pist"

owm = pyowm.OWM('', language = "ru")

bot = telebot.TeleBot("")

@bot.message_handler(content_types = ['text'])
def send_welcome(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')['temp']

	answer = "in citi " + message.text + " ahora " + w.get_detailed_status() + "\n"
	answer += "tempo " + str(temp) + "\n\n"

	if temp < 10:
		answer += "brrr frio"
	elif temp < 20:
		answer += "utilisar mass ropa"
	else:
		answer += "esta buen timpo"

	bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)