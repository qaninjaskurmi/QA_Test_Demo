It is a file for data inserting script by using Python,

To run this:

Steps:
------
1. Install Python version 3.6.4
2. Install JetBrains PyCharm version 2019.2.3
3. Open the script on the PyCharm or Drag and drop the Python script file on the pycharm
4. Run the script

CSV file:
---------
Here I have created some sample data in CSV file, where it has 4 collumns:

Assuming the csv file with 
- Account numbers in column 0
- The Ammount in column 1
- Currency in Column 3
- Date and time in Column 4

N.B: Setting and taking date and hour in format by following the column no of CSV file, table in DB, Time stamp also

Date format in Excell : yyyy-mm-dd hh:mm:ss by using custom format and save it as CSV
as CSV file is saving its default format, where hour, min and sec is not showing and also showing in different format

CSV file's data format check before running:
--------------------------------------------
Before run the script, Do not open the CSV file with excel, it will clear the date format by converting as it's default, then the script will not work 
For opening the CSV file please open it by Notepad or any text editor or use the import feature from excel, Import CSV at Excel file.
Incase the CSV file format changed anyhow, you can open the excel file and saved it as CSV file and replaced with older CSV file

statements_result.csv
----------------------
- Column 5 saving the created timestamp, Column 6 is showing the Status Code of API, Column 7 is showing response time of API

Thus how API is showing also the result in automated way.

Note: Here also open the CSB file by using Notepad or any text editor.