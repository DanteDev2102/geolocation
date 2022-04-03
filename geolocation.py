import urllib
import json

def main():
	url = "https://ipinfo.io/172.217.9.4/json"
	v = urllib.urlopen(url)
	j = json.loads(v.read())

	for dato in j:
		print(f"{dato} : {j[dato]}")
	if __name__ == 'pip__main__':
		try:
			main()
		except KeyboardInterrupt:
			exit()


main()