# Python Week 7 – File Handling and CSV Learner Report

## 1. Project Overview

This project demonstrates my understanding of Python file handling and CSV processing.

It contains two main activities:

1. Reading learner information from a CSV file, calculating scores, identifying learners who passed or failed, and generating a report.
2. Creating a text file, writing notes, appending additional information, reading the file, and counting the total number of lines.

## 2. Project Objectives

The main objectives of this project are to:

- Understand how to import and use Python libraries.
- Read data from CSV files.
- Understand file paths and file locations.
- Use exception handling to manage missing files.
- Convert text values into integers.
- Use loops and conditional statements.
- Calculate totals and average scores.
- Identify learners who passed or failed.
- Create and write information into text files.
- Understand the difference between read, write, and append modes.
- Read text files line by line.
- Count the number of lines in a file.

## 3. Project Files

The project contains the following files:

| File | Description |
|---|---|
| `report_builder.py` | Main Python program containing both activities. |
| `hubs.csv` | Stores learner names, hubs, and scores. |
| `report.txt` | Contains the generated learner performance report. |
| `my_notes.txt` | Stores notes written and appended by the program. |
| `README.md` | Explains the project and its functionality. |

## 4. Activity One: CSV Learner Report

### Description

The first activity reads learner information from `hubs.csv` and generates a performance report in `report.txt`.

### CSV Input Data

The `hubs.csv` file contains three columns:

- `name`: The learner's name.
- `hub`: The learner's learning hub.
- `score`: The learner's examination score.

Example:

```csv
name,hub,score
Amina,ASAL,82
Brian,NENAP,45
Fatuma,ASAL,90
Kevin,TCDM,61
Halima,NENAP,38
```

### Main Operations

**1. Importing libraries**

- `csv` is used to read CSV files.
- `os` is used to manage file paths and check whether files exist.

**2. Finding file locations**

The program uses `os.path.abspath()`, `os.path.dirname()`, and `os.path.join()` to locate the CSV file and report file.

**3. Checking file existence**

`os.path.exists()` checks whether `hubs.csv` exists in the project folder.

**4. Reading CSV data**

`csv.DictReader()` reads the CSV records using column headings. The data is stored in a list called `rows`.

**5. Exception handling**

`try` and `except FileNotFoundError` handle situations where the CSV file cannot be found.

**6. Creating variables**

- `total` stores all learner scores added together.
- `passed` counts learners who passed.
- `failed` counts learners who failed.
- `passed_learners` stores passed learner records.
- `failed_learners` stores failed learner records.

**7. Processing learner records**

A `for` loop processes each learner. The program retrieves the learner's name, hub, and score.

`int()` converts the score from text into a whole number, while `.strip()` removes unnecessary spaces.

**8. Calculating total scores**

`total += score` adds each learner's score to the overall total.

**9. Identifying passed and failed learners**

The program uses an `if-else` condition:

- A score of 50 or above is a pass.
- A score below 50 is a fail.

The `.append()` method stores each learner's information in the appropriate list.

**10. Calculating the average**

The program divides the total score by the number of learners. `round()` rounds the result to one decimal place.

**11. Generating the report**

The program uses `open()` in write mode and `f.write()` to create `report.txt`.

It includes the total learners, passed learners, failed learners, average score, and individual learner details.

### Expected Report Output

```text
LEARNER REPORT
--------------------
Total learners: 5
Passed: 3
Failed: 2
Average score: 63.2

LEARNERS WHO PASSED:
Amina | ASAL | 82
Fatuma | ASAL | 90
Kevin | TCDM | 61

LEARNERS WHO FAILED:
Brian | NENAP | 45
Halima | NENAP | 38
```

## 5. Activity Two: Writing and Reading Text Files

### Description

The second activity demonstrates how to create a text file, write notes, append additional information, read the file, and count the total lines.

### Main Operations

**1. Creating a text file**

The program uses:

`open("my_notes.txt", "w")`

This creates a file called `my_notes.txt` and writes three notes into it.

**2. Writing information**

The `write()` method adds text to the file. The `\n` character moves each new note to another line.

**3. Appending information**

The program uses:

`open("my_notes.txt", "a")`

Append mode adds a fourth note without deleting the first three notes.

**4. Reading information**

The program uses:

`open("my_notes.txt", "r")`

Read mode allows Python to read the contents of the file.

**5. Reading line by line**

A `for` loop displays each line. The `.rstrip()` method removes unwanted newline characters.

**6. Counting lines**

`readlines()` reads all the lines into a list.

`len(lines)` counts the total number of lines.

### Expected Notes Output

```text
--- My notes ---
Python is fun
Files are useful
Week 7 is going well
I added this later
```

Expected terminal result:

```text
Total lines: 5
```

The total is five because the file contains one heading and four notes.

## 6. Python Concepts Used

| Python concept | Purpose |
|---|---|
| `import` | Imports libraries. |
| `csv` | Works with CSV data. |
| `os` | Manages file paths. |
| `open()` | Opens files. |
| `with` | Manages files and closes them automatically. |
| `try-except` | Handles errors. |
| `for` | Repeats operations over records or lines. |
| `if-else` | Makes decisions based on conditions. |
| `int()` | Converts values into integers. |
| `round()` | Rounds numerical results. |
| `len()` | Counts items or lines. |
| `append()` | Adds items to a list. |
| `write()` | Writes information into a file. |
| `readlines()` | Reads all file lines into a list. |
| `rstrip()` | Removes trailing whitespace and newline characters. |
| `f-string` | Inserts variable values into strings. |

## 7. How to Run the Project

1. Open the `python week7` folder in Visual Studio Code.
2. Make sure `report_builder.py` and `hubs.csv` are in the same folder.
3. Save all your files.
4. Open the VS Code terminal.
5. Run the following command:

```powershell
python report_builder.py
```

6. Open `report.txt` to view the learner report.
7. Open `my_notes.txt` to view the saved notes.

## 8. Expected Project Results

After running the program successfully:

