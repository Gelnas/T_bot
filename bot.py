import telebot, signal, time
import citation
import equation

#url = ''

bot = telebot.TeleBot('980859496:AAFX3yHkiCsqWFX5aHzumavj9mkpNBgqnSA')

start_message = '''Добро пожаловать. Я математический бот. Я могу решать алгебраические уравнения 1 - 3 степени, радовать тебя математическими цитатами и помогать тебе совершенствоваться в решении уравнений\n\n Основные команды: \n
/start - начальное меню \n /solveEquation -  решить уравнение \n /citation - получить цитату \n /test - пройти тест'''
solve_equation_message = 'Выберите тип уравнения, которое необходимо решить'


@bot.message_handler(commands=['citation'])
def cit(message):
   bot.send_message(message.from_user.id, citation.get_citation())

@bot.message_handler(commands=['start'])
def st(message):
   bot.send_message(message.from_user.id, start_message)

@bot.message_handler(commands=['solveEquation'])
def sol(message):
    bot.send_message(message.from_user.id, 'Введите коэффициенты через пробел')
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        coeff = message.text.split(' ')
        if len(coeff) == 2:
            bot.send_message(message.from_user.id, 'Решение уравнения {0}x+{1}=0'.format(int(coeff[0]), int(coeff[1])))
            bot.send_message(message.from_user.id, equation.linear_equation(int(coeff[0]), int(coeff[1])))
        elif len(coeff) == 3:
            #bot.send_message(message.from_user.id, 'Решение уравнения {0}x+{1}=0'.format(int(coeff[0]),int(coeff[1])))
            bot.send_message(message.from_user.id, equation.quadratic_equation(int(coeff[0]), int(coeff[1]), int(coeff[2])))
        elif len(coeff) == 3:
            #bot.send_message(message.from_user.id, 'Решение уравнения {0}x+{1}=0'.format(int(coeff[0]),int(coeff[1])))
            bot.send_message(message.from_user.id, equation.cubic_equation(int(coeff[0]), int(coeff[1]), int(coeff[2]), int(coeff[3])))
        else:
            bot.send_message(message.from_user.id, 'К сожалению, я не могу решить уравнения выше третей степени((')
            
            
    
    
'''keyboard = telebot.types.InlineKeyboardMarkup() 
        button_linear = telebot.types.InlineKeyboardButton(text='Линейное', callback_data='linear')
        keyboard.add(button_linear)
        button_quadratic = telebot.types.InlineKeyboardButton(text='Квадратное', callback_data='quadratic')
        keyboard.add(button_quadratic)
        button_cubic = telebot.types.InlineKeyboardButton(text='Кубическое', callback_data='cubic')
        keyboard.add(button_cubic)
        bot.send_message(message.from_user.id, solve_equation_message, reply_markup = keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'linear':
        bot.send_message(call.message.chat.id, equation_message)
        print('Nu')
        time.sleep(10)
        #signal.pause()
        
        

        n = get_message()
        print('Nu2')
        print(n)
        coeff = n.split(' ')
        print(coeff)
        bot.send_message(call.message.chat.id, equation.linear_equation(coeff[0],coeff[1]))
    elif call.data == 'quadratic':
        bot.send_message(call.message.chat.id, equation_message)
    elif call.data == 'cubic':
        bot.send_message(call.message.chat.id, equation_message)'''
    
'''@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        
        
        
        
    elif message.text == "/citation":
       bot.send_message(message.from_user.id, citation.get_citation())


 @bot.message_handler(content_types=['text'])
        def work(message):
            n = message.text
            print(n)
            return n        
       '''


bot.polling(none_stop=True, interval=0)
