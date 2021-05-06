#! python3

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:    py.exe mcp.pyw save <keyword> Saves clipboard.
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard.py
#           py.exe mcb.pyw list - Loads all keywords to clipboard
# Deps:     pyperclip

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()

