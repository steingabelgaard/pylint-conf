set conf=C:\Users\HansHenrik\git\pylint-conf\conf\travis_run
cd %2
pylint --load-plugins=pylint_odoo --rcfile=%conf%_pylint_pr.cfg %2\%1
flake8 --config=%conf%_flake8__init__.cfg %2\%1
flake8 --config=%conf%_flake8.cfg %2\%1