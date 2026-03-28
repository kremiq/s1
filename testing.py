import os
from dotenv import load_dotenv

load_dotenv()

# If "DB_PASSWORD" isn't set, Python will immediately throw a KeyError and stop
db_pass = os.environ["DB_PASSWORD"]

print("Password loaded, connecting to database...")