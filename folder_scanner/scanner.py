import os
import pathspec


def scan_directory(core_folder, ignore_patterns, chunk_size=512):
    # Compile ignore patterns using pathspec
    spec = pathspec.PathSpec.from_lines('gitwildmatch', ignore_patterns)

    for root, dirs, files in os.walk(core_folder, topdown=True):
        # Modify dirs in-place to apply ignore patterns to directories
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.join(root, d))]

        for file in files:
            file_path = os.path.join(root, file)
            if spec.match_file(file_path):
                continue  # Ignore files based on the ignore pattern

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Yield chunks of the file
                for i in range(0, len(content), chunk_size):
                    yield {"filepath": file_path, "chunk": i // chunk_size + 1, "content": content[i:i + chunk_size]}
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

'''
def main():
    core_folder = '/path/to/your/projects'
    ignore_patterns = [
        '.git', '.dockerignore', '*.log', 'tmp/*'
    ]
    for file_chunk in scan_directory(core_folder, ignore_patterns):
        print(file_chunk)


if __name__ == '__main__':
    main()
'''