# A Simple Python Clock

This is a simple Python clock application. This project displays the current time, day of the week, and date on a graphical user interface.

<img src="clock.png" alt="PiaClock Screenshot" width="400">

## Features
- Displays the current time in the 12-hour format with seconds and AM/PM.
- Shows the current day of the week.
- Presents the date in the format "Month Day Year."
- A pink color theme, personalized to my preference.

## Installation
This application can be run as an executable file named **PiaClock.exe**. By simply double-clicking this file to launch the clock.

## How It Works
- **Tkinter**: The graphical user interface is created using the Tkinter library.
- **Time Module**: The clock updates every second, utilizing the `time` module to fetch the current time, day, and date.
- **Recursion**: The clock uses a recursive function to continuously update the time, ensuring it stays accurate.

## Building the Executable

To build the PiaClock executable, the PyInstaller tool was used with the following command:

```plaintext
pyinstaller -F -w -i PiaClock.ico clock.py

## Project Files
- `clock.py`: The source code for the PiaClock application.
- `PiaClock.exe`: An executable file created using PyInstaller.
- `clock.png`: A screenshot of the PiaClock application.
- `PiaClock.ico`: The application icon file used.

This project is a personal creation and exercise. :)


