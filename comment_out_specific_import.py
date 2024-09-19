import os

def comment_out_specific_import(file_path, specific_import):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        try:
            with open(file_path, "r", encoding="latin-1") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Skipping file due to encoding issues: {file_path} - {e}")
            return

    modified = False
    new_lines = []
    
    # Print each line to debug
    print("Reading lines from the file:")
    for line in lines:
        print(line.strip())  # Print the line without leading/trailing whitespace
        if specific_import in line and 'import' in line:
            new_lines.append("# " + line)  # Comment out the specific import
            modified = True
            print(f"Commented out import in {file_path}")
        else:
            new_lines.append(line)
    
    if modified:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print(f"Successfully updated file: {file_path}")
        except Exception as e:
            print(f"Failed to write to file: {file_path} - {e}")
    else:
        print(f"No matching import statement found in {file_path}")

# Define the specific file to be modified
file_path = r"C:\Users\wmi\Desktop\django-lms-main\school\Lib\site-packages\django\utils\encoding.py"

# Define the specific import to be commented out
specific_import = "python_2_unicode_compatible"

# Run the function
comment_out_specific_import(file_path, specific_import)
print("Finished processing the file.")
