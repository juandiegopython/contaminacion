import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$que es la contaminacion'):
        await message.channel.send("la contaminacion es el proceso en el cual salen residuos dañinos para el medio ambiente este se divide en:     luminica      de aire     de  agua         acustica       y de suelo")
    elif message.content.startswith('$que es lo que mas contamina'):
        await message.channel.send("son los motores generando gases o el petroleo ")
    elif message.content.startswith('$tips'):
        await message.channel.send("1.puedes usar botellas de plastico como macetas            2.puedes usar mas la bicicleta evitando generar gases de motor           3.evitar gastar luz o gas mas de lo normal tambien cerrando la llave del agua")
    else:
        await message.channel.send(message.content)

