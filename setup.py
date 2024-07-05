from setuptools import setup, find_packages

setup(
    name='mkdocs-asyncapi',
    version='0.0.1',
    description='A MkDocs plugin for rendering asyncAPI specification',
    license='MIT',
    packages=find_packages(),
    author='Tortem',
    author_email='todo',
    keywords=['mkdocs', 'plugin', 'asyncapi'],
    url='https://github.com/Tortem/mkdocs-asyncapi',
    entry_points={
        "mkdocs.plugins": [
            "async-api = mkdocs_asyncapi.plugin:AsyncApiPlugin",
        ]
    },
)