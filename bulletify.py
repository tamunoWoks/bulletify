import pyperclip

# Get text from clipboard
text = pyperclip.paste()

# Add a star to lines with text, keep empty lines as they are
lines = ['* ' + line if line.strip() != '' else '' for line in text.split('\n')]

# Join the lines back into a single string
text = '\n'.join(lines)

# Copy the result back to the clipboard
pyperclip.copy(text)

