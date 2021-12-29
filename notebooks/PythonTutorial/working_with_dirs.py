from pathlib import Path

# absolute apth - a path starting from the root of the hadrdisk
# relative path - a path starting from the current directiry

path = Path()

for file in path.glob('*.py'):  # iterate over all files
    print(file.name)
