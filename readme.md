# Talk to your codebase (Codebase Concatenator)
Codebase Concatenator is a simple Python script that helps to concatenate a codebase into a single text file. The main goal of this tool is to create a structured summary of a codebase that can be used as input for a large language model. It facilitates interactive exploration, understanding, modification, and maintenance of the codebase through conversation with the language model.

# Features
* Hierarchical Overview: Provides a hierarchical list of directories and files at the beginning of the output.
* Directory and File Tags: Encapsulates directories and files with BEGIN and END tags for clear delineation.
* Configurable Exclusions: Allows exclusion of specific file patterns.
* Focus on Specific Folders: Allows configuration to focus on specific directories or repositories within the codebase.

# Usage
1. Configuration: Open the concatenate_files.py script and set the following configuration variables at the beginning of the file:
* root_folder: Path to the root folder of the codebase.
* output_file: Name of the output text file.
* separator_pattern: Separator pattern to be used between sections.
* include_folders: List of folders to include (e.g., ['folder1', 'folder2']).
* exclude_patterns: List of patterns to exclude (e.g., ['.exe', '.dll']).
2. Execution: Run the script by executing the following command in your terminal:

```bash
python concatenate_files.py
```

3. Output: The concatenated codebase will be saved in the specified output file. You can use this file as input for a large language model to chat, understand, modify, and better maintain the codebase.

4. Present it to the large language model with the following prompt
```
Hello Large Language Model,

I have a concatenated output from multiple repositories of a codebase, and I want you to assist me in understanding and navigating through it. Here's how the file is structured:

1. Hierarchical Paths: At the beginning of the file, there's a section that lists the hierarchical paths of all included directories and files.
2. Main Separator: The main separator used between different sections is YOUR_SEPARATOR_PATTERN.
3. Directories: For each directory in the codebase, there's a BEGIN and END tag.
4. Files: Inside each directory section, individual files are encapsulated with BEGIN and END tags.
5. Exclusions: Some files and folders were excluded based on specific patterns.
6. Focus: The primary directories of interest are listed in the include_folders configuration.

With this structure in mind, please assist me in understanding, querying, and potentially modifying the content. Let's start by giving me an overview or any patterns you notice.
```

* Interact and Explore:
Continue the conversation with the model, asking questions, requesting explanations, and exploring the codebase. The model's responses can help you understand various aspects of the codebase, make modifications, and perform maintenance tasks.

* Iterative Development:
You can make changes to the codebase and regenerate the concatenated file as needed. The model can assist you in this iterative development process, providing insights and guidance along the way.