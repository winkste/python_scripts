# This cheat sheet shows the interactive mode similar
# to Jupyter, but on native python scripts. The link
# below demonstrates this in a youtube video
# https://www.youtube.com/watch?v=lwN4-W1WR84&t=34s
# Note: The jupyter library has to be installed!
# %%
print('Hello World!')

# %%
print('This is the interactive mode in VSCode')
# %%
%pylab inline
# %%
plot([0,1,2], [0,1,4])
# %%
import pandas as pd
pd.DataFrame({'one':1, 'two':2}, {'one':11, 'two': 22})
# %%
# Command	Keyboard shortcut
print('Go to Next Cell:                 Ctrl+Alt+]')
print('Go to Previous Cell:             Ctrl+Alt+[')

print('Extend Selection by Cell Above:  Ctrl+Shift+Alt+[')
print('Extend Selection by Cell Below:	Ctrl+Shift+Alt+]')
print('Move Selected Cells Up:	        Ctrl+; U')
print('Move Selected Cells Down:        Ctrl+; D')
print('Insert Cell Above:	            Ctrl+; A')
print('Insert Cell Below:	            Ctrl+; B')
print('Insert Cell Below Position:	    Ctrl+; S')
print('Delete Selected Cells:	        Ctrl+; X')
print('Change Cell to Code:	            Ctrl+; C')
print('Change Cell to Markdown:	        Ctrl+; M}')

# %%
