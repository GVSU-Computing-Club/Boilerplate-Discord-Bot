import discord
from sys import exit

class Bot(discord.Client):
    def __init__(self):
        discord.Client.__init__(self)

    @staticmethod
    def getToken():
        try:
            f = open('token.txt', 'r')
            token = f.read().strip()
            f.close()
        except IOError:
            print('A file named token.txt could not be found in this directory')
            exit(1)
        return token

    def fixHour(self, hour):
        '''
        the api gets utc time this converts it to est time and changes it from 24 hour time to 12 hour
        '''
        if(hour >= 4):
            hour -= 4
        else:
            hour += 8
        return hour % 12

    async def on_ready(self):
        print('Connected as:', self.user)

    async def on_typing(self, channel, user, when):
        print('User: [{}] typing at time: {}:{}:{}'.format(user.display_name, self.fixHour(when.hour), when.minute, when.second))

    ########################
    #challenges            #
    ########################

    # 10 point challenges:

    #example: 
    #!add 4 5
    #output: 9

    def add(self, message):
        pass

    def subtract(self, message):
        pass

    def multiply(self, message):
        pass

    def divide(self, message):
        pass

    # 20 point challenges:

    #reverse incoming string message and print it back to the user
    #example:
    #!reverse hello world
    #output:
    #dlrow olleh
    def reverse(self, message, channel):
        pass

    # 50 point challenges:

    # list all users who are online currently
    def list_online(self, channel):
        pass

    # 100 point challenges

    #rock, paper, scissors
    #When you !rps the bot will countdown from 5 and randomly choose rock, paper, or scissors
    #if the user responds
    def rps(self, message, channel):
        pass

    #get the weather for a specific location
    def weather(self, message, channel):
        pass

    #get the time in a certain location of the world and print to the user
    def time_in(self, message, channel):
        pass

    # 300 points
    # count individual words of any message and store them into a file as a dictionary
    # hint use json, and the json.dump to store it as a dictionary in a file
    def word_count(self, message):
        pass

    # part 2 of previous challenges:
    # 200 points extra
    # using !topwords get the top 5 most commonly used words and their count
    # hint: use json.load to read the information from the file as a dictionary
    def top_words(self, message, channel):
        pass

    async def on_message(self, message):
        if(message.content.startswith('hello')):
            await self.send_message(message.channel, 'world')

