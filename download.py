import webbrowser as wb, pyautogui as pgi, json, os, time

class download:
    def page_close(self):
        pgi.moveTo(100, 700)
        pgi.leftClick()
        pgi.keyDown("ctrl")
        pgi.press("w")
        
    def download_click(self):
        pgi.moveTo(1278, 284)
        pgi.leftClick()
        time.sleep(1)
        pgi.moveTo(1650, 600)
        pgi.leftClick()
        
    def check_down_single(self):
        files = os.listdir("downloads")

        if any(".part" in s for s in files):
            return True
        else:
            return False

class get_meta_data:
    def get_series_name(self, series_data):
        meta_data = []
        for i in series_data['down']:
            meta_data.append(i)
        return(meta_data)
    
    def get_seasons(self, series_data, name_data):
        season_data = []
        for name in name_data:
            n = 0
            for season in series_data["down"][name]:
                n += 1
            season_data.append(n)
        return season_data
            
    
    def get_links(self, series_data):
        url_list = []
        for i in series_data['down']:
            for j in series_data['down'][i]:
                for z in series_data['down'][i][j]:
                    url_list.append(series_data['down'][i][j][z])
        return url_list
    
    def get_episode_count(self, series_data):
        episode_data = []
        for i in series_data['down']:
            for j in series_data['down'][i]:
                n = 0
                for z in series_data['down'][i][j]:
                    n += 1
                episode_data.append(n)
        return episode_data
    
class file_name:
    def change_name(self, files, names, seasons, episodes, count):
        filtered_names = []
        for file in files:
            if "- S" not in file:
                filtered_names.append(file)
        
        # gets to know what season and what episode im on
        
        season_index , episode_slice = self.get_slice_index(count, episodes)
        season_index += 1 # compansate so its over the 0 index
        season_name, season_num = self.get_slice_index(season_index, seasons)
        
        new_name = (f"{names[season_name]} - S{season_num}E{episode_slice}.mp4")
        file = open("all.txt", "a")
        file.write(new_name+"\n")
        file.close()
        try:
            os.rename(f"downloads/{filtered_names[0]}", f"downloads/{new_name}")
        except:
            pass
    
    # dont go over the total amount of episodes
    def get_slice_index(self, number, slice_sizes):
        for i, size in enumerate(slice_sizes):
            if number <= size:
                return i, number
            number -= size

class App:
    def __init__(self):
        self.json_file = json.load(open("file.json"))
        
        self.meta = get_meta_data()
        self.down = download()
        self.file_name = file_name()
        
        self.series = self.meta.get_series_name(self.json_file)
        self.seasons = self.meta.get_seasons(self.json_file, self.series)
        self.episode_count = self.meta.get_episode_count(self.json_file)
        self.link_data = self.meta.get_links(self.json_file)
        
        
    def run(self):
        #print(self.series, self.seasons, self.episode_count, self.link_data)
        #files = os.listdir("downloads")
        #self.file_name.change_name(files, self.series, self.seasons, self.episode_count, 3)
        
        for episode in range(len(self.link_data)):
            wb.open(self.link_data[episode])
            time.sleep(1)
            self.down.download_click()
            time.sleep(1)
            val = self.down.check_down_single()
            while val:
                time.sleep(10)
                val = self.down.check_down_single()
            self.down.page_close()
            files = os.listdir("downloads")
            self.file_name.change_name(files, self.series, self.seasons, self.episode_count, episode+1+19)
                

if __name__ == '__main__':
    app = App()
    app.run()