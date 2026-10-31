import json
import pandas as pd

data = '''
[
    {"city": "Kochi", "weather": {"temp": 30, "humidity": 80}},
    {"city": "Delhi", "weather": {"temp": 35, "humidity": 60}},
    {"city": "Mumbai", "weather": {"temp": 32, "humidity": 75}}
]
'''

weather = json.loads(data)

df = pd.json_normalize(weather)

df.columns = ["City", "Temperature", "Humidity"]

print("Weather Report:")
print(df.to_string(index=False))

print("\nAverage Temperature:", df["Temperature"].mean())
print("Average Humidity:", df["Humidity"].mean())
