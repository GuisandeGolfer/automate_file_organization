# %%
import os
import shutil
from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# %%
source_dir = "/Users/diegoguisande/Downloads"
dest_dir_onedrive_documents = "/Users/diegoguisande/Desktop/for_onedrive"
dest_dir_images = "/Users/diegoguisande/Desktop/download_images_and_screenshots" 
dest_dir_videos = "/Users/diegoguisande/Desktop/downloaded_videos"
dest_dir_documents = "/Users/diegoguisande/Desktop/downloaded_documents"
# %%
video_extensions = [ ".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
document_extensions = [ ".doc", ".docx", ".odt",".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
berkeley_extensions = ["UC", "Berkeley", "status","report", "kickoff", "meeting", "meetings"]
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# %%
class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_video_files(entry)
                self.check_image_files(entry)
                self.check_document_files(entry)
                self.check_customer_files(entry)

    def check_customer_files(self, entry):
        for keyword in berkeley_extensions:
            if os.path.exists(entry):
                if entry.name.__contains__(keyword.lower()) or entry.name.__contains__(keyword.upper()):
                    shutil.move(entry.path, dest_dir_onedrive_documents)
                    logging.info(f"Moved Customer File: {entry.name}") 

    def check_document_files(self, entry):
        for extension in document_extensions:
            if os.path.exists(entry):
                if entry.name.endswith(extension) or entry.name.endswith(extension.upper()):
                    shutil.move(entry.path, dest_dir_documents)
                    logging.info(f"Moved Document file: {entry.name}")

    def check_image_files(self, entry):
        for extension in image_extensions:
            if os.path.exists(entry):
                if entry.name.endswith(extension) or entry.name.endswith(extension.upper()): 
                    shutil.move(entry.path, dest_dir_images) 
                    logging.info(f"Moved Image file: {entry.name}")

    def check_video_files(self, entry):
        for extension in video_extensions:
            if os.path.exists(entry):
                if entry.name.endswith(extension) or entry.name.endswith(extension.upper()): 
                    shutil.move(entry.path, dest_dir_videos)
                    logging.info(f"Moved Video file: {entry.name}")

# %%
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
# %%