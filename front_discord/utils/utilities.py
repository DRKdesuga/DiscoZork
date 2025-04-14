def utils(bot):
    @bot.command(name="welp")
    async def help_cmd(ctx):
        help_text = (
            "**Available Commands:**\n\n"
            "`!welp` - Displays this help message.\n\n"
            "`!liststories` - Lists available stories in the storage.\n\n"
            "`!startgame <story_folder>` - Starts a game session with the selected story.\n\n"
            "`!choice <number>` - Processes your choice and advances the game.\n"
        )
        await ctx.send(help_text)
