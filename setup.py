from setuptools import setup

setup(
   name='mtracker',
   version='1.0',
   description='Provides a decorator for memory usage tracking. The part of FOSS course.',
   license='MIT',
   author='Timofeev Evgeniy',
   author_email='geka.timof@mail.ru',
   url='https://github.com/GekaTimof/mtracker',
   packages=['mtracker'],
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)