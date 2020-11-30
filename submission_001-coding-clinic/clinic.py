import sys
import os
import sync
from commands import help_page
from contextlib import contextmanager
import subprocess


def verify_token():
    if os.path.exists('token.pickle'):
        return True
    
    print("Please login!!")
    sys.exit()


@contextmanager      # Suppress system output
def suppress_output():
    """
    - supress the function output
    - usage : with suppress_output():
    """
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout



if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == '-o':
        sync.open_events()
    
    elif len(sys.argv) > 1 and sys.argv[1] == '-v':
        sync.view_events()

    else:
        print(help_page.help_sheet())
        sys.exit()

    
    

    pass
