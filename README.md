## mac/linux

python --version # ensure it is 3.x
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

## windows

python --version # ensure it is 3.x
python -m venv venv
./venv/bin/Activate
pip install -r requirements.txt
uvicorn main:app --reload
