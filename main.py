from fastapi import FastAPI
import os
from supabase import create_client, Client

app = FastAPI()

# Pegando variáveis de ambiente definidas no painel do Render
SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "Supabase conectado com sucesso!"}
