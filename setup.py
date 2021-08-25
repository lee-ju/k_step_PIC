from setuptools import setup

setup(
    name='k_step_pic',
    version='0.0.3',
    description='k-step-PIC: for Prior Art Search',
    url='https://github.com/lee-ju/k_step_PIC.git',
    author='Juhyun Lee',
    author_email='leeju@korea.ac.kr',
    license='Juhyun Lee',
    packages=['k_step_pic'],
    zip_safe=False,
    install_requires=[
	'pandas',
	'datetime',
	'networkx',
    ]
)
