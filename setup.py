from setuptools import setup, find_packages

# Read the version from a separate file (if needed)
exec(open('h5reader/__version__.py').read())

# Setup configuration
setup(
    name="h5reader",
    packages=find_packages(),  # Automatically find the package(s)
    version=__version__,       # Version number loaded from the file
    author="Your Name",
    url="https://github.com/yourusername/h5reader",  # Update with your repo URL
    license="MIT",
    python_requires='>=3.7',
    install_requires=[
        'h5py',
        'matplotlib',
        'tqdm',
        'readline; platform_system!="Windows"',
        'pyreadline3; platform_system=="Windows"',  # For Windows compatibility
    ],
    entry_points={
        'console_scripts': [
            'h5reader=h5reader.h5reader:main'  # Create CLI command
        ],
    }
)