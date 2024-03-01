import Env
Env.set_env()
from DBFunctions import get_all_countries, get_specific_country, update_specfic_country

get_all_countries()
get_specific_country(2)

update_specfic_country(2, {"name": "Netherlands"})

get_specific_country(2)
