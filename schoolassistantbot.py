import discord
import random
import datetime
import requests
from discord.ext import commands

pertama = 11 #Senin Pertama Tanggal Berapa
pelajaran = '.p' , '.pelajaran'
now = datetime.datetime.now()

#List Pantun
pantunlist = ["Waktu daftar hari terakhir, waktu terasa banyak terbuang. Kamu nggak perlu khawatir, cintaku hanya untukmu seorang.", "Jalanan lagi lancar,itu adalah sebuah berkah.Aku bukan nyari pacar,tapi nyari yang mau diajak nikah","Bawa paku dipukul batu,dicampur jamu di atas tungku.Cintaku cukuplah satu,untuk kamu sepanjang waktu."]
pantunlist.insert (1, "Dua katak pergi bertemu, Duduk berdampingan diatas baja. Masih kupandang wajah cantikmu, Walau dari kejauhan saja")

#DISCORD REUQIREMENTS (DO NOT CHANGE OR DELETE)
TOKEN = 'token example here'

client = discord.Client()

@client.event
async def on_message(message):
    #Making The Bot Decline it Self
    if message.author == client.user:
        return

    if message.content.startswith('.hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    if message.content.startswith('.help'):
        msg = 'List of Command we Have {0.author.mention} , .hello , .random , .p , .kaldik , .jadwal'.format(message)
        await message.channel.send(msg)
    if message.content.startswith('.tell'):
        msg = message.content[5:]
        await message.channel.send(msg)
    elif message.content.startswith('.bot'):
        await message.channel.send("HENLO")
    elif message.content.startswith('.pantun'):
        msg = random.choice(pantunlist).format(message) #send pantun
        await message.channel.send(msg)
    elif message.content.startswith('.tolol'):
        msg = 'EH KOK NGAMOK, ELU TOLOL AJG {0.author.mention}'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith('.jevontolol'):
        msg = 'Setuju ngab, {0.author.mention} . Memang tolol si Jevon'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith('.random'): #random num gen 1 digit only
        number = []
        msg1 = message.content [7:9]
        number.append(msg1)
        msg2 = message.content [9:12]
        msg1 = msg1.replace(' ','')
        msg2 = msg2.replace(' ','')
        msg1 = int(msg1)
        msg2 = int(msg2)
        while msg1 != msg2 :
            msg1 = msg1 + 1
            number.append(msg1)
        msg = random.choice(number)
        await message.channel.send(msg)
    elif message.content.startswith('.kaldik'):
        msg = 'OTW BROO {0.author.mention}. Sending nih!!'.format(message)
        await message.channel.send(msg)
        await message.channel.send(file=discord.File(r"/home/discordbot/foto/kaldik.png"))
    elif message.content.startswith('.jadwal'):
        msg = 'Untuk jadwal Lengkap bisa di #school-info {0.author.mention}'.format(message)
        await message.channel.send(msg)
        if now.day == pertama or now.day == pertama + 1 :
            await message.channel.send(file=discord.File(r"/home/discordbot/foto/1.png"))
        if now.day == pertama + 2 or now.day == pertama + 3 :
            await message.channel.send(file=discord.File(r"/home/discordbot/foto/2.png"))
        if now.day == pertama + 4 :
            await message.channel.send(file=discord.File(r"/home/discordbot/foto/3.png"))
        else :
            msg = 'Hari Libur Bro {0.author.mention}'.format(message)
            await message.channel.send(msg)
    elif message.content.startswith('.anc'):
        await message.channel.send(file=discord.File(r"/home/discordbot/ancbot/topi.png"))
    elif message.content.startswith(pelajaran):
        msg = 'Karena Bentuk jadwal yang baru, .p mungkin sudah tidak dapat beroperasi lagi.'.format(message)
        await message.channel.send(msg)
#DISCORD REUQIREMENTS (DO NOT CHANGE OR DELETE)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Welcome to Second Semester"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print (datetime.datetime.now())
client.run(TOKEN)
