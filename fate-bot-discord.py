import discord
import random

client = discord.Client()
semilla = 0
frasesSergio = ['Vergacion!', 'Sale vicio?', 'He visto mejores', 'Ese juego es una mierda']
frasesAlex = ['Manibular', 'Me voy a calentar las manos', 'Anda mal Internet, voy a reiniciar el router (y no vuelvo mas)', 'Tecnicamente no llegue tarde, sino que ustedes viven en otro huso horario', 'Me hago un te, ya vuelvo']

@client.event
async def onready():
    print('Logueado como {0.user}'.format(client))
    semilla = random.seed()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hola'):
        await message.channel.send('Hola!')
    if message.content.startswith('!sergio'):
        await message.channel.send(frasesSergio[random.randint(0, len(frasesSergio) - 1)])
    if message.content.startswith('!alex'):
        await message.channel.send(frasesAlex[random.randint(0, len(frasesAlex) - 1)])

    if message.content.startswith('!fate'):
        salidaDebug = ""
        modificador = 0
        if message.content.startswith('!fate +') or message.content.startswith('!fate -'):
            salidaDebug = salidaDebug + "| Se encontro un modificador "
            modTexto = message.content
            modTexto = modTexto.replace('!fate ', '')
            suma = False
            if modTexto.find('+') != -1:
                suma = True
            modTexto = modTexto.replace('+', '')
            modTexto = modTexto.replace('-', '')
            if modTexto.isdigit():
                salidaDebug = salidaDebug + "| Modificador es numerico "
                modificador = int(modTexto)
                if suma == False:
                    modificador = modificador * -1
                    salidaDebug = salidaDebug + "| Modificador es negativo "
        #dados = [random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1)]
        dados = [round(random.randint(-10000, 10000) / 10000), round(random.randint(-10000, 10000) / 10000), round(random.randint(-10000, 10000) / 10000), round(random.randint(-10000, 10000) / 10000)]
        resultadoDadosTexto = ""
        for num in dados:
            if num == -1:
                resultadoDadosTexto = resultadoDadosTexto + " -"
            elif num == 0:
                resultadoDadosTexto = resultadoDadosTexto + " 0"
            else:
                resultadoDadosTexto = resultadoDadosTexto + " +"
        resultadoDadosNumero = sum(dados)
        #await message.channel.send(message.author.mention + " | " + resultadoDadosTexto + " | Resultado: " + str(resultadoDadosNumero + modificador) + "          " + salidaDebug + "       | modTexto: " + modTexto)
        await message.channel.send(message.author.mention + " | " + resultadoDadosTexto + " | Resultado: " + str(resultadoDadosNumero + modificador))

client.run(process.env.TOKEN)