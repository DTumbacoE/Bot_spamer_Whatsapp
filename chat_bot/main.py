"""
Main module for the WhatsApp chat bot.

This module handles the automation of sending messages via WhatsApp Web
using pyautogui and webbrowser.
"""

import webbrowser
from time import sleep

import pyautogui

# Constants
WHATSAPP_URL = "https://web.whatsapp.com/send?phone=+codigonumerotelefonico"
MESSAGE_FILE = "mensaje.txt"
WAIT_TIME_SECONDS = 60


def open_whatsapp_web() -> None:
    """
    Open WhatsApp Web in the default browser.

    This function opens the WhatsApp Web URL for the specified phone number.

    Raises:
        Exception: If there is an error opening the browser.
    """
    try:
        webbrowser.open(WHATSAPP_URL)
    except Exception as e:
        raise RuntimeError(f"Failed to open WhatsApp Web: {e}") from e


def wait_for_whatsapp_load() -> None:
    """
    Wait for WhatsApp Web to load.

    This function pauses execution for a specified duration to allow
    WhatsApp Web to fully load in the browser.
    """
    sleep(WAIT_TIME_SECONDS)


def read_and_send_message(file_path: str) -> None:
    """
    Read message from file and send it via WhatsApp Web.

    This function reads the message file line by line and types each line
    followed by pressing enter to send the message.

    Args:
        file_path: Path to the message file.

    Raises:
        FileNotFoundError: If the message file does not exist.
        IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                pyautogui.typewrite(line)
                pyautogui.press("enter")
    except FileNotFoundError:
        raise FileNotFoundError(f"Message file not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading message file: {e}") from e


def main() -> None:
    """
    Main entry point for the WhatsApp chat bot.

    This function orchestrates the entire process:
    1. Opens WhatsApp Web
    2. Waits for the page to load
    3. Reads and sends the message from the file
    """
    try:
        open_whatsapp_web()
        wait_for_whatsapp_load()
        read_and_send_message(MESSAGE_FILE)
    except Exception as e:
        print(f"Error in chat bot execution: {e}")
        raise


if __name__ == "__main__":
    main()