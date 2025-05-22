!pip install supabase python-dotenv
from google.colab import drive
drive.mount ("/content/drive")
import os
from dotenv import load_dotenv
load_dotenv ("/content/drive/MyDrive/ProjetoCanil/.env")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
print("SUPABASE_URL: ", SUPABASE_URL)


from fastapi import FastAPI
import os
from supabase import create_client, Client

app = FastAPI()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "Supabase conectado com sucesso!"}

