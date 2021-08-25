from setuptools import setup

setup(
    name='k-step-pic',
    version='0.0.1',
    description='k-step-PIC: for Prior Art Search',
    url='https://github.com/lee-ju/k-step-PIC.git',
    author='Juhyun Lee',
    author_email='leeju@korea.ac.kr',
    license='Juhyun Lee',
    packages=['k-step-pic'],
    zip_safe=False,
    install_requires=[
	'pandas',
	'datetime',
	'networkx',
    ]
)
