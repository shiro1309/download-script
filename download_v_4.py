import webbrowser as wb, pyautogui as pgi, json, os, time

# this code is for mp4upload new (30sek waiting) and a 1440p screen the download and dlownload click function need to be changed to fit yout screen, use the screen_where.py to find out

# changes in this verison
# oppen a lot of tabs at once like 20 of them and then keep tabs on them by using a number that is reset every time and can be a maximum of the amount of tabs open
# after every season of download, save it and then change the name insted of it being the last thing
# use pygame to make a simple gui window


class download:
    def page_close(self):
        pgi.moveTo(100, 700)
        pgi.leftClick()
        pgi.keyDown("ctrl")
        pgi.press("w")
        time.sleep(0.5)
        pgi.keyUp("ctrl")
        
    def page_nav(self):
        pgi.moveTo(1680, 280)
        pgi.leftClick()
    
    def page_down(self):
        time.sleep(1)
        pgi.moveTo(1680, 670)
        pgi.leftClick()
        
    def clickpage(self):
        pgi.moveTo(100, 700)
        pgi.leftClick()
        
    def goback(self):
        pgi.keyDown("ctrl")
        pgi.keyDown("shift")
        pgi.press("tab")
        time.sleep(0.1)
        pgi.keyUp("ctrl")
        pgi.keyUp("shift")
        
    def gofront(self):
        pgi.keyDown("ctrl")
        pgi.press("tab")
        time.sleep(0.1)
        pgi.keyUp("ctrl")
    
    def open_tabs(self, links):
        for link in links:
            wb.open(link)
            time.sleep(0.2)
            
    def downprep(self,links):
        self.open_tabs(links)
        self.clickpage()
        for i in range(len(links)-1):
            self.page_nav()
            self.goback()
        self.page_nav()

class get_meta_data:
    def get_all_data(self, series_data):
        url_list = []
        episode_list = []
        season_data = []
        series_name = []
        
        for i in series_data["down"]:
            series_name.append(i)
            n = 0
            
            for j in series_data["down"][i]:
                n += 1
                n_ = 0
                
                for z in series_data["down"][i][j]:
                    n_ += 1
                    url_list.append(series_data['down'][i][j][z])
                    
                episode_list.append(n_)
                
            season_data.append(n)
            
        return series_name, season_data, episode_list, url_list
    
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
            
    # cant get it better than this
    def rename(self, old_name, new_name):
        for i in range(len(old_name)):
            os.rename(f"downloads/{old_name[i]}", f"downloads/{new_name[i]}")
            
    def check_new_file(self, no_new_file, old_name_list):
        files = os.listdir("downloads")
        for file in files:
            if ".part" not in file:
                if file not in old_name_list:
                    old_name_list.append(file)
                    no_new_file = False
                else:
                    no_new_file = True
        return old_name_list, no_new_file 

class App:
    def __init__(self):
        self.json_file = json.load(open("file.json"))

        self.meta = get_meta_data()
        self.down = download()
        self.file_name = file_name()

        self.series, self.seasons, self.episode_count, self.url_list= self.meta.get_all_data(self.json_file)
        self.no_new_file = False
        self.new_name_list = []
        self.old_name_list = []
        self.temp_array = []
        
        
    def run(self):
        print(self.series, self.seasons, self.episode_count)
        print("it will take " + str(round(sum(self.episode_count)*220/60/60/5, 2)) + " hours with 5Mb/s")
        print("it will be " + str(round(sum(self.episode_count)*220/1000, 2)) + " Gb of data if the episode average is 220MB")
        n = 0
        episode = 0
        batch_size = 10
        while True:
            while True:
                list_2 = self.url_list[n*batch_size:(n+1)*batch_size]

                self.down.downprep(list_2) # opens and prepere the pages for download just need to wait for 32 seconds
                time.sleep(32) # the waiting time
                for i in range(len(list_2)): # loops over links but as a number
                    episode += 1
                    self.down.page_down() # starts the download
                    time.sleep(1)

                    self.down.page_close()
                    files = os.listdir("downloads")
                    for file in files:
                        if ".part" not in file:
                            if file not in self.old_name_list:
                                self.old_name_list.append(file)
                                self.new_name_list = self.file_name.note_name(self.series, self.seasons, self.episode_count, n*batch_size+i+1, self.new_name_list)
                    
                    print(episode, len(self.url_list))
                while True:
                    files = os.listdir("downloads")
                    if any(".part" in s for s in files):
                        pass
                    else:
                        break
                n += 1
                if episode >= len(self.url_list):
                    break
            files = os.listdir("downloads")
            if any(".part" in s for s in files):
                pass
            else:
                break
        
        self.file_name.rename(self.old_name_list, self.new_name_list)          
            
        
if __name__ == '__main__':
    app = App()
    app.run()