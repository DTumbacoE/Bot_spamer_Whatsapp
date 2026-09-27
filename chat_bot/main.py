"""
Chat Bot Main Module.

This module handles the automation of sending messages via WhatsApp Web
using PyAutoGUI and webbrowser.
"""

import webbrowser
from time import sleep
from typing import Final

import pyautogui

# Constants
WHATSAPP_URL: Final[str] = "https://web.whatsapp.com/send?phone=+codigonumerotelefonico"
MESSAGE_FILE: Final[str] = "mensaje.txt"
WAIT_TIME_SECONDS: Final[int] = 60


def send_whatsapp_message() -> None:
    """
    Opens WhatsApp Web, waits for the page to load, and types the message
    from a local file line by line.

    This function performs the following steps:
    1. Opens the WhatsApp Web URL in the default web browser.
    2. Waits for a specified duration to allow the page to load.
    3. Reads the message content from a local text file.
    4. Types each line of the file and presses 'enter' after each line.

    Raises:
        FileNotFoundError: If the message file does not exist.
        PermissionError: If the message file cannot be read.
    """
    # Open WhatsApp Web in the default browser
    webbrowser.open(WHATSAPP_URL)

    # Wait for the page to load
    sleep(WAIT_TIME_SECONDS)

    # Read and type the message from the file
    with open(MESSAGE_FILE, "r", encoding="utf-8") as file:
        for line in file:
            pyautogui.typewrite(line)
            pyautogui.press("enter")


if __name__ == "__main__":
    send_whatsapp_message()