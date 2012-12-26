import sublime, sublime_plugin

class EnableLogCommandsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.log_commands(True)

class DisableLogCommandsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.log_commands(False)
