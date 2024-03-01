import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Function to get all countries from the database
def get_all_countries():
    response = supabase.table('countries').select('*', count='exact').execute()
    print(response)

# Function to get a specific country from the database
def get_specific_country(id: int):
    response = supabase.table('countries').select("*", count='exact').eq('id', id).execute()
    print(response)

# Function update a specific country from the database
def update_specfic_country(id: int, data: dict):
    response = supabase.table('countries').update(data).eq('id', id).execute()
    print(response)