from setuptools import setup


setup(
    name='scores',
    version='1.0',
    py_modules=['api'],
    install_requires=['click'],
    entry_points="""[console_scripts]
                      scores = scores:cli""",
)
