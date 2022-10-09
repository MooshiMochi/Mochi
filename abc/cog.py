from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.bot import Mochi

from discord.ext.commands import Cog


class BaseCog(Cog):
    def __init__(self, bot: Mochi):
        self.bot: Mochi = bot

    async def cog_load(self) -> None:
        self.bot.logger.info(f"Loaded {self.__cog_name__} cog...")

    async def cog_unload(self) -> None:
        self.bot.logger.info(f"Unloaded {self.__cog_name__} cog...")
