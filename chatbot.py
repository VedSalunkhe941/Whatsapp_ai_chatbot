import time
import pyautogui
import pyperclip
import re
from client import generate_reply

# Give yourself 3 seconds to switch to the target window
time.sleep(3)

# 1. Click on the icon
pyautogui.click(1184,1050)


time.sleep(0.5)
last_processed_message = ""
while True:
# 2. Drag to select the text
  pyautogui.moveTo(1877,188, duration=0.2)
  pyautogui.dragTo(
     1863,
     931,
     duration=0.8,
     button="left"
   )


  time.sleep(0.2)

# 3. Copy selected text
  pyautogui.hotkey("ctrl", "c")

# Wait for clipboard to update
  time.sleep(0.3)

# 4. Store clipboard contents in a variable
  copied_text = pyperclip.paste()

  print("Copied Text:")
  print(copied_text)

  MY_NAME = "Ved:)"

  pattern = r"\[(.*?)\]\s(.*?):\s(.*?)(?=\n\[|\Z)"

  messages = re.findall(pattern, copied_text, re.DOTALL)

  last_message = ""

  for _, sender, message in reversed(messages):

    if sender.strip() != MY_NAME:
        last_message = message.strip()
        break

  print("\nLast Incoming Message:")
  print(last_message)


  if last_message == last_processed_message:
      time.sleep(2)
      continue

  last_processed_message = last_message

  reply = generate_reply(last_message)

  time.sleep(1)

# Click on the message input box
  pyautogui.click(962, 986)   # <-- Tuza message box cha coordinate

# Type AI reply
  pyautogui.write(reply, interval=0.01)

# Send message
  pyautogui.press("enter")


 
  print("\nAI Reply:")
  print(reply)

  time.sleep(3)