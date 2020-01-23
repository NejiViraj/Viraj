import requests
import json



def Neji_version():
	# import neji
	# print(neji.Neji_version())

	# output: Hydrogen-0.0.0.1

	return "Hydrogen-0.0.0.1"


def Neji_upload(put_file_directory_in_string_format):

	# import neji
	# print(neji.Neji_upload(r"C:\...\Pictures\trial\black1 - Copy (5).png"))

	# output: https://file.io/CfJlLI

	r =  requests.post('https://file.io', files={'file': open(str(put_file_directory_in_string_format), 'rb')})
	al1 = json.loads(r.text)
	if al1['link'][0] == "h":
		return al1['link']
	else:
		r2 =  requests.post('https://api.anonymousfiles.io', files={'file': open(str(put_file_directory_in_string_format), 'rb')})
		al2 = json.loads(r2.text)
		if al2["url"][0] == "h":
			return al2["url"]
		else:
			return "inform us"