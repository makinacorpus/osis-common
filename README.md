
# Osis-Common
Common functionnalities for osis and osis-portal.

## Installation with pip
If you just want to use this library in osis or osis-portal.
In this way , the package cannot be modified.
The package is made with the last stable version of the app.

1. `(VENV)$ pip3 install git+ssh://git@github.com/uclouvain/osis-common.git@package#egg=osis-common`
2. Add osis-common to the INSTALLED_APPS of the django settings

    INSTALLED_APPS = [
        ...
        'osis_common',
    ]

3. Run `python manage.py migrate` to create the common models.

4. Start the development server and visit http://127.0.0.1:8000

## Installation as git submodule
If you want to install the package in the projet tree folder, or if you want to develop this package.

1. Clone either osis or osis-portal project , on master branch
  `git clone git@github.com:uclouvain/osis.git -b master --single-branch`

2. Add osis-common as submodule of the previous cloned project
  ```
  cd /path/to/osis
  git submodule add git@github.com:uclouvain/osis-common.git ./osis_common
  ```
3. Add osis-common to the INSTALLED_APPS of the django settings

    INSTALLED_APPS = [
        ...
        'osis_common',
    ]
4. go to the submodule and checkout de branch you want
5. Make modifications, and make a pull request of the submodule if you want
6. Write tests in the tests folder of the submodule
7. Make migrations if necessary
8. Test the submodule
  ```
  cd /path/to/osis
  (VENV)$ python3 manage.py test
  ```
9. Start the development server and visit http://127.0.0.1:8000
