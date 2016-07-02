from optparse import OptionParser
import os
import ntpath
import re
import sys

def parse_match(file_name):
   head, tail = ntpath.split(file_name)
   name = tail or ntpath.basename(head)
   p = re.match("(\S+?)_(\S+?)_(\S+?)_\S+", name)
   team1 = p.groups()[0].replace('-', ' ').replace('~', ' ')
   team2 = p.groups()[1].replace('-', ' ').replace('~', ' ')
   return "{}\t{}\t{}".format(team1, team2, p.groups()[2])

if __name__ == "__main__":
   usage = '''%prog file1.tsv [file2.tsv ...]
Each filename should respect the following pattern: Team1_Team2_yyyy-mm-dd_HHh_fr.tsv'''
   parser = OptionParser(usage)
   opts, args = parser.parse_args()
   
   if(len(args) < 1):
      parser.print_usage()
      sys.exit(1)
   
   for arg in args:
      match_info = parse_match(arg)
      iterlines = iter(open(os.path.realpath(arg), 'r'))
      next(iterlines)
      for line in iterlines:
         if line.strip():
            sys.stdout.write("{0}\t{1}".format(match_info, line))
      