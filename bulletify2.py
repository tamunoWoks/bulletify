import pyperclip

# Get text from clipboard
text = pyperclip.paste()

# Separate lines
lines = text.split('\n')

# Loop through all indexes in the "lines" list
for i in range(len(lines)):
    # Add a star only if the line is not empty
    if lines[i].strip() != '':
        lines[i] = '* ' + lines[i]

# Join the lines back into a single string
text = '\n'.join(lines)

# Copy the result back to the clipboard
pyperclip.copy(text)

