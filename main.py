"""Main file for Python app."""

import os
import sys
import toml
import arrow
from dotenv import load_dotenv
from pyutilities_thedarknine import display, logs

# Load env variables
try:
    load_dotenv(os.getenv("PROJECT_NAME"))
except FileNotFoundError:
    sys.exit(display.alert(f"Configuration could not be loaded {repr(Exception)}"))

#display.clear_screen()

# Initialize logs
logger = logs.init_logger()

# Initialize script info
start_date = arrow.now(os.getenv("TIMEZONE", "Europe/Paris"))
display.start_info(start_date, "Data consistence")

if __name__ == "__main__":
    logger.debug("Starting script")

    ## YOUR CODE HERE !!

    # End script
    display.end_info(start_date)
    sys.exit()