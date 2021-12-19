import os

dir_content = os.listdir()

files = [el for el in dir_content if "." in el]
report = {}

for file in files:
    file_names, ext = file.split(".")
    if ext not in report:
        report[ext] = []
    report[ext].append(file_names)

result_str = ""
for ext, file_names in sorted(report.items()):
    result_str += f".{ext}\n"
    for name in file_names:
        result_str += f"- - - {name}.{ext}\n"

desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
final_path = desktop + os.path.sep + "report.txt"
with open(final_path, "w") as file:
    file.write(result_str)