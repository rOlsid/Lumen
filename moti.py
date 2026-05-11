import python_weather
import asyncio
import os
from openai import OpenAI, AsyncOpenAI

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
    logs = await getweather()
    response = await client.responses.create(
        model="gpt-4.1",
        instructions="Talk like a weather presenter. do not use punctuation and write symbols, units and numbers with letters.",
        input= f"Turn the data of the firts day into a short, 1 sentence weather description. DATA: {logs}",
    )

    print(response.output_text)



asyncio.run(chat())
