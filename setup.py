from setuptools import setup

setup(
    name='FloppyLib',
    version='0.1.0',
    description='Library for interacting with floppy disks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='HazmatPants',
    author_email='hazmatpants@gmail.com',
    url='https://github.com/your-repo',
    py_modules=['floppyLib.'],
    install_requires=[
        'shutil',
        'win32api'
        'os'
        'time'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
    ],
    python_requires='>=3.6',             # Minimum Python version.
)