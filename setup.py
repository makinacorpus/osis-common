import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='osis-common',
    version='0.3',
    packages=find_packages(),
    include_package_data=True,
    license='GNU v3',
    description='Common package for all osis projects',
    long_description=README,
    url='https://github.com/uclouvain/osis-common',
    author='uclouvain',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
          'Django>=1.9',
          'reportlab>=3.2.0',
          'django-ckeditor==5.0.3',
          'XlsxWriter==0.9.3'
    ],
)
