# Copyright 2020 Salar Nosrati-Ershad
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import setuptools


setuptools.setup(
    name='beancounter',
    version='0.0.1',
    author='Salar Nosrati-Ershad',
    author_email='vharveyi@tutanota.com',
    project_urls={
        'Source': 'https://github.com/blueblossom/beancounter',
        'Tracker': 'https://github.com/blueblossom/beancounter/issues',
    },
    license='Apache-2.0',
    packages=['beancounter'],
    entry_points={
        'console_scripts': ['beancounter = beancounter.__main__:main'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX'
        'Programming Language :: Python :: 3.8',
        'Topic :: Office/Business :: Financial :: Accounting',
    ]
)
