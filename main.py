import discord, zad_b, wdi, re

tags = []

client = discord.Client()

def dajBB(msg):
    temp = msg.split("```")
    strin = ""
    bb = []
    for i in range(0, len(temp), 2):
        ttemp = temp[i].split("**")
        for j in range(1, len(ttemp), 2):
            bb.append(ttemp[j].strip())
        strin += temp[i] + " "
    return [strin, bb]

@client.event
async def on_ready():
    print('>>> Connected as: ' + str(client.user))
    with open("msgtags.txt") as f:
        temp = f.read().splitlines()
        for j in range(0, len(temp), 2):
            tags.append([temp[j],temp[j+1]])

@client.event
async def on_reaction_add(reaction, user):
    if(reaction.message.author == client.user):
        return

    chan = reaction.message.channel
    if(chan.name == "p1" and reaction.emoji == "✅"):
        mesg, bb = dajBB(reaction.message.content)
        idmsg = str(reaction.message.id)
        with open("messages/msg" + idmsg + ".txt", "w") as f:
            f.write(mesg)
        with open("msgtags.txt", "a") as f:
            for i in bb:
                f.write(i.lower() + "\n" + idmsg + "\n")
                tags.append([i.lower(), idmsg])

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.split()
    if(message.channel.name == "p1"):
        for j in tags:
            if(re.search(r"\s+("+j[0]+r")\s*", message.content.lower())):
                with open("messages/msg" + j[1] + ".txt") as f:
                    await message.channel.send("**Potencjalna odpowiedz:**\n" + f.read())
    elif(message.channel.name == "bot-spam"):
        if(msg[0] == "!baca"):
            if(msg[1] == "b" or msg[1] == "B"):
                moreInfo = False
                if("--m" in msg):
                    moreInfo = True
                if(msg[2] == "def"):
                    for ind, i in enumerate(zad_b.B_TESTS):
                        if(ind != 0):
                            await message.channel.send("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                        await message.channel.send("**Running test: **#" + str(ind+1) + "\n")
                        await message.channel.send(zad_b.main(' '.join(i.split()).split(), moreInfo))
                else:
                    if(moreInfo):
                        await message.channel.send(zad_b.main(' '.join(msg[3:]).split(), moreInfo))
                    else:
                        await message.channel.send(zad_b.main(' '.join(msg[2:]).split(), moreInfo))
        elif(msg[0] == "!wdi"):
            if(msg[1] == "przelicz"):
                if(msg[2] != "" and msg[3] != "" and msg[4] != ""):
                    await message.channel.send(wdi.przelicz(msg[2].upper(), int(msg[3]), int(msg[4])))

with open("discordkey.txt") as f:
    client.run(f.read())