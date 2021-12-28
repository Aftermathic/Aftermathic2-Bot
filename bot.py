import discord
import json
import requests
import random
import asyncio
import os

from webserver import keep_alive

token = os.environ['bot_token']

class Bot(discord.Client):
    #on ready
    async def on_ready(self):
        print(f'\nLogged in as {self.user} (ID: {self.user.id})\n-----------------------------')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='"$help"'))

    #functions
    def get_quote():
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + "\n-" + json_data[0]['a']
        return (quote)

    #commands and stuff
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10!')

            def is_correct(m):
                return m.author == message.author

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long to answer. The number was {answer}.')

            try:
                int(guess.content)
            except ValueError:
                await message.channel.send('That isn\'t a number. Try again later.')
            except:
                await message.channel.send('Something went wrong. Try again later.')
            else:
                if int(guess.content) == answer:
                    await message.channel.send('You got it! Good job!')
                else:
                    await message.channel.send(f'You didn\'t get it, the number was {answer}.\nMaybe you will do better next time.')

        if message.content.startswith('$random_quote'):
            quote_to_send = Bot.get_quote()
            await message.channel.send(quote_to_send)

        if message.content.startswith('$flipcoin'):
            coin_sides = [
                'Heads',
                'Tails'
            ]

            await message.channel.send('You got: ||' + random.choice(coin_sides) + "!||")

        if message.content.startswith('$generate_password'):
            chars = 'abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSUVWXYZ1234567890!@#$%^&()[]{},./;:"|<>?'

            length = random.randint(8, 20)

            generated_password = ''
            for p in range(3):
                for l in range(length):
                    generated_password += random.choice(chars)

            await message.channel.send('Here is your new generated password:\n' + str(generated_password))

        if message.content.startswith('$copytext'):
            copyed_text = message.content.split("$copytext ",1)[1]
            await message.channel.send(str(copyed_text))

        if message.content.startswith('$math'):
            operation = random.randint(1, 3)

            a = random.randint(0, 100)
            b = random.randint(0, 100)

            if operation == 1:
                sum = a + b

                amount_of_time = random.randint(5, 15)

                await message.channel.send('What is ' + str(a) + ' + ' + str(b) + '?\nYou have ' + str(amount_of_time) + ' seconds!')

                try:
                   sum_msg = await self.wait_for('message', timeout=amount_of_time)
                except asyncio.TimeoutError:
                    return await message.channel.send(f'Sorry, you took too long to answer. The answer was ' + str(sum))

                try:
                    int(sum_msg.content)
                except ValueError:
                    await message.channel.send('That\'s not a number. The answer was ' + str(sum))
                except:
                    await message.channel.send('Something went wrong. Sorry.')
                else:
                    if int(sum_msg.content) == sum:
                        await message.channel.send('Good job! You got it correct!')
                    else:
                        await message.channel.send('Sorry you didn\'t get it. The correct answer was ' + str(sum))

            elif operation == 2:
                subtracted = a - b

                amount_of_time = random.randint(5, 15)

                await message.channel.send('What is ' + str(a) + ' - ' + str(b) + '?\nYou have ' + str(amount_of_time) + ' seconds!')

                try:
                   sum_msg = await self.wait_for('message', timeout=amount_of_time)
                except asyncio.TimeoutError:
                    return await message.channel.send(f'Sorry, you took too long to answer. The answer was ' + str(subtracted))

                try:
                    int(sum_msg.content)
                except ValueError:
                    await message.channel.send('That\'s not a number. The answer was ' + str(subtracted))
                except:
                    await message.channel.send('Something went wrong. Sorry.')
                else:
                    if int(sum_msg.content) == subtracted:
                        await message.channel.send('Good job! You got it correct!')
                    else:
                        await message.channel.send('Sorry you didn\'t get it. The correct answer was ' + str(subtracted))

            elif operation == 3:
                product = a * b

                amount_of_time = random.randint(5, 15)

                await message.channel.send('What is ' + str(a) + ' x ' + str(b) + '?\nYou have ' + str(amount_of_time) + ' seconds!')

                try:
                   sum_msg = await self.wait_for('message', timeout=amount_of_time)
                except asyncio.TimeoutError:
                    return await message.channel.send(f'Sorry, you took too long to answer. The answer was ' + str(product))

                try:
                    int(sum_msg.content)
                except ValueError:
                    await message.channel.send('That\'s not a number. The answer was ' + str(product))
                except:
                    await message.channel.send('Something went wrong. Sorry.')
                else:
                    if int(sum_msg.content) == product:
                        await message.channel.send('Good job! You got it correct!')
                    else:
                        await message.channel.send('Sorry you didn\'t get it. The correct answer was ' + str(product))

        if message.content.startswith('$help'):
            await message.channel.send('My prefix is "$"\n\nCommands:\n$guess\n$random_quote\n$flipcoin\n$generate_password\n$math\n$ping\n$copytext (Put text in front of it so it works.)')

        if message.content.startswith('$ping'):
            await message.channel.send('Pong!')

keep_alive()

client = Bot()
client.run(token)
