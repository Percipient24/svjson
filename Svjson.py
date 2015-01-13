import sublime, sublime_plugin

class SvjsonCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		def replace(token, substitute):
			# replace token with substitute 
			dq_edit = self.view.begin_edit()
			dq_list = []
			dq_regions = self.view.find_all(token, sublime.IGNORECASE, substitute, dq_list)
			for pos, region in reversed(zip(dq_regions, dq_list)):
				self.view.replace(dq_edit, pos, region)
			self.view.end_edit(dq_edit)

		# replace the DOCTYPE
		replace(r"<\?.*\?>\n", "")

		# replace the DOCTYPE
		replace(r"<!--.*-->\n", "")

		# replace the DOCTYPE
		replace(r"<!DOC.*>", "[")

		# replace the <svg>
		replace(r"<svg.*\n.*>\n", "")

		# replace for id
		replace("<rect id=", "\t{\n\t\"id\" : ")

		# replace for x
		replace(" x=", ",\n\t\"x\" : ")

		# replace for y
		replace(" y=", ",\n\t\"y\" : ")

		# replace for w
		replace(" width=", ",\n\t\"w\" : ")
		
		# replace for h
		replace(" height=", ",\n\t\"h\" : ")

		# replace the end
		replace("/>", "\n\t},")

		# replace the fills and crud
		replace(r" fill.*,", ",")

		# replace the </svg>
		replace(r",\n</svg>", "\n]")