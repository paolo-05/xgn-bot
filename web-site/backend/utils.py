import requests

import constants


async def get_token(code: str):
    data = {
        'client_id': constants.CLIENT_ID,
        'client_secret': constants.CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': constants.REDIRECT_URI,
        'scope': 'identify guilds'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp = requests.post(
        "https://discord.com/api/oauth2/token", data=data, headers=headers)
    resp.raise_for_status()
    return resp.json()['access_token']


async def get_user_info(token):
    resp = requests.get("https://discord.com/api/v6/users/@me",
                        headers={"Authorization": f"Bearer {token}"})
    resp.raise_for_status()
    return resp.json()


async def get_user_info_by_id(user_id):
    token = constants.BOT_TOKEN
    resp = requests.get(f"https://discord.com/api/v6/users/{user_id}",
                        headers={"Authorization": f"Bot {token}"})
    resp.raise_for_status()
    return f'{resp.json()["username"]}#{resp.json()["discriminator"]}'


async def get_guild_data(guild_id: int):
    token = constants.BOT_TOKEN
    resp = requests.get(
        f"https://discord.com/api/v6/guilds/{guild_id}", headers={"Authorization": f"Bot {token}"})
    try:
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError:
        return None


async def get_valid_guilds(token: str):
    resp = requests.get("https://discord.com/api/v6/users/@me/guilds",
                        headers={"Authorization": f"Bearer {token}"})
    resp.raise_for_status()

    return [
        {
            "id": str(guild['id']),
            "name": str(guild['name']),
            "icon_url": str(f"https://cdn.discordapp.com/icons/{guild['id']}/{guild['icon']}.png?size=512"),
            "in":False if await get_guild_data(guild['id']) is None else True
        } for guild in resp.json() if (guild['permissions'] & 0x20) == 0x20]


async def get_guild_channels(guild_id: int):
    token = constants.BOT_TOKEN
    resp = requests.get(
        f"https://discord.com/api/v6/guilds/{guild_id}/channels", headers={"Authorization": f"Bot {token}"}
    )
    return [{'id': i['id'], 'name': i['name'], 'guild_id': i['guild_id']} for i in resp.json() if i['type'] == 0]


async def get_channel_by_id(guild_id: int, channel_id: str):
    channels = await get_guild_channels(guild_id)
    channel_name = [channel['name']
                    for channel in channels if channel['id'] == channel_id]
    return channel_name[0]
