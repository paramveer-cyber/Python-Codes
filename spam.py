['import win32api\n', 'import time\n', 'import mouse\n', '\n', 'width = win32api.GetSystemMetrics(0)\n', 'height = win32api.GetSystemMetrics(1)\n', 'midWidth = int((width + 1) / 2)\n', 'midHeight = int((height + 1) / 2)\n', '\n', 'state_left = win32api.GetKeyState(0x01)  # Left button up = 0 or 1. Button down = -127 or -128\n', 'while True:\n', '    a = win32api.GetKeyState(0x01)\n', '    if a != state_left:  # Button state changed\n', '        state_left = a\n', '        if a < 0:\n', "            mouse.click('left')\n", "            mouse.click('left')\n", "            mouse.click('left')\n", "            mouse.click('left')\n", "            mouse.click('left')\n", "            mouse.click('left')\n", "            mouse.click('left')\n", "            mouse.click('left')\n", "            mouse.click('left')\n", "            mouse.click('left')\n", '        else:\n', '            pass']