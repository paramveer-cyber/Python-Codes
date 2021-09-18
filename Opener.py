import psutil, pyautogui, time

while True:
	if "chrome.exe" in (i.name() for i in psutil.process_iter()):
		print("True")
		time.sleep(5)
		pyautogui.hotkey('win', '1')
		pyautogui.hotkey('ctrl', 't')
		pyautogui.typewrite("www.youtube.com", interval=0.1)
		pyautogui.press('enter')
		break

	else:
		print("False")
