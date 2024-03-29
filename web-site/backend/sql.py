from tortoise import Tortoise
from models import GuildConfig, WelcomeConfig, LeaveConfig, LevelUpConfig, LogChannel


async def connect_db():
    await Tortoise.init(
        db_url="postgres://xgnbot:12345@localhost:5432/bot",
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()


async def get_config(guild_id):
    await connect_db()
    config = await GuildConfig.filter(id=guild_id).get_or_none()
    welcome_conf = await WelcomeConfig.filter(guild_id=guild_id).get_or_none()
    leave_conf = await LeaveConfig.filter(guild_id=guild_id).get_or_none()
    level_conf = await LevelUpConfig.filter(guild_id=guild_id).get_or_none()
    log_conf = await LogChannel.filter(guild_id=guild_id).get_or_none()
    if config:
        prefix = config.prefix
        welcome_enabled = config.welcome_enabled
        if welcome_enabled:
            if welcome_conf is None:
                welcome_message = False
                welcome_channel = False
            else:
                welcome_message = welcome_conf.message
                welcome_channel = welcome_conf.channel_name

        else:
            welcome_message = False
            welcome_channel = False
        leave_enabled = config.leave_enabled
        if leave_enabled:
            if leave_conf is None:
                leave_message = False
                leave_channel = False
            else:
                leave_message = leave_conf.message
                leave_channel = leave_conf.channel_name
        else:
            leave_message = False
            leave_channel = False
        log_enabled = config.log_enabled
        if log_enabled:
            if log_conf is None:
                log_channel = False
            else:
                log_channel = log_conf.channel_name
        else:
            log_channel = False
        level_up_enabled = config.level_up_enabled
        if level_up_enabled:
            if level_conf is None:
                level_message = False
                level_channel = False
            else:
                level_message = level_conf.message
                level_channel = level_conf.channel_name
        else:
            level_message = False
            level_channel = False
    else:
        prefix = '!'
        welcome_enabled = False
        leave_enabled = False
        log_enabled = False
        level_up_enabled = False
        level_message = False
        level_channel = False
    await Tortoise.close_connections()
    return prefix, welcome_enabled, welcome_channel, welcome_message, leave_enabled, leave_message, leave_channel, level_up_enabled, level_message, level_channel, log_enabled, log_channel


async def change_prefix(new_prefix, guild_id):
    await connect_db()
    config = await GuildConfig.filter(id=guild_id).get_or_none()

    config = await GuildConfig.filter(id=guild_id).get_or_none()
    if config is None:
        new_config = GuildConfig(id=guild_id, prefix=new_prefix)
        await new_config.save()
    else:
        config.prefix = new_prefix
        await config.save()

    await Tortoise.close_connections()


async def welcome_event(guild_id, message, channel_id, channel_name):
    await connect_db()

    config = await GuildConfig.filter(id=guild_id).get_or_none()
    welcome_conf = await WelcomeConfig.filter(guild_id=guild_id).get_or_none()
    if config.welcome_enabled == False:
        config.welcome_enabled = True
        await config.save()
    else:
        if welcome_conf is not None:
            welcome_conf.message = message
            welcome_conf.channel_id = channel_id
            welcome_conf.channel_name = channel_name

            await welcome_conf.save()
        else:
            new_config = WelcomeConfig(
                guild_id=guild_id, channel_id=channel_id, message=message, channel_name=channel_name)
            await new_config.save()

    await Tortoise.close_connections()


async def leave_event(guild_id, message, channel_id, channel_name):
    await connect_db()

    config = await GuildConfig.filter(id=guild_id).get_or_none()
    leave_conf = await LeaveConfig.filter(guild_id=guild_id).get_or_none()
    if config.leave_enabled == False:
        config.leave_enabled = True
        await config.save()
    else:
        if leave_conf is not None:
            leave_conf.message = message
            leave_conf.channel_id = channel_id
            leave_conf.channel_name = channel_name
            await leave_conf.save()
        else:
            new_config = LeaveConfig(
                guild_id=guild_id, channel_id=channel_id, message=message, channel_name=channel_name)
            await new_config.save()

    await Tortoise.close_connections()


async def level_system(guild_id, message, channel_id, channel_name):
    await connect_db()

    config = await GuildConfig.filter(id=guild_id).get_or_none()
    level_conf = await LevelUpConfig.filter(guild_id=guild_id).get_or_none()
    if config.level_up_enabled == False:
        config.level_up_enabled = True
        await config.save()
    else:
        if level_conf is not None:
            level_conf.message = message
            level_conf.channel_id = channel_id
            level_conf.channel_name = channel_name
            await level_conf.save()
        else:
            new_config = LevelUpConfig(
                guild_id=guild_id, channel_id=channel_id, message=message, channel_name=channel_name, role1=2112, role2=312312, role3=312312, role4=312312, role5=312312,)
            await new_config.save()

    await Tortoise.close_connections()


async def log_system(guild_id, channel_id, channel_name):
    await connect_db()
    print(channel_name)
    config = await GuildConfig.filter(id=guild_id).get_or_none()
    log_conf = await LogChannel.filter(guild_id=guild_id).get_or_none()
    if config.log_enabled == False:
        config.log_enabled = True
        await config.save()
    else:
        if log_conf is not None:
            log_conf.channel_id = channel_id
            log_conf.channel_name = channel_name
            await log_conf.save()
        else:
            new_config = LogChannel(
                guild_id=guild_id, channel_id=channel_id, channel_name=channel_name)
            await new_config.save()

    await Tortoise.close_connections()


async def disable_(guild_id, action):
    await connect_db()
    config = await GuildConfig.filter(id=guild_id).get_or_none()
    if action == 'welcome':
        config.welcome_enabled = False
    if action == 'leave':
        config.leave_enabled = False
    if action == 'leveling':
        config.level_up_enabled = False
    if action == 'log':
        config.log_enabled = False

    await config.save()

    await Tortoise.close_connections()
