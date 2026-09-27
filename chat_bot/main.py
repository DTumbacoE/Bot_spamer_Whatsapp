"""
Main module for the chat bot application.

This module handles the automation of sending messages via WhatsApp Web
using browser automation and keyboard input simulation.
"""

import webbrowser
from time import sleep
from typing import NoReturn

import pyautogui


def calculate_discount() -> NoReturn:
    """
    Execute the WhatsApp message sending automation sequence.

    This function opens WhatsApp Web in the default browser, waits for the
    page to load, and then types and sends the contents of a predefined
    message file line by line.

    Note:
        The function name `calculate_discount` is preserved for API
        compatibility, but the underlying logic performs message automation.

    Raises:
        FileNotFoundError: If "mensaje.txt" does not exist in the current
            working directory.
        pyautogui.PyAutoGUIException: If keyboard input simulation fails.

    Returns:
        NoReturn: This function does not return a value.
    """
    # Open WhatsApp Web with the specified phone number
    webbrowser.open('https://web.whatsapp.com/send?phone=+codigonumerotelefonico')

    # Wait for the browser to load the page
    sleep(60)

    # Read and send the message content line by line
    with open("mensaje.txt", "r", encoding="utf-8") as file:
        for line in file:
            pyautogui.typewrite(line)
            pyautogui.press("enter")


if __name__ == "__main__":
    calculate_discount()