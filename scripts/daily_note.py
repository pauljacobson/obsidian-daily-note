#!/usr/bin/env python3

import os
import os.path
from datetime import datetime, timedelta

import requests

dw = datetime.today()
tomorrow = "{:%Y-%m-%d}".format(dw + timedelta(days=1))
yesterday = "{:%Y-%m-%d}".format(dw - timedelta(days=1))
title = "{:%A, %d %B %Y}".format(dw)
year = "{:%Y-%m-%d}".format(dw)

PATH = "/path/to/your/directory/"
filename = "{}{}.md".format(PATH, year)


def get_weather(location):
    payload = {"format": "3"}
    weather_request = requests.get("http://wttr.in/" + location, params=payload)
    return weather_request.text.strip()

# Define the city I want weather for from wttr.in
weather = get_weather("Modiin")

# Check if the daily note file already exists
# Create a new note if it doesn't
if os.path.exists(filename):
    pass
else:
    with open(filename, "w") as f:
        f.write(
            f"""---
tags: [dailynote]
cssclass: []
---

Stats: [[!vault stats]]

Today's weather in {weather}

[[{yesterday}]] 👈  👉 [[{tomorrow}]]

# {title}

## Today's notes

```dataview
list
from [[{year}]]
where tag != "dailynote"
```

## Today's thoughts


"""
        )
