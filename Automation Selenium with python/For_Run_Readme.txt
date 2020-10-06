It is a script for automation checking of UI interface:
---------------------------------------------------------

Use: Selenium Webdriver, Python, PyCharm

Installation and Run: 

Steps:
------- 
Step 1: Install python and pycharm editor 
Step 2. Add environment variable:

Here an example for windows:
Default Path of installation of Python_3.6.4:
C:\Users\sharmin\AppData\Local\Programs\Python\Python33
Win->System->Advanced System Settings->Environment Variable->System variable->Select Path->click Edit
Copy path to advanced system


Step 3. Install selenium Webdriver
Upgrade pip
Upgrade pip : https://datatofish.com/upgrade-pip/ 
python -m pip install --upgrade pip
pip –version

Step 4. Create virtual environment 
Pycharm usually created this automatically before run, if not. it can be created by this way:

Created folder manually < envs\Selenium3> : C:\Users\sharmin\envs\Selenium3
-pip install virtualenv
-Virtual environment creation command (virtualenv <folder name>): 
-virtualenv C:\Users\sharmin\envs\Selenium3
-After this command, below folder will be created

-Go to Scripts folder and then activate virtual environment
-cd Scripts
-activate
-Virtual environment Activate Command: C:\Users\sharmin\envs\Selenium3\Scripts\activate
-Deactivate Command: deactivate
If deactivate doesn’t work then need to install selenium

Step 5:
Downloading python bindings for Selenium
Using pip, you can install selenium like this:

Go to Cmd > pip install selenium

for details: check here
https://selenium-python.readthedocs.io/installation.html

Step 6:
Creating folder and Driver:
-Create a folder named ‘webdrivers’ in C:\webdrivers (or where you want to create the work space)
-Download geckodriver (win64 bit) and chromedriver (as per version no) in C:\webdrivers
https://github.com/mozilla/geckodriver/releases (geckodriver-v0.24.0-win64.zip)
http://chromedriver.chromium.org/downloads 
-Unzip those zip files
-Copy below exe files in C:\webdrivers
-Chromedriver.exe and geckodriver.exe
-Delete zip and non folders. Keep only 2 exe files.

Step 7:
Add Environment:
-Now add environment variable in path “C:\webdrivers”
-Click on edit of system variable
Click on new in recent editor
-Add “C:\webdrivers” at the below
Click ok.. ok.. ok..

RUN:
----
Open the Selenium File at PyCharm
Run the file at (Chrome) Browser





