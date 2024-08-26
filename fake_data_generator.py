import datetime
import random
import json
from faker import Faker
import pandas as pd  

def generate_random_data():
  fake = Faker()

  data = {
    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "level": random.choice(["INFO", "WARNING", "ERROR"]),
    "query": fake.sentence(),
    "search_type": random.choice(["web", "image", "video"]),
    "user": fake.name()
  }

  return data

def generate_json_file(num_records):
  with open('random_data.json', 'w') as f:
    for _ in range(num_records):
      data = generate_random_data()
      json.dump(data, f)
      f.write('\n')

# Gerar 100 registros
generate_json_file(100)
