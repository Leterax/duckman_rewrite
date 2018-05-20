import discord


class EmbedGenerator(object):
	def __init__(self,bot):
		self.bot = bot
		self.help_dict = {"MAIN":HELP_EMBED,"PLACEHOLDER":X_EMBED}
		
		
		# MAIN HELP
		HELP_EMBED = discord.Embed(title="__**Current Commands**__", color=0x547e34, url="https://gwo.io")
		HELP_EMBED.add_field(name="General Commands",
				value="**!help** - Sends this message\n"
					"**!github** - Duckman's Github repository\n"
					"**!ping** - Get Duckman's ping\n"
					"**!who** - Shows how many people are on the server\n"
					"**!tut_code** - Links to the tutorial code\n"
					"**!gamble** - Gamble & win XP"
			)
		HELP_EMBED.add_field(name="User Commands",
			value="**!xp** - See your XP\n"
					"**!xp @username @username2 @username3...** - See the XP of multiple people\n"
					"**!lb** - XP leaderboard\n"
					"**!level** - See your level\n"
					"**!avg_xp** - See the average XP\n"
					"**!me** - See information about yourself\n"
					"**!v_helper** - Vote for someone to become helper"
			)
		HELP_EMBED.add_field(name="Role Commands",
			value="**!role** - Set your roles\n"
					"**!r_role** - Remove your roles\n"
					"**!myrole** - Set your color role\n"
					"**!skill** - Set your skills"
			)
		HELP_EMBED.set_footer(text="Mainly developed by Grewoss | Avatar design by Grassmou")
		HELP_EMBED.set_thumbnail(url=ctx.bot.user.avatar_url)
		
		### SECOND HELP
		X_EMBED = discord.Embed(title="__**Current Commands**__", color=0x547e34, url="https://gwo.io")
		X_EMBED.add_field(name="Example Commands", value="**!help** - Sends this message\n")
		X_EMBED.set_footer(text="Mainly developed by Grewoss | Avatar design by Grassmou")
		X_EMBED.set_thumbnail(url=ctx.bot.user.avatar_url)
		
## in the main.py file:
# helps = EmbedGenerator(bot)
# @bot.command()
# async def help(ctx, arg):
#    await ctx.send(embed=EmbedGenerator.help_dict[arg])
		
		

