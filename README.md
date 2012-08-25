gpx_conversion
==============

Convert GPX files into single line log files.

Python script for converting one or more files in GPX format into a log line
that's easily parsed by utilities such as Splunk.

Output format is:
    '''<datetime> lat=<latitude>, lon=<longitude>, elevation=<elevation>'''

Requires the untangle library for XML parsing:
    '''pip install untangle'''