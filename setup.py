from setuptools import setup


setup(
    name='portcharges',
    version='0.0.1.dev',
    packages=('portcharges',),
    include_package_data=True,
    classifiers=(
        'Programming Language :: Python :: 3.5',
    ),
    install_requires=(
        'knot==0.4.0',
        'pymongo==3.4.0',
    ),
    zip_safe=False,
)
