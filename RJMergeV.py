import os, subprocess, shlex

BASE_DIRECTORY = "/mnt/multimedia/Other/~Miscellaneous/VR/09/Multipart/"
TARGET_DIRECTORY = f"{BASE_DIRECTORY}Output/"
TEMP_DIRECTORY = "./~Temp/"
BASE_EXTENSION = ".mp4"

if __name__ == "__main__":

    os.system("clear")

    if not os.path.exists(BASE_DIRECTORY):
        print (f"{BASE_DIRECTORY} does not exist.  Terminating.")
        exit()

    if not os.path.exists(TARGET_DIRECTORY):
        print (f"{TARGET_DIRECTORY} does not exist.  Creating.")
        os.makedirs(TARGET_DIRECTORY, exist_ok=True)

    if not os.path.exists(TEMP_DIRECTORY):
        print (f"{TEMP_DIRECTORY} does not exist.  Creating.")
        os.makedirs(TEMP_DIRECTORY, exist_ok=True)

    unique_files = set()
    files = os.listdir(BASE_DIRECTORY)
    files.sort()

    for file in files:
        if os.path.isfile(os.path.join(BASE_DIRECTORY, file)):
            if file.endswith(BASE_EXTENSION):   
                filename_without_extension, _ = os.path.splitext(file)
                output_filename = filename_without_extension[:-1]
                unique_files.add(output_filename)
 
    for unique_file in unique_files:
        print (unique_file)
        merged_video_name = unique_file + BASE_EXTENSION
        input_file = open(TEMP_DIRECTORY + unique_file + ".lst", "w")

        print (len(files))
        exit()
        for file in files:
            if (os.path.isfile(os.path.join(BASE_DIRECTORY, file)) and \
                file.startswith(unique_file) and \
                file.endswith(BASE_EXTENSION)):
                    input_file.write(f"file '{BASE_DIRECTORY}{file}'\r\n")
                    print (f"- {file}")

        input_file.close()

        #ffmpeg_command = f"ffmpeg -f concat -safe 0 -i {input_file.name} -c copy {TARGET_DIRECTORY}{merged_video_name} -y"
        print (f"*   {ffmpeg_command}")
        
        result = subprocess.run(shlex.split(ffmpeg_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        result_file = open(TEMP_DIRECTORY + unique_file + ".log", "w")
        result_file.write(f"{result}\r\n")
        result_file.close()
        
        print (result.returncode)

