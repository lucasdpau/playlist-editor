#a simple script that will create an edited copy of a m3u8 playlist. The copy will be different
#from the original, it will have the paths of each file in the playlist changed. However
#it will keep subfolders intact
#eg. C://Desktop/Music/File -> D://Folder/New Folder/File
#eg2 C://Desktop/Music/BSB/File -> D://Folder/New Folder/BSB/File

old_file_name = "Lucas Music.m3u8"
new_file_name = "Lucas Music D Drive.m3u8"


#first open an m3u8 playlist file. must specify encoding for unicode to work
old_playlist = open(old_file_name, 'r', encoding = "utf8")
new_playlist = open(new_file_name, 'w', encoding = "utf8")


#specify a 'file path' in the playlist's file info that needs to be removed, and 
#specify another file path that will replace it
old_path = "\\Users\\Lucas\\Desktop\\"
new_path = "D:\\"
#so here, ""\\Users\\Lucas\\Desktop\\Music\x.mp3" will become "D:\\Music\x.mp3"

#then go line by line. Each line in m3u8 file is either an #EXTINF or a file path
#Copy all lines, but if its a file path then edit it first
def check_line(line):
    if line[0] == '#':
        return False
    else:
        return True
#if a line starts with #, it's #EXTINF, and not a file path name
        
def replace_path(line):
    new_line = line.replace(old_path, new_path)
    return(new_line)

#run a loop to go thru the whole playlist
for line in old_playlist:
    if check_line(line):
        new_playlist.write(replace_path(line))
    else:
        new_playlist.write(line)
    print(line)

#save the copied file.
old_playlist.close()
new_playlist.close()