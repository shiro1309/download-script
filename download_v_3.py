import webbrowser as wb, pyautogui as pgi, json, os, time

# this code is for mp4upload old and a 1440p screen the download and dlownload click function need to be changed to fit yout screen, use the screen_where.py to find out

class download:
    def page_close(self):
        pgi.moveTo(100, 700)
        pgi.leftClick()
        pgi.keyDown("ctrl")
        pgi.press("w")
        time.sleep(0.5)
        pgi.keyUp("ctrl")
        
    def download_click(self):
        pgi.moveTo(1278, 284)
        pgi.leftClick()
        time.sleep(3)
        pgi.moveTo(1650, 847)
        pgi.leftClick()

    def check_down_single(self):
        files = os.listdir("downloads")

        if any(".part" in s for s in files):
            return True
        else:
            return False
    
    def check_down_advanced(self, download_list):
        files = os.listdir("downloads")
        
        for file in files:
            if any(".part" in file) and file not in download_list:
                download_list.append(file)
                return True, download_list
            else:
                return False, download_list

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
    def note_name(self, names, seasons, episodes, count, new_name_list):
        season_index , episode_slice = self.get_slice_index(count, episodes)
        season_index += 1                                                              
        season_name, season_num = self.get_slice_index(season_index, seasons)
        
        new_name = (f"{names[season_name]} - S{season_num}E{episode_slice}.mp4")
        file = open("all.txt", "a")
        file.write(new_name+"\n")
        file.close()
        new_name_list.append(new_name)
        
        return new_name_list
        
    def add_missing_names(self, names, directory):
        filenames = os.listdir(directory)
        for filename in filenames:
            if filename not in names:
                names.append(filename)
        return names
    
    def get_slice_index(self, number, slice_sizes):
        for i, size in enumerate(slice_sizes):
            if number <= size:
                return i, number
            number -= size
            
    def rename(self, old_name, new_name):
        for i in range(len(old_name)):
            os.rename(f"downloads/{old_name[i]}", f"downloads/{new_name[i]}")
            
    def backup(self, old_name, new_name):
        file = open("backup.txt", "a")
        file.truncate(0)
        file.write(old_name + "\n")
        file.write(new_name + "\n")
        file.close()

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
        self.new_file = False
        self.new_name_list = []
        self.old_name_list = []
        self.temp_array = []
        
    def run(self):
        print(self.series, self.seasons, self.episode_count)
        print("it will take " + str(round(sum(self.episode_count)*220/60/60/5, 2)) + " hours with 5Mb/s")
        print("it will be " + str(round(sum(self.episode_count)*220/1000, 2)) + " Gb of data")
        n = 0
        while True:
            list_2 = self.link_data[n*10:(n+1)*10]
            list_3 = []
            
            list_3.clear()
            while True:
                time.sleep(1)
                
                for episode in range(len(list_2)):
                    file_list_old = 0
                    file_list_new = 0
                    
                    if episode not in list_3:
                        
                        files = os.listdir("downloads")
                        for file in files:
                            if ".part" not in file:
                                file_list_old += 1
                                
                        wb.open(list_2[episode])
                        time.sleep(5)
                        self.down.download_click()
                        time.sleep(2)
                        
                        files = os.listdir("downloads")
                        for file in files:
                            if ".part" not in file:
                                file_list_new += 1
                                
                        if file_list_new == file_list_old:
                            val = False
                        elif file_list_new > file_list_old:
                            val = True
                        
                        if val == False:
                            self.down.page_close()
                            self.down.page_close()
                        
                        if val == True:
                            self.down.page_close()
                            list_3.append(episode)

                            dir_files = os.listdir("downloads")

                            for file in dir_files:
                                if ".part" not in file:
                                    if file not in self.old_name_list:
                                        self.old_name_list.append(file)
                                        self.new_name_list = self.file_name.note_name(self.series, self.seasons, self.episode_count, n*10+episode+1, self.new_name_list)
                        print(episode)
                if len(list_2) == len(list_3):
                    break
            
            n += 1
            
            files = os.listdir("downloads")
            if any(".part" in s for s in files):
                pass
            else:
                break
            
        self.file_name.rename(self.old_name_list, self.new_name_list)
        
if __name__ == '__main__':
    app = App()
    app.run()