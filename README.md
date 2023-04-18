# Django Test
## Python Version 3.10
## CLI Commands
``` bash
# run following commands in terminal in backend_test directory 
# after cloning.

pip install pipenv
pipenv install
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
# this command could take some time to run
python manage.py create_employees
```

``` bash
# if below command ran without any errors, 
# it means you have installed this project successfully.
python manage.py runserver
```

## Task
``` bash
1. Make a relationship between companies and employees.
2. In home page there is a table with company names and an empty link along with each company. 
   clinking on that link, should open up a page to a form with a dropdwon of employees that when choosed 
   should associate that employee with that particular company and redrirect to the table.
3. All employee names associated with a company should be displayed comma separated on the second column of the table on the home page.
4. Each employee can only be associated with one company only.
5. Employee dropdown in the form should be searchable.

```