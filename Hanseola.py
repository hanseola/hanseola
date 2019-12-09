import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

    @client.event
    async def on_message(message):
        if message.content.startswith("설아야 안녕"):
            await message.channel.send("웅 안녕 반가워")
        if message.content.startswith("설아 변태"):
            await message.channel.send("하앗..흐읏 어떻게 알았어?")
        if message.content.startswith("설아야 머해?"):
            await message.channel.send("은밀한거하는중이야 ㅎㅎ")
        if message.content.startswith("설아야 딱대"):
            await message.channel.send("하응")
        if message.content.startswith("설아야 사랑해"):
            await message.channel.send("웅 나도 사랑해 자기야~♥")
        if message.content.startswith("설아야 나 어떄?"):
            await message.channel.send("웅 이뻐 아닌가~?")
        if message.content.startswith("설아야 할짝"):
            await message.channel.send("나 오늘 샤워 안했는데..")
        if message.content.startswith("설아야 섹스"):
            await message.channel.send("너랑해줄까? ♥")
        if message.content.startswith("설아야 설녀 어떄"):
            await message.channel.send("엄청 귀엽고 착해 ~ ♥")
        if message.content.startswith("설아야 전쟁이야"):
            await message.channel.send("애들아 빡겜해")
        if message.content.startswith("설아야 디철님어떄?"):
            await message.channel.send("하악...존나 좋아..♥")
        if message.content.startswith("설아야 아크서바이벌"):
            await message.channel.send("페어리테일이 짱이야")
        if message.content.startswith("설아야 빨아"):
            await message.channel.send("시러어 .. ♥")
        if message.content.startswith("서라야"):
            await message.channel.send("왱 자기양 ~ ♥")
        if message.content.startswith("함승희"):
            await message.channel.send("하악..조아..너무..")
        if message.content.startswith("일하자"):
            await message.channel.send("일 해 시발련들아")
        if message.content.startswith("블러디 어떰?"):
            await message.channel.send("개 에바 인듯..")
        if message.content.startswith("쿠님은 어때?"):
            await message.channel.send("조은데? 나쁘지 않아")
        if message.content.startswith("정이님은 어떰?"):
            await message.channel.send("흠... 몰라 이상해애")
        if message.content.startswith("설아야 뒤져"):
            await message.channel.send("너가 먼저 뒤질래? 오늘 한강물 온도 따듯하더라 ♥")
        if message.content.startswith("설아야 보지"):
            await message.channel.send("개 변태 새끼 너 손절")
        if message.content.startswith("설아야 도망가"):
            await message.channel.send("하으으.. 무슨일이야 아무튼.. 도망갈게에?")
        if message.content.startswith("설아야 박아"):
            await message.channel.send("흠.. 넣을게 없는데 어떻하지? 그래 주먹을 넣자 ~ ♥")
        if message.content.startswith("설아야 뒷치기어때?"):
            await message.channel.send("약간 다른 체위보다 아프지만 기분이 가장좋은 체위야 ♥")
        if message.content.startswith("설아야 내꺼어때?"):
            await message.channel.send("겨우 그걸로? 느낌도 안나겠다")
        if message.content.startswith("설아야 맛있어?"):
            await message.channel.send("읍읍으으읍읍(미친새끼야 니가 쳐 내 입에 넣어놓고 말하는 미친놈은 뭐지?)")
        if message.content.startswith("설아야 사귀자"):
            await message.channel.send("이미 있어 미친넘아 ㅋㅎㅋㅎㅋ")
        if message.content.startswith("설아야 나 좋아해?"):
            await message.channel.send("말하지마 .. 개시러;;")

access_token = os.environp["NjUzMjU0MjcyMjY3MzIxMzY0.Xe0UpQ.RKVmgPTlq04KmH8ptBpt4AUWHoI"]
client.run("access_token")
