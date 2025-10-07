## Clipboard Bullet Point Script
### Overview
This Python script allows you to quickly convert text from your clipboard into a bulleted list. Each line of the copied text will be prefixed with a `*` , and the result will automatically be copied back to your clipboard for easy pasting elsewhere. Blank lines are preserved.

### Features:
- Adds `*` (bullet) to the beginning of each line with text.
- Preserves empty lines for clean formatting.
- Works directly with your system clipboard—no file input/output needed.
- Lightweight and easy to use.

### How It Works:
1. Retrieves text from the clipboard.
2. Splits the text into individual lines.
3. Loops through each line:
    - Adds `*` only if the line is not empty.
4. Joins all lines back into a single string.
5. Copies the modified text back to the clipboard.

### Notes:
- Empty lines are preserved.
- Works on Windows, macOS, and Linux.
- Ideal for formatting lists quickly for emails, documents, or notes.
