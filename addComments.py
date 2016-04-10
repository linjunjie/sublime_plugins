#可以自动添加这里约定好的注释

import datetime
import sublime_plugin

class addCommentsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("insert_snippet",
			{
				"contents" : "/**""\n"
					" * @Description: 	Description""\n"
					" * @Datetime: 		" "%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
					" * @Author: 		Your Name""\n"
					" */"
			}
		)