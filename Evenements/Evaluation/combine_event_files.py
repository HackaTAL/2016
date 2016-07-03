from optparse import OptionParser
import os
import ntpath
import re
import sys

def parse_match(file_name):
   head, tail = ntpath.split(file_name)
   name = tail or ntpath.basename(head)
   p = re.match("(\S+?)_(\S+?)_(\S+?)_\S+", name)
   if p:
      team1 = p.groups()[0].replace('-', ' ').replace('~', ' ')
      team2 = p.groups()[1].replace('-', ' ').replace('~', ' ')
      return "{}\t{}\t{}".format(team1, team2, p.groups()[2])
   else:
      return None

if __name__ == "__main__":
   usage = '''%prog file1.tsv [file2.tsv ...]
Each filename should respect the following pattern: <Team1>_<Team2>_<yyyy>-<mm>-<dd>_<.*>.tsv'''
   parser = OptionParser(usage)
   opts, args = parser.parse_args()
   
   if(len(args) < 1):
      parser.print_usage()
      sys.exit(1)
   
   for arg in args:
      match_info = parse_match(arg)
      if match_info is None:
         sys.stderr.write("Warning: " + arg +
      " doesn't respect the following pattern: <Team1>_<Team2>_<yyyy>-<mm>-<dd>_<*>.tsv and it will be ignored\n")
         continue
      iterlines = iter(open(os.path.realpath(arg), 'r'))
      for line in iterlines:
         if line.strip():
            if(not re.match("TEMPS", line)):
               sys.stdout.write("{0}\t{1}".format(match_info, line))
      