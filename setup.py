from setuptools import setup, find_packages

setup(
    name='FolderScanner',
    version='0.1.0',
    author='Eugene Evstafev',
    author_email='ee345@cam.ac.uk',
    description='Scan directories, apply ignore rules, and chunk file contents.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/FolderScanner',
    packages=find_packages(),
    install_requires=[
        'pathspec',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)