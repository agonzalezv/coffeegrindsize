import webbrowser

# Method to open blog web page
def blog_goto(self, *args):
    webbrowser.open("https://coffeeadastra.com")


# Method to display help
def launch_help(self):
    webbrowser.open(
        "https://www.dropbox.com/s/m2af0aer2e17xie/coffee_grind_size_manual.pdf?dl=0"
    )


# Method to quit user interface
def quit_gui(root):
    root.quit()


# Method to return a lighter color
def lighter(self, color, percent):
    color = np.array(color) * 255
    white = np.array([255, 255, 255])
    vector = white - color
    output = tuple((color + vector * percent) / 255.0)
    return output


# Method to quit reset interface
def reset_gui(self):
    python = sys.executable
    os.execl(python, python, *sys.argv)


# Method to clear entry (when clicked)
def clear_entry(self, entry_id):
    entry_id.delete(0, "end")


# Trigger expert mode
def toggle_expert_mode(self):
    if self.expert_mode is False:
        self.frame_options.tkraise()
        self.expert_mode = True
        return

    if self.expert_mode is True:
        self.simple_frame_options.tkraise()
        self.expert_mode = False
        return


# Method to toggle advanced options
def toggle_advanced_options(self):
    if self.display_advanced_options is False:
        self.display_advanced_options = True
    else:
        self.display_advanced_options = False
    print(self.display_advanced_options)
    self.frame_options.refresh()
