import discord
import random
import os

client = discord.Client()
semilla = 0

@client.event
async def onready():
    print('Logueado como {0.user}'.format(client))
    semilla = random.seed()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

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

client.run(os.environ.get('TOKEN', None))