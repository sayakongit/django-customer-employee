echo "BUILD START"
mkdir staticfiles_build
pip install -r requirements.txt
python manage.py collectstatic --noinput
echo "BUILD END"