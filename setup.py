from setuptools import setup, find_packages


setup(
    name='rapidsms-decisiontree-app',
    version=__import__('decisiontree').__version__,
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(),
    include_package_data=True,
    url='http://github.com/caktus/rapidsms-decisiontree-app/',
    license='BSD',
    description='RapidSMS Decisiontree',
    long_description=open('README.rst').read(),
    classifiers=(
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ),
    zip_safe=False,
)
