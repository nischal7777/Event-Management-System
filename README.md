# Event Management System
<br>

## Development Environment Setup

### For Windows
```ps1
# install virtual environment
pip install virtualenv

# clone the project
git clone https://github.com/AngelDhakal/Event-Management-System.git

# create virtual environment
cd Event-Management-System
virtualenv venv

# activate virtual environment
.\venv\Scripts\activate

# install required dependencies
pip install -r requirements.txt

# run django application
python manage.py runserver

# go to http://localhost:8000 in you browser
```
<br>

### For Linux
```bash
# Install virtualenv
sudo apt install python3-venv

# clone the project
git clone https://github.com/AngelDhakal/Event-Management-System.git

# create virtual environment
cd Event-Management-System
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run django application
python manage.py runserver

# go to http://localhost:8000 in you browser

```
