import os
from datetime import datetime

def print_file_modification_dates(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Loop through the files
    for file_name in files:
        # Get the full path of the file
        file_path = os.path.join(folder_path, file_name)
        
        # Get the modification time of the file
        modification_time = os.path.getmtime(file_path)
        
        # Convert the modification time to a datetime object
        modification_datetime = datetime.fromtimestamp(modification_time)
        
        # Print the file name and modification date
        print(f"{file_name} was last modified on {modification_datetime}")


def sort_files_by_modification_time(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Create a dictionary to store the modification times of each file
    modification_times = {}
    
    # Loop through the files
    for file_name in files:
        # Get the full path of the file
        file_path = os.path.join(folder_path, file_name)
        
        # Get the modification time of the file
        modification_time = os.path.getmtime(file_path)
        
        # Convert the modification time to a datetime object
        modification_datetime = datetime.fromtimestamp(modification_time)
        
        # Store the modification datetime in the dictionary
        modification_times[file_name] = modification_datetime
    
    # Sort the dictionary by value in descending order
    sorted_modification_times = dict(sorted(modification_times.items(), key=lambda item: item[1], reverse=True))
    
    # Return the sorted dictionary
    return sorted_modification_times

file = sort_files_by_modification_time("downloads")
print(file)