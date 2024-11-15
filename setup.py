from setuptools import setup, find_packages
from pathlib import Path

# read version
version_file = Path(__file__).parent / 'garfield/_version.py'
dd = {}
with open(version_file.absolute(), 'r') as fp:
    exec(fp.read(), dd)
__version__ = dd['__version__']

# read long_description
long_description = (Path(__file__).parent / "README.md").read_text()

# read requirements.txt for extras_require
with open('requirements.txt') as f:
    notebook_required = f.read().splitlines()

setup(
    name='garfield',
    version=__version__,
    description="Genetic Algorithm Resonator Fitting for Impedance ExtrapoLation and Determination",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SebastienJoly/GARFIELD',
    author='Sebastien Joly',
    author_email="sebastien.joly@helmholtz-berlin.de", 
    license='GNU GENERAL PUBLIC LICENSE',
    download_url="https://pypi.python.org/pypi/garfieldx",
    project_urls={
            "Bug Tracker": "https://github.com/ImpedanCEI/GARFIELD/issues",
            "Documentation": "https://garfield.readthedocs.io/en/latest/.html",
            "Source Code": "https://github.com/ImpedanCEI/GARFIELD/",
        },
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
		"Topic :: Scientific/Engineering :: Physics",
        ],
    install_requires=[
        'numpy<2.0',
        'scipy',
        ],
    )
