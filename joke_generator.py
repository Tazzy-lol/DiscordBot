import requests
import discord
from discord.ext import commands

class JokeGenerator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joke_api_url = "https://official-joke-api.appspot.com/random_joke"
    
    @commands.command(name='joke')
    async def get_joke(self, ctx):
        """Fetches a random joke from the Official Joke API"""
        try:
            response = requests.get(self.joke_api_url)
            response.raise_for_status()
            
            joke_data = response.json()
            
            # Extract joke components
            joke_type = joke_data.get('type', 'general')
            setup = joke_data.get('setup', '')
            punchline = joke_data.get('punchline', '')
            
            # Create an embed for better formatting
            embed = discord.Embed(
                title="😂 Random Joke",
                description=f"**{setup}**\n\n||{punchline}||",
                color=discord.Color.gold()
            )
            embed.set_footer(text=f"Type: {joke_type}")
            
            await ctx.send(embed=embed)
            
        except requests.exceptions.RequestException as e:
            embed = discord.Embed(
                title="❌ Error",
                description=f"Failed to fetch joke: {str(e)}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(JokeGenerator(bot))
