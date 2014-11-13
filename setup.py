#!/usr/bin/env python
# -*- coding: utf8 -*-
import os

from modulefinder import ModuleFinder
from distutils.core import setup






setup(
    name='zabbix_service_monitor_script',
    version='0.1',
    packages=['zsmc'],
    provides=['zsmc'],
    url='https://github.com/damagedcode/zabbix_service_monitor_script',
    license='MIT',
    author='HarrisonZhu',
    author_email='wcg6121@gmail.com',
    description='A script for zabbix agent monitor service, etc. mysql, mongodb, memcache..',
    long_description=open(os.path.dirname(__file__), 'README.md').read(),
)

