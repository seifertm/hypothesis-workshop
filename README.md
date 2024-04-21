# Hypothesis workshop
This repository includes the theoretical and practical material for the Hypothesis workshop.

## Setup
You're encouraged to set up the exercise material ahead of the workshop according to the following setup instructions.
When running pytest, you should see a number of skipped tests.

### Unix/MacOS (Bash)
```sh
git clone https://github.com/seifertm/hypothesis-workshop
cd hypothesis-workshop/exercises
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt -c constraints.txt
pytest
````

### Windows (PowerShell)
```powershell
git clone https://github.com/seifertm/hypothesis-workshop
cd hypothesis-workshop\exercises
python -m venv venv
venv\Scripts\activate.ps1
pip install -r requirements.txt -c constraints.txt
pytest
```
