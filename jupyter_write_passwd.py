from notebook.auth import passwd

from pathlib import Path
import os
import json

def main():
    path = Path.home() / '.jupyter'
    if not path.exists():
        path.mkdir()
    path = path / 'jupyter_notebook_config.json'
    
    pw = os.environ.get('NOTEBOOK_PW')
    loc = os.environ.get('NOTEBOOK_LOCATION')
    sha1 = passwd(pw)

    with open(path, 'w') as f:
        config = {"NotebookApp": {"password": sha1}}
        config["NotebookApp"]['base_url'] = '/' + loc
        f.write(json.dumps(config))

if __name__ == '__main__':
    main()