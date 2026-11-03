
import csv
import os

folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "hubs.csv")
report_file = os.path.join(folder, "report.txt")

print("Looking for CSV file:", csv_file)
print("Does the file exist?", os.path.exists(csv_file))

try:
    with open(csv_file, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        print("CSV headings:", reader.fieldnames)
        rows = list(reader)

    print("Number of learners found:", len(rows))
    print("Learner records:", rows)

except FileNotFoundError:
    print("ERROR: hubs.csv not found")
    rows = []

total = 0
passed = 0
failed = 0
passed_learners = []
failed_learners = []

for row in rows:
    name = row["name"].strip()
    hub = row["hub"].strip()
    score = int(row["score"])

    total += score

    if score >= 50:
        passed += 1
        passed_learners.append((name, hub, score))
    else:
        failed += 1
        failed_learners.append((name, hub, score))

average = round(total / len(rows), 1) if rows else 0

with open(report_file, "w", encoding="utf-8") as f:
    f.write("LEARNER REPORT\n")
    f.write("--------------------\n")
    f.write(f"Total learners: {len(rows)}\n")
    f.write(f"Passed: {passed}\n")
    f.write(f"Failed: {failed}\n")
    f.write(f"Average score: {average}\n")

    f.write("\nLEARNERS WHO PASSED:\n")
    for name, hub, score in passed_learners:
        f.write(f"{name} | {hub} | {score}\n")

    f.write("\nLEARNERS WHO FAILED:\n")
    for name, hub, score in failed_learners:
        f.write(f"{name} | {hub} | {score}\n")

print("Report written to report.txt")




