from huskylib import HuskyLensLibrary
import json
from yapper import Yapper, PiperSpeaker, PiperVoiceUK, PiperQuality
import python_weather
import asyncio
import os
from openai import OpenAI, AsyncOpenAI
import subprocess

voice = PiperSpeaker(
    voice=PiperVoiceUK.ALBA
)
hl = HuskyLensLibrary("I2C","", address=0x32)
client = AsyncOpenAI(api_key = "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")

async def getweather() -> None:
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    weather = await client.get('Tirana')
    print(weather.temperature)
    logs = ""
    for daily in weather:
      print(daily)
      logs+= str(daily)
      
      for hourly in daily:
        print(f' --> {hourly!r}')
        logs+= str(hourly)
    return logs

async def chat():
    print("starting")
    logs = await getweather()
    response = await client.responses.create(
        model="gpt-3.5-turbo",
        instructions="Talk like a weather presenter. do not use punctuation and write symbols, units and numbers with letters.",
        input= f"Turn the data of the firts day into a short, 1 sentence weather description. DATA: {logs}",
    )

    print(response.output_text)
    voice.say(response.output_text)


def printObjectNicely(obj):
    count=1
    if(type(obj)==list):
        for i in obj:
            print("\t "+ ("BLOCK_" if i.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(i.__dict__))
            count+=1
    else:
        print("\t "+ ("BLOCK_" if obj.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(obj.__dict__))

while True:
    try:
        printObjectNicely(hl.getObjectByID(1))
        voice.say("hello, olseed!")
        break
    except:
        pass

asyncio.run(chat())
subprocess.call(["/home/flatratedijes/lumen/venv/bin/python3", "/home/flatratedijes/lumen/gas.py"])