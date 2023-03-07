import traceback
from . import DL as http
from typing import Dict, Optional, Any


API_KEY = 'your api key, to get one contact glory#0007'


class VileAPI:
    def __init__(self, api_key: str = API_KEY) -> None:
        self.key = api_key

    
    async def user(self, user_id: int) -> Dict[str, Any]:
        return await http.get(
            'https://api.vilebot.xyz/user', 
            headers={'Authorization': self.key}, 
            params={'user_id': user_id}
        )


    async def names(self, user_id: int) -> Dict[str, Any]:
        return await http.get(
            'https://api.vilebot.xyz/names', 
            headers={'Authorization': self.key}, 
            params={'user_id': user_id}
        )


    async def tiktok(self, url: str) -> Dict[str, Any]:
        return await http.get(
            'https://api.vilebot.xyz/tiktok', 
            headers={'Authorization': self.key}, 
            params={'url': url}
        )


    async def youtube(self, url: str) -> Dict[str, Any]:
        return await http.get(
            'https://api.vilebot.xyz/youtube', 
            headers={'Authorization': self.key}, 
            params={'url': url}
        )


    async def images(self, query: str, safe: str = 'false') -> Dict[str, Any]:
        return await http.get(
            'https://api.vilebot.xyz/images', 
            headers={'Authorization': self.key}, 
            params={'query': url, 'safe': safe}
        )


    async def tags(self) -> Dict[str, Any]:
        return await http.get(
            'https://api.vilebot.xyz/tags', 
            headers={'Authorization': self.key}
        )


    async def transparent(self, url: str) -> Dict[str, Any]:
        return await http.post(
            'https://api.vilebot.xyz/transparent', 
            headers={'Authorization': self.key}, 
            params={'url': url}
        )


    async def ocr(self, url: str) -> Dict[str, Any]:
        return await http.post(
            'https://api.vilebot.xyz/ocr', 
            headers={'Authorization': self.key}, 
            params={'url': url}
        )


    async def translate(self, text: str, target: str = 'english') -> Dict[str, Any]:
        return await http.get(
            'https://api.vilebot.xyz/transparent', 
            headers={'Authorization': self.key}, 
            params={'text': text, 'target': target}
        )


    async def hex(self, hex: str) -> Dict[str, Any]:
        return await http.get(
            'https://api.vilebot.xyz/hex', 
            headers={'Authorization': self.key}, 
            params={'hex': hex}
        )
