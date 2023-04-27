import webbrowser as wb, pyautogui as pgi, json
# Define the list of files to download

file = open("file.json")
anime_data = json.load(file)

url_list = []
meta_data = []

#wb.open("url")
for i in anime_data['down']:
    for j in anime_data['down'][i]:
        print(len(anime_data['down'][i]))
        

file.close()




