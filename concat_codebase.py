import os

# Configuration Variables
root_folder = 'YOUR_ROOT_FOLDER_PATH'
output_file = 'YOUR_OUTPUT_FILE_NAME.txt'
separator_pattern = 'YOUR_SEPARATOR_PATTERN'
include_folders = ['FOLDER1', 'FOLDER2'] # List of folders to include
exclude_patterns = ['PATTERN1', 'PATTERN2', 'PATTERN3'] # Add or remove patterns as needed

def concatenate_files(root_folder, output_file, separator_pattern, include_folders):
    distinct_extensions = set()
    hierarchical_paths = []

    for root, dirs, files in os.walk(root_folder):
        # Check if the current root is within one of the include_folders
        if not any(os.path.join(root_folder, folder) in root for folder in include_folders):
            continue
        
        # Exclude specified subfolders
        dirs[:] = [d for d in dirs if not any(pattern in d for pattern in exclude_patterns)]

        # Add directory path
        relative_dir = os.path.relpath(root, root_folder)
        hierarchical_paths.append(relative_dir)

        for file_name in files:
            if any(pattern in file_name for pattern in exclude_patterns):
                continue
            file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_path, root_folder)
            # Add file path
            hierarchical_paths.append(f"  {relative_path}")

    with open(output_file, 'w', encoding='utf-8') as out_file:
        # Write hierarchical paths at the beginning
        out_file.write("Hierarchical Paths:\n")
        out_file.write('\n'.join(hierarchical_paths) + '\n')
        out_file.write(separator_pattern + '\n')

        # Now, repeat the os.walk to write the content
        for root, dirs, files in os.walk(root_folder):
            # Check if the current root is within one of the include_folders
            if not any(os.path.join(root_folder, folder) in root for folder in include_folders):
                continue
            
            # Exclude specified subfolders
            dirs[:] = [d for d in dirs if not any(pattern in d for pattern in exclude_patterns)]
            
            # Write BEGIN tag for the directory
            relative_dir = os.path.relpath(root, root_folder)
            out_file.write(f"--- BEGIN DIRECTORY: {relative_dir} ---\n")
            
            for file_name in files:
                if any(pattern in file_name for pattern in exclude_patterns):
                    continue
                file_extension = os.path.splitext(file_name)[1]
                distinct_extensions.add(file_extension)
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, root_folder)

                # Write BEGIN and END tags for each file
                out_file.write(separator_pattern + '\n')
                out_file.write(f"--- BEGIN FILE: {relative_path} ---\n")
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as in_file:
                    content = in_file.read()
                    out_file.write(content + '\n')
                out_file.write(f"--- END FILE: {relative_path} ---\n")
                out_file.write(separator_pattern + '\n')

            # Write END tag for the directory
            out_file.write(f"--- END DIRECTORY: {relative_dir} ---\n")

    print("Distinct file extensions written:", distinct_extensions)

concatenate_files(root_folder, output_file, separator_pattern, include_folders)
