#imports
import os
from dotenv import load_dotenv

#dotenv
load_dotenv()

Users: set[int] = {
    int(user_id.strip())
    for user_id in os.getenv("USERS", "").split(",")
    if user_id.strip().isdigit()

}