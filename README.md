# My Obsidian Daily Note

Templates and scripts for my Obsidian daily note.

## The script

My Python script is in the `scripts` folder. It's a simple script that takes the date as an argument and creates a new file in the `daily-notes` folder. It also adds the date to the frontmatter of the file.

The script also makes use of the excellent Dataview Obsidian plugin to dynamically add links back to notes in your Obsidian vault that reference the daily note.

My inspiration for this workflow came from Jamie Rubin:

- [Automating My Daily Notes with Obsidian – Jamie Todd Rubin](https://jamierubin.net/2021/02/08/automating-my-daily-notes-with-obsidian/)
- [My Obsidian Daily Notes Automation Script is Now Available on GitHub – Jamie Todd Rubin](https://jamierubin.net/2021/04/01/my-obsidian-daily-notes-automation-script-is-now-available-on-github/)

Jamie was also kind enough to help me implement the script on my macOS device using the LaunchControl app.

## The template

The template is in the `templates` folder. It's a simple template that uses the `date` variable to create a title and a link to the daily note. It also uses the Dataview plugin to add links to notes that reference the daily note.

The template also invokes the Templater plugin for Obsidian to source the weather information from `wttr.in` so you'll need to install that Obsidian plugin as well.

You can then run the template manually if you decide to create a daily note manually.
