import os
class FileFilter():
    def __init__(self):
        self.accepted_extensions = ('.jpg', '.jpeg', '.gif', '.bmp')
    def __call__(self, filename):
        base, ext = os.path.splitext(filename)
        return ext in self.accepted_extensions
files = [
    'me.txt',
    'friend.jpg',
    'you.jpeg',
    'he.xml']

def main():
    file_filter = FileFilter()
    print(list(filter(file_filter, files)))

if __name__ == "__main__":
    main()