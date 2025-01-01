# Desktop-ToDo

**Before anything, go into the .py file and update your paths!**

**Turn your desktop into your todo list**

a script to turn your todo.txt files into an image displayed on your desktop at all times.

with some steps, all it takes is running 'todo' in your terminal to update the wallpaper image to your text file with it's new changes.

for linux users you can create an alias that will do this for you, making it easy to run the command:

1. Edit your shell configuration file

2. If you're using bash, open the .bashrc file in your home directory: nano ~/.bashrc
If you're using zsh, open .zshrc: nano ~/.zshrc

3. Add an alias: Add the following line to the file: alias todo='cd /path/to/your/.py/file && python3 todo.py'

4. Reload your shell configuration: After saving and closing the file, run the following to reload the configuration: source ~/.bashrc        If you're using zsh: source ~/.zshrc

5. Set your desktop wallpaper to the created image.

Now, you can run 'todo' in the terminal to automatically cd into the directory and run your todo.py script


**Making Changes**

If you open the todo.py script in your text editor of choice, you should easily be able to update the paths to everything.

The code is commented to help you make changes like placing the text, changing colors of backgrounds and text, chaning fonts, etc.

Remember, your image will be generated to wherever your .py is located.

