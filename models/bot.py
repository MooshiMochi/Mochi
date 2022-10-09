import os

from discord import Intents
from discord.ext import commands
from loguru import Logger


class Mochi(commands.Bot):
    logger = Logger()
    logger.configure(
        **{
            "handlers": [
                {
                    "sink": "logs/bot.log",
                    "level": "DEBUG",
                    "rotation": "1 week",
                    "compression": "zip",
                }
            ]
        }
    )

    def __init__(self, intents: Intents, prefix: str, **options):
        super().__init__(
            command_prefix=commands.when_mentioned_or(prefix),
            intents=intents,
            **options,
        )

    async def on_ready(self):
        self.logger.info(f"Logged in as {self.user} (ID: {self.user.id})")

    async def setup_hook(self) -> None:
        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                try:
                    self.load_extension(f"cogs.{filename[:-3]}")
                except Exception as e:
                    self.logger.error(f"Failed to load extension {filename}: {e}")
