from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-custom_search',
	version=version,
	description="Custom Search",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='VT',
	author_email='v-vt@azaas.com',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.custom_search'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.custom_search:PluginClass
        my_custom_search=ckanext.custom_search.plugin:CustomSearchPlugin
	""",
)
