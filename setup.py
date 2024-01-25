from setuptools import setup, find_packages

setup(
    name='MostActiveCookie',
    version='1.0.0',
    author='Joshua Finney',
    author_email='joshuafinney01@icloud.com',
    description='A command-line tool to find the most active cookie in a log file for a given day.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joshfinney/most-active-cookie',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'most_active_cookie=most_active_cookie.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    keywords='cookie log analysis cli-tool',
    license='MIT',
    test_suite='pytest',
    tests_require=['pytest==7.4.4'],
)