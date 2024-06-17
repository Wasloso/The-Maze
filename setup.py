from setuptools import setup, find_packages

setup(
    name='themaze',
    version='0.0.1',
    description='A(maze)ing game TheMaze',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Partyk Łuszczek & Tymoteusz Lango',
    url='https://github.com/Wasloso/TheMaze',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pygame>=2.0.0'],
    entry_points={
        'console_scripts': [
            'themaze=app:main',  # Replace with the entry point of your app
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
