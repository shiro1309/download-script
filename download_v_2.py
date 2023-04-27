import webbrowser as wb, pyautogui as pgi, json, os, time


#save the files and what they are going to be named
#when download is finished then go over the names and change them

class download:
    def page_close(self):                                                                               # gage close function
        pgi.moveTo(100, 700)                                                                            # moves the cursor to cordinates 100, 700
        pgi.leftClick()                                                                                 # left click with the mouse
        pgi.keyDown("ctrl")                                                                             # gold ctrl
        pgi.press("w")                                                                                  # press w
        time.sleep(0.5)                                                                                 # wait for 0.5 seconds
        pgi.keyUp("ctrl")                                                                               # release the ctrl key
        
    def download_click(self):                                                                           # download link function
        pgi.moveTo(1278, 284)                                                                           # goes to the first nav link
        pgi.leftClick()                                                                                 # left click with the mouse
        time.sleep(3)                                                                                   # wait for the page to load
        pgi.moveTo(1650, 600)                                                                           # go to the download link
        pgi.leftClick()                                                                                 # click the download link

    def check_down_single(self):                                                                        # check if the download is done
        files = os.listdir("downloads")                                                                 # gets the directory list

        if any(".part" in s for s in files):                                                            # if any of the files have the .part ending
            return True #                                                                               # return True to keep the while active
        else:                                                                                           # else                        
            return False                                                                                # return False to stop the while loop

class get_meta_data:
    def get_series_name(self, series_data):                                                             # get the series name
        meta_data = []                                                                                  # meta data list
        for i in series_data['down']:                                                                   # loops over series data
            meta_data.append(i)                                                                         # append the content of the series to the meta data list
        return(meta_data)                                                                               # return the meta data list
    
    def get_seasons(self, series_data, name_data):                                                      # get the season data
        season_data = []                                                                                # season data list
        for name in name_data["down"]:                                                                  # loops over the series        
            n = 0                                                                                       # reset n to 0
            for season in series_data["down"][name]:                                                    # loops over the seasons
                n += 1                                                                                  # add 1 to n
            season_data.append(n)                                                                       # when loop done append n to season_data list
        return season_data                                                                              # return season_data list [3, 2]
            
    
    def get_links(self, series_data):                                                                   # get all the links
        url_list = []                                                                                   # url list
        for i in series_data['down']:                                                                   # loops over the series
            for j in series_data['down'][i]:                                                            # loops over the season
                for z in series_data['down'][i][j]:                                                     # loops over the episodes
                    url_list.append(series_data['down'][i][j][z])                                       # append the content of the episodes that are links to the url list
        return url_list #                                                                               # return the url list
    
    def get_episode_count(self, series_data):                                                           # get the amount of episodes
        episode_data = []                                                                               # episode list
        for i in series_data['down']:   #                                                               # loops thru the series
            for j in series_data['down'][i]:                                                            # loops thru the seasons
                n = 0                                                                                   # reset n
                for z in series_data['down'][i][j]:                                                     # loop thru the episodes
                    n += 1                                                                              # adds 1 to n
                episode_data.append(n)                                                                  # when the episode loop is done save the n in the episode list and loop again
        return episode_data                                                                             # return the episode list [2,2,2,2,2]
    
class file_name:
    def note_name(self, names, seasons, episodes, count, new_name_list, old_name_list):                 # note name functio it gets 6 variables and notes down the new and old names into 2 lists for later rename use
        old_name_list = self.add_missing_names(old_name_list, "downloads")                              # the old names list is equal to the add_missing_names function
        
        season_index , episode_slice = self.get_slice_index(count, episodes)                            # gets the curent season and episode
        season_index += 1                                                                               # adds 1 to the season since it starts from 0
        season_name, season_num = self.get_slice_index(season_index, seasons)                           # gets the curent series and the season for that series
        
        new_name = (f"{names[season_name]} - S{season_num}E{episode_slice}.mp4")                        # makes the new name for the file
        file = open("all.txt", "a")                                                                     # oppens the log file
        file.write(new_name+"\n")                                                                       # writes the new name to the log file
        file.close()                                                                                    # closes the log file
        new_name_list.append(new_name)                                                                  # adds the newn name to the new_name_list
        
        return new_name_list, old_name_list                                                             # returns the new_name_list and the old_name_list
        
    def add_missing_names(self, names, directory):                                                      # adds the mising names from the directory to the old names list
        filenames = os.listdir(directory)                                                               # gets all the files in the directory
        for filename in filenames:                                                                      # loops over all the files in the directory
            if filename not in names:                                                                   # if there is a file that doesn't exist in the list
                names.append(filename)                                                                  # then add it to the list
        return names                                                                                    # when the loop is done return the list
    
    # dont go over the total amount of episodes
    def get_slice_index(self, number, slice_sizes):                                                     # list overflow function with 2 inputs
        for i, size in enumerate(slice_sizes):                                                          # loops over the slice_sizes and saves the size of the slice as well as what the idex is
            if number <= size:                                                                          # checks if the number is less or equal to the size
                return i, number                                                                        # if the if is true then it will return the index and the reziced number
            number -= size                                                                              # if the if is false then it minuses the size away from the number and saves it
            
    def rename(self, old_name, new_name):                                                               # rename function with 2 inputs
        for i in range(len(old_name)):                                                                  # loops over the old name list
            os.rename(f"downloads/{old_name[i]}", f"downloads/{new_name[i]}")                           # changes the old names that maches the new name index

class App:
    def __init__(self):                                                                                 # every time the App class is called the __init__ method starts once
        self.json_file = json.load(open("file.json"))                                                   # loads in the json file into the python file

        self.meta = get_meta_data()                                                                     # changes from get_meta_data() to self.meta
        self.down = download()                                                                          # changes from download() to self.down
        self.file_name = file_name()                                                                    # changes from file_name() to self.file_name

        self.series = self.meta.get_series_name(self.json_file)                                         # gets what the names for the series are
        self.seasons = self.meta.get_seasons(self.json_file, self.series)                               # how many seasons there are per series
        self.episode_count = self.meta.get_episode_count(self.json_file)                                # how many episodes there are per season
        self.link_data = self.meta.get_links(self.json_file)                                            # gets all the links into a single list
        self.new_name_list = []                                                                         # makes a list for all the new names
        self.old_name_list = []                                                                         # the list for all the old names

    def run(self):                      
        print(self.series, self.seasons, self.episode_count)                                            # printer ut all meta dataen untat link listen

        for episode in range(len(self.link_data)):                                                      # loops over every item in the link list and names the number episodes
            wb.open(self.link_data[episode])                                                            # opens up the link in the browser
            time.sleep(1)                                                                               # wait 1 seconds
            self.down.download_click()                                                                  # runs the download click function
            time.sleep(1)                                                                               # waits 1 seconds
            val = self.down.check_down_single()                                                         # checks if the download is complete
            while val:                                                                                  # as long as the download is not done continue
                time.sleep(10)                                                                          # wait 10 seconds
                val = self.down.check_down_single()                                                     # checks if the download is complete
            self.down.page_close()                                                                      # does the close page function
            self.new_name_list, self.old_name_list = self.file_name.note_name(self.series,              # update the name lists
                                                                              self.seasons, 
                                                                              self.episode_count, 
                                                                              episode+1, 
                                                                              self.new_name_list, 
                                                                              self.old_name_list)
        self.file_name.rename(self.old_name_list, self.new_name_list)                                   # rename all the files in the old name list to the new name list
                

if __name__ == '__main__':                                                                              # dont know what it does but it is true
    app = App()                                                                                         # makes the App class to a variable
    app.run()                                                                                           # use the run function inside the app variable