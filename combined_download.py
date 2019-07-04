import os
from dail_download_support_functions import open_file_and_read_html, get_debate_links, speech_processing_whole_day


file_directory = "/Users/colleendriscoll/Dropbox/Dissertation/data/Ireland/debates/oireachtas html files/"
errors_file_out = "/Users/colleendriscoll/Dropbox/errors.txt"


file_end_L2 = sorted(os.listdir(file_directory + "Level 2 pages"))
level_2_file_names = [file_directory + "Level 2 pages/" + 
					  file_end_L2[i] for i in range(len(file_end_L2))]

### PUTTING IT ALL TOGETHER

begin_num = 229
end_num = begin_num
day_index = 0
errors = []
## For each file in the list of results pages

for html_file in level_2_file_names[begin_num:]:
	print(html_file)
	L2_file_bs_obj = open_file_and_read_html(html_file) ## Opening to BS object
	## Get each day from the page
	day_links_list = get_debate_links(L2_file_bs_obj)
	day_index = 0
	for day_link in day_links_list:
		try:
			day_index +=1
			# Writing json to file based on date
			speech_processing_whole_day(day_link)
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			index_of_error = str(end_num)+ "_" + str(day_index)
			errors.append(index_of_error)
			with open(errors_file_out, "a+") as f:
				f.write(index_of_error + "\n")
	end_num +=1
	print(end_num)
	
print("Done!")

print("Errors: ", errors)