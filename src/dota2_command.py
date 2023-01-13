import pyttsx3
import pyautogui
import asyncio
import json
import uuid

import numpy as np
import cv2 as cv
from PIL import ImageGrab, Image

icon_mode = "laptop"
icon_path = f"../assets/dota2/accept_icon_{icon_mode}.jpg"
screen_size = pyautogui.size()
REGION = (0, 0, screen_size[0], screen_size[1])

ACCEPT_PICTURE_PIL = Image.open(icon_path)
ACCEPT_PICTURE_CV = cv.imread(icon_path)

def check_image_exists():
    img = ImageGrab.grab(bbox = REGION )
    img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
    res = cv.matchTemplate(img_cv, ACCEPT_PICTURE_CV, cv.TM_CCOEFF_NORMED)
    conf = (res >= 0.8)
    width, height = ACCEPT_PICTURE_PIL.size
    loc = np.where(conf)
    for pt in zip(*loc[::-1]):
        if conf.any():
            return (pt[0], pt[1], width, height), True
    return (0, 0, width, height), False

class Dota2:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = None
        self._initialize_tts()
        self._mouse_position = None
        self.match_found = False
        
    def _initialize_tts(self):
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("rate", 145)
        self.engine.setProperty("voice", self.voices[1].id)
    
    def _speak(self, text: str):
        self.engine.say(f"  {text} ")
        self.engine.runAndWait()
        
        
    async def _await_match(self):
        icon_coords, isFound = check_image_exists()
        if isFound:
            self._mouse_position = pyautogui.center(icon_coords)
            return True
        await asyncio.sleep(0)
                
        
    async def _click_accept(self):
        pyautogui.moveTo(self._mouse_position, _pause = False)
        pyautogui.click(self._mouse_position, _pause = False) 
        # Read Data in Json File
        with open("../status.json") as fr:
            data = dict(json.load(fr))
    
        # Overwrite Auto Accept depending on what user wants
        curr_id = data.get("current_match_id")
        data["current_match_id"] = str(uuid.uuid4())
            
        # Save it
        with open("../status.json", 'w') as fw:
            json.dump(data, fw, indent = 2)
        await asyncio.sleep(0)
        
    async def run(self):
        self.match_found = await self._await_match()
            # await self._click_accept()
            