from setuptools import setup

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_hello_world.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='lektor-bibtex-support',
    version='0.1',
    author='Arun Persaud',
    author_email='arun@nubati.net',
    description=description,
    long_description=readme,
    long_description_content_type='text/markdown',
    data_files=[('templates', ['templates/lektor_bibtex_support_default_template.html'])],
    url='https://github.com/arunpersaud/lektor-bibtex-support',
    include_package_data=True,
    keywords='Lektor plugin static-site bibtex',
    license='MIT',
    py_modules=['lektor_bibtex_support'],
    entry_points={
        'lektor.plugins': [
            'bibtex-support = lektor_bibtex_support:BibtexSupportPlugin',
        ]},
    install_requires=['pybtex'],
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Lektor',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
