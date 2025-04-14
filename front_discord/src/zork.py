import os
from ZorkAPI.managers.game_runner import GameRunner

game_sessions = {}

def launch_story(story_folder: str, story_filename: str = None):
    possible_filenames = ['story.yaml', 'story.yml'] if story_filename is None else [story_filename]
    base_path = os.path.join(os.getcwd(), "storage", "stories", story_folder)
    story_file = None
    for filename in possible_filenames:
        candidate = os.path.join(base_path, filename)
        if os.path.isfile(candidate):
            story_file = candidate
            break
    if story_file is None:
        raise FileNotFoundError(f"Story file not found in folder '{story_folder}'.")
    
    runner = GameRunner(story_file)
    output = runner.get_pretty_output()
    return runner, output

def zork(bot):
    @bot.command(name="liststories")
    async def list_stories(ctx):
        stories_root = os.path.join(os.getcwd(), "storage", "stories")
        try:
            folders = [
                d for d in os.listdir(stories_root)
                if os.path.isdir(os.path.join(stories_root, d))
            ]
            if folders:
                message = "**Available Stories:**\n\n" + "\n".join(f"- {folder}" for folder in folders)
            else:
                message = "**No stories found.**"
            await ctx.send(message)
        except Exception as e:
            await ctx.send(f"**Error:** {str(e)}")


    @bot.command(name="startgame")
    async def start_game(ctx, story: str):
        try:
            runner, output = launch_story(story)
            game_sessions[ctx.channel.id] = runner
            await ctx.send(output)
        except Exception as e:
            await ctx.send(f"Erreur : {str(e)}")

    @bot.command(name="choice")
    async def make_choice(ctx, choice_number: int):
        if ctx.channel.id not in game_sessions:
            await ctx.send("!startgame. to start a game first")
            return
        
        runner = game_sessions[ctx.channel.id]
        try:
            runner.process_choice(choice_number - 1)
            output = runner.get_pretty_output()
            await ctx.send(output)
            if not runner.current_node.choices:
                del game_sessions[ctx.channel.id]
        except Exception as e:
            await ctx.send(f"Erreur : {str(e)}")
