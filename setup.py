from setuptools import setup

setup(
    name='quack-docs',
    version='0.1.0',
    packages=['.', 'src', 'src.docs', 'src.q', 'src.utils'],
    package_dir={'': '.'},
    py_modules=['main'],
    install_requires=[
        'pyfiglet',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'quack-docs=main:main',
        ],
    },
)
