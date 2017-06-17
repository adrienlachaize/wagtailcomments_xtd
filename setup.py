from setuptools import setup, find_packages


setup(
    name='wagtailcomments_xtd',
    author='Adrien Lachaize',
    author_email='adrien.lachaize@gmail.com',
    version='0.0.1',
    url='https://github.com/adrihein/wagtailcomments_xtd',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    packages=find_packages(),
    install_requires=[
        "wagtail>1.7",
        "Django>=1.8.16",
        "wagtailfontawesome>=1.0.2"
    ],
)
