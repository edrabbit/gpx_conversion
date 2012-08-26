""" convertgpx - Converts GPX files into a simple log file

Python script for converting one or more files in GPX format into a log line
that's easily parsed by utilities such as Splunk.

Output format is:
<datetime> lat=<latitude>, lon=<longitude>, elevation=<elevation>

"""

__author__ = "Ed Hunsinger"
__copyright__ = "Copyright 2012"
__email__ = "edrabbit@edrabbit.com"

import glob
import os
import sys

import untangle

def convert_gpx_to_log(gpxfile, logfile=None, append=False):
    if not logfile:
        fname, fext = os.path.splitext(gpxfile)
        logfile = "%s.log" % fname
        file_mode = "w"
    else:
        file_mode = "a"
    print "Processing %s to %s" % (gpxfile, logfile)
    obj = untangle.parse(gpxfile)
    outfile = open(logfile, file_mode)
    for trk in obj.gpx.children:
        for trkseg in trk.children:
            for trkpt in trkseg.children:
                lat = trkpt['lat']
                lon = trkpt['lon']
                elevation = trkpt.ele.cdata
                timestamp = trkpt.time.cdata
                event = ("%s lat=%s, lon=%s, elevation=%s\n"
                         % (timestamp, lat, lon, elevation))
                outfile.write(event)
    outfile.close()

if __name__ == "__main__":
    print "Processing gpx files..."
    if len(sys.argv) == 1:
        print "Usage: %s [gpx_files] [output_file]" % sys.argv[0]
        print "Wild cards are permitted in [gpx_files]"
        print ("If you specify wildcards in gpx_files and provide an "
               "output_file, all gpx_files will be combined into output_file")
        exit(1)
    else:
        list_of_files = glob.glob(sys.argv[1])
        # Sort files by filenames, assuming some sort of datebased filename
        list_of_files.sort()
        if len(sys.argv) > 2:
            output_file = sys.argv[2]
        else:
            output_file = None

        for gpxfile in list_of_files:
            convert_gpx_to_log(gpxfile, output_file)