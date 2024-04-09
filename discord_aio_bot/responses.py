import discord
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
import bot


async def send_message(message):
    try:
        # Assuming bot.MovieAPI.send_recommedation() returns a dictionary
        movie_information = bot.MovieAPI.send_recommedation()

        # Extract information from the dictionary
        name = movie_information.get("name", "N/A")
        overview = movie_information.get("overview", "N/A")
        release_date = movie_information.get("release date", "N/A")
        rating = movie_information.get("rating", "N/A")
        image = movie_information.get("image", "N/A")
        # Format the information into a sentence
        sentence = f">>> Name: {name}\nOverview: {overview}\nRelease Date: {release_date}\nRating: {rating}\n {image}"

        await message.channel.send(sentence)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTE5Njk4MzAyMDIwNTM4MzczMQ.Giv4bu.DDHtW40wBuYBWgg7bS_6c28jrTvddMjKxpK3WQ'
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has now booted')

    
    
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if str(message.content) == "Chief, Recommend":
            await send_message(message)

    client.run(TOKEN)
    