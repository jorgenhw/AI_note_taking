# install requirements.txt for project
# Usage: source setup.sh

# create virtual environment
python3 -m venv note_taking_program_venv

# activate virtual environment
source ./note_taking_program_venv/bin/activate

# Install requirements
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

# INFO message
echo "Successfully installed requirements.txt"

# run the code
python3 main.py # run the code with default parameters

# Extra: Type ```python3 main.py --help``` to see the help message for the adjustable parameters

# Deactivate virtual environment
deactivate