python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate.bat  # Windows

pip install django djangorestframework

For testing:
pip install coverage
coverage run --source='.' manage.py test
coverage report
