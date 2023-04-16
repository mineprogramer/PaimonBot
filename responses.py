import random
import discord

def handle_response(user_message, message) -> str:

    p_message = user_message
    rock_s_p = ['rock', 'scissors', 'paper']
    help = """
Commands
----------------------------------------------
$help      -> for this beautiful index
$hello     -> response to your greeting
$roll      -> gives you a random number from 1 to 6
$greet     -> greets you by your discord username
$greetings -> greets you by your discord nickname

$echo "your text here" -> repeats what you sent
$say "your text here"  -> deletes and repeats what you sent
"""

    if p_message == 'help' :
        return '```arm' + help + '```'

    if p_message == 'hello' :
        return 'Hey there!'
    
    if p_message == 'roll' :
        return 'You rolled a ' + str(random.randint(1,6)) + '!'
    
    if p_message == 'greet' :
        return "Greetings " + str(message.author)

    if p_message == 'greetings' :
        return "Greetings " + str(message.author.nick)
    
    if p_message.startswith('echo') :
        return str(message.content[5:])
    
    if p_message.startswith('rock') or p_message.startswith('scissors') or p_message.startswith('paper') :
        botNum = int(random.randint(0,2))
        bot = rock_s_p[botNum]

        if ((p_message.startswith(rock_s_p[0]) and bot == 'rock') or 
            (p_message.startswith(rock_s_p[1]) and bot == 'scissors') or
            (p_message.startswith(rock_s_p[2]) and bot == 'paper')):
            return "I chose " + str(bot) + "!\nIt's a Tie!"
        elif ((p_message.startswith(rock_s_p[0]) and bot == 'scissors') or
            (p_message.startswith(rock_s_p[1]) and bot == 'paper') or
            (p_message.startswith(rock_s_p[2]) and bot == 'rock')) :
            return "I chose " + str(bot) + "!\nYou Win!"
        elif ((p_message.startswith(rock_s_p[0]) and bot == 'paper') or
            (p_message.startswith(rock_s_p[1]) and bot == 'rock') or
            (p_message.startswith(rock_s_p[2]) and bot == 'scissors')) :
            return "I chose " + str(bot) + "!\nYay I Win!"
        
    if p_message.startswith('roll') :
        try:
            p_message = p_message[5:]
            counter = 0
            number = ''
            for i in p_message :
                if p_message[counter].isnumeric() :
                    number = str(number) + str(p_message[counter])
                    counter += 1
                else:
                    break
            return 'You rolled a ' + str(random.randint(1,int(number))) + '!'
        except Exception as e:
            return e
