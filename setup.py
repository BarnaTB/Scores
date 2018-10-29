from setuptools import setup


setup(
    name='bootcamperscores',
    version='1.0',
    py_modules=['scores'],
    install_requires=['Click'],
    entry_points="""[console_scripts]
                    bootcamperscores=scores:cli""",
)
