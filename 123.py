import discord
import openpyxl
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!명령어")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!명령어"):
        await message.channel.send(" 각 명령어는 ''빼고 써라 괄호도 쓰지마세요\n'!생년월일' (이름) (xxxx년xx월xx일)생일입력하세요\n'!생일' (이름) 생일을 입력한 사람만 뜬다 자꾸 노무현 쳐보지마세요\n'!사다리타기' A  B  C  D/1  2  3  4 결과가 바로 나와요!\n'!주사위' (주사위)/(리롤) 둘이 위치 바껴도 결과 그대로입나다\n'!선택' (1) (2) (3) 고르기 힘들때 쓰세요")


    if message.content.startswith("!생년월일"):
        file = openpyxl.load_workbook("생일.xlsx")
        sheet = file.active
        learn = message.content.split(" ")
        for i in range(1, 100):
            if sheet["A" + str(i)].value == "-" or sheet["A" + str(i)].value == learn[1]:
                sheet["A" + str(i)].value = learn[1]
                sheet["B" + str(i)].value = learn[2]
                break
        file.save("생일.xlsx")


    if message.content.startswith("!생일"):
        file = openpyxl.load_workbook("생일.xlsx")
        sheet = file.active
        memory = message.content.split(" ")
        for i in range(1, 100):
            if sheet["A" + str(i)].value == memory[1]:
                await message.channel.send(sheet["b" + str(i)].value)
                break



    if message.content.startswith("!사다리타기"):
        team = message.content[7:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(person[i] + "==>" + teamname[i])


    if message.content.startswith("!주사위"):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(1, int(rolld[0])+1):
            dice = dice + random.randint(1, int(rolld[1]))
        await message.channel.send(str(dice))

    if message.content.startswith("!선택"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await  message.channel.send(choiceresult)




access_token = os.environ["Bot_Token"]


client.run(access_token)


