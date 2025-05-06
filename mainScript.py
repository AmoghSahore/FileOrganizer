import os
import shutil

#defining common file extensions into their categories
EXT = {
    "Images": [".png",".jpg",".jpeg",".gif"],
    "Videos": [".mp4",".mov",".mkv",".avi"],
    "Docs": [".pdf",".docx",".txt",".xlsx",".pptx"],
    "Music": [".mp3",".wav"],
    "Installers": [".exe",".msi",".bat",".cmd",".dmg",".pkg",".app",".deb",".rpm",".run"],
    "Archives": [".zip",".rar",".tar"],
    "Code": [".py",".c",".js",".html",".css",".cpp",".java",".cs",".ts",".php",".sql",".go",".rb",".sh",".json",".yaml",".yml"]
}

#function to define the category of a file based on it's extension
def get_category(ext):
    for category, extensions in EXT.items():
        if ext.lower() in extensions:
            return category
    return "others"

#main function which sorts and moves files into designated folders
def organize_folder(folder_path):
    #checking if the folder exists
    if not os.path.isdir(folder_path):
        print("⚠️Folder Not Found. Try Again with a valid path.")
        return
    
    #loop through files in the folder to sort based on their extensions
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path,filename)

        #check whether the new file path is a directory or not, if it is another directory, skip
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)

            #creating folder for the category if it doesn't exist
            category_path = os.path.join(folder_path, category)
            os.makedirs(category_path, exist_ok=True)

            try:
                shutil.move(file_path, os.path.join(category_path,filename))
                print(f"✅ File moved: {filename} -> {category}/")
            except Exception as e:
                print(f"⚠️ File {filename} could not be moved: {e}")

#main function which is called when the script is run
if __name__ == "__main__":
    target_folder = "" #Add your file path here
    organize_folder(target_folder)