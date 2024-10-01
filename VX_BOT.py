import discord
from discord.ext import commands
from discord import Intents
import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
base_url = "https://globalstats.vx.nexon.com"
usn_path = '/api/Search/GetSearchRead/'
profile_path = '/api/Profile/GetGameProfile/'
record_path = '/api/Record/GetSeasonRecord/'

bot = commands.Bot(command_prefix = '/', intents = discord.Intents.all())
 

@bot.event
async def on_ready():
    print('TAKE BOT RUNNING')


@bot.command()
async def 전적(message, *user_list) :
    for user in user_list :
        # usn
        usn_url = base_url + usn_path + user
        usn_response = requests.post(usn_url, headers = headers)
        try :
            user_usn = usn_response.json()['nickname_list'][0]['usn']
        except :
            embed = discord.Embed(title = user + ' 닉네임을 확인해주세요.', color = 0x60f8c5)
            await message.channel.send(embed = embed)
            continue

        # profile
        profile_url = base_url + profile_path + user_usn
        profile_response = requests.post(profile_url, headers = headers)

        # record
        record_url = base_url + record_path + '202310/' + user_usn + '/1/1'
        record_response = requests.post(record_url, headers = headers)

        #total
        total = {
            'adr' : profile_response.json()['rankInfo']['solo_rank_info']['adr'],
            'clan_name' : profile_response.json()['rankInfo']['solo_rank_info']['clan_name'],
            'headshot_rate' : record_response.json()['cSoloRecordInfo']['headshot_rate'],
            'kd' : profile_response.json()['rankInfo']['solo_rank_info']['kdr'],
            'match_cnt' : profile_response.json()['rankInfo']['solo_rank_info']['match_cnt'],
            'nick_name' : profile_response.json()['rankInfo']['solo_rank_info']['nick_name'],
            'rank' : profile_response.json()['rankInfo']['solo_rank'],
            'ranking_point' : profile_response.json()['rankInfo']['solo_rank_info']['ranking_point'],
            'win_rate' : profile_response.json()['rankInfo']['solo_rank_info']['win_rate'],
        }

        # error check code
        # await message.channel.send(profile_response.status_code)

        # output
        embed = discord.Embed(color = 0x60f8c5)
        if total['clan_name'] :
            embed.set_author(name = total['nick_name'] + '   (' + total['clan_name'] + ')', url = "https://globalstats.vx.nexon.com/ko/" + user_usn + "/")
        else :
            embed.set_author(name = total['nick_name'], url = "https://globalstats.vx.nexon.com/ko/" + user_usn + "/")
        if total['ranking_point'] >= 8000 and total['ranking_point'] >= 100 :
            embed.set_thumbnail(url="https://globalvx.dn.nexoncdn.co.kr/Web/barracks/page/grade2_160_expert.png")
        elif total['ranking_point'] >= 8000 :
            embed.set_thumbnail(url="https://globalvx.dn.nexoncdn.co.kr/Web/barracks/page/grade2_160_elite.png")
        elif total['ranking_point'] >= 5500 :
            embed.set_thumbnail(url="https://globalvx.dn.nexoncdn.co.kr/Web/barracks/page/grade2_160_diamond.png")
        elif total['ranking_point'] >= 4000 :
            embed.set_thumbnail(url="https://globalvx.dn.nexoncdn.co.kr/Web/barracks/page/grade2_160_platinum.png")
        elif total['ranking_point'] >= 2000 :
            embed.set_thumbnail(url="https://globalvx.dn.nexoncdn.co.kr/Web/barracks/page/grade2_160_gold.png")
        elif total['ranking_point'] >= 1000 :
            embed.set_thumbnail(url="https://globalvx.dn.nexoncdn.co.kr/Web/barracks/page/grade2_160_silver.png")
        elif total['ranking_point'] >= 0 :
            embed.set_thumbnail(url="https://globalvx.dn.nexoncdn.co.kr/Web/barracks/page/grade2_160_bronze.png")
        else :
            embed.set_thumbnail(url="https://globalvx.dn.nexoncdn.co.kr/Web/barracks/page/grade_vx_symbol.png")
        embed.add_field(name = "RANK", value = total['rank'], inline = True)
        embed.add_field(name = "K/D", value = total['kd'], inline = True)
        embed.add_field(name = "ADR", value = total['adr'], inline = True)
        embed.add_field(name = "HEADSHOT_RATE", value = str(total['headshot_rate']) + '%', inline = True)
        embed.add_field(name = "MATCH", value = total['match_cnt'], inline = True)
        embed.add_field(name = "WIN_RATE", value = str(total['win_rate']) + '%', inline = True)
        await message.channel.send(embed = embed)

# token
bot.run('')
