import telethon

class Client:
    def __init__(self, api_hash, api_id):
        self.client = telethon.TelegramClient(session="telegram_client_session", api_id=api_id, api_hash=api_hash)

    # Connect to Telegram
    async def connect(self):
        await self.client.start()

    # Get myself
    async def get_me(self):
        me = await self.client.get_me()
        return f"{me.username}"

    # Disconnect from Telegram
    async def disconnect(self):
        await self.client.disconnect()

    # Get all chats - the ones I am in
    async def get_dialogs(self):
        return await self.client.get_dialogs()
    
    # Given a name, get chat id - return None if not found
    async def get_chat_id(self, name):
        chats = await self.get_dialogs()
        for chat in chats:
            if chat.name == name:
                return chat.id
        return None
    
    # Get N messages from dialog id
    async def get_all_messages(self, dialog_id, n):
        return await self.client.get_messages(dialog_id, limit=n)
    
    # Get N messages from dialog id that I have sent
    async def get_mine_messages(self, dialog_id, n):
        return await self.client.get_messages(dialog_id, limit=n, from_user="me")
    
    # Get users in dialog id
    async def get_users(self, dialog_id):
        return await self.client.get_participants(dialog_id)
    
    # Delete messages in dialog id 
    async def delete_messages(self, dialog_id, message_ids):
        await self.client.delete_messages(dialog_id, message_ids)
