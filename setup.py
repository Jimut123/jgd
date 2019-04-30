from setuptools import setup
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(
        name = 'jgd',
        version="1.0.0",
        description = 'A public repo/folder downloader, without any token',
        author = 'Jimut Bahan Pal',
        author_email = 'paljimutbahan@gmail.com',
        maintainer = 'Jimut Bahan Pal',
        maintainer_email = 'paljimutbahan@gmail.com',
        url = '',
        license = 'GPLv2+',
        platforms = 'Linux',
        py_modules = ['jgd'],
        entry_points = {
            'console_scripts': ['jgd = jgd:main'],
        },
        include_package_data = True,
        install_requires = [
            'selenium',
            'wget',
            'pip',
            'bs4'
        ],
        keywords = 'Git cloner, github downloader, folder downloader, public repo scraper, scraper, selenium, free without token',
        classifiers = [
                'Development Status :: 1.0.0',
                'Environment :: Console',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: System Administrators',
                'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                'Operating System :: Manjaro',
                'Programming Language :: Python :: 3.7.2',
                'Topic :: Internet :: WWW/HTTP',
                'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
                ],
)
