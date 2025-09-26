import os
import shutil

#This tool only organizes files of extensions: .txt, .docx, .pdf, .jpg, .png, .mp4

folder = input("Enter folder path: ")

folder_lists = os.listdir(folder)


for file in folder_lists :
    source_path = os.path.join(folder, file)
    if os.path.isfile(source_path):
        file_path = os.path.splitext(file)

        if(file_path[1] == ".txt"):
            destination_path = os.path.join(folder, "Text Documents")
            if (not os.path.exists(destination_path)):
                os.makedirs(destination_path)
            shutil.move(source_path, destination_path)
            print("Moved the file(s)")

        elif(file_path[1] == ".docx") :
            destination_path = os.path.join(folder, "Word Documents")
            if( not os.path.exists(destination_path)):
                os.makedirs(destination_path)
            shutil.move(source_path, destination_path)
            print("Moved the file(s)")

        elif(file_path[1] == ".pdf") :
            destination_path = os.path.join(folder, "PDF Documents")
            if( not os.path.exists(destination_path)) :
                os.makedirs(destination_path)
            shutil.move(source_path, destination_path)
            print("Moved the file(s)")

        elif(file_path[1] == ".jpg" or file_path[1] == ".png") :
            destination_path = os.path.join(folder, "Images")
            if( not os.path.exists(destination_path)) :
                os.makedirs(destination_path)
            shutil.move(source_path, destination_path)
            print("Moved the file(s)")

        elif(file_path[1] == ".mp4") :
            destination_path = os.path.join(folder, "Videos")
            if( not os.path.exists(destination_path)) :
                os.makedirs(destination_path)
            shutil.move(source_path, destination_path)
            print("Moved the file(s)")


