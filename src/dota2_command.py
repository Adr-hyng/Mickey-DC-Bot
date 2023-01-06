import pyttsx3
import pyautogui
import asyncio
import json
import uuid

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
        # print("Running")
        icon = pyautogui.locateOnScreen("../assets/dota2/accept_icon2.jpg", confidence = 0.9)
        if icon:
            self._mouse_position = pyautogui.center(icon)
            return True
        await asyncio.sleep(0)
                
        
    async def _click_accept(self):
        pyautogui.moveTo(self._mouse_position)
        pyautogui.click(self._mouse_position) 
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
            