from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.bot import Mochi

from discord.ext import commands

from ..abc.cog import BaseCog


class Misc(BaseCog):
    def __init__(self, bot: Mochi):
        super().__init__(bot)

    @commands.command(aliases=["ss"])
    async def screenshot(self, ctx: commands.Context) -> None:
        ...


def setup(bot):
    bot.add_cog(Misc(bot))
