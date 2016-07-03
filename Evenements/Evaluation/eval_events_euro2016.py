# encoding: utf-8
'''
eval_events_euro2016 -- Evaluation of event detection using Precision, Recall and F1
'''

from __future__ import division
import sys
import os.path
from datetime import datetime, timedelta
import re
from optparse import OptionParser
from tabulate import tabulate
      

class Event(object):
   '''
   An event is one of the following (event : description) :
      team1 team2 date hh:mm BUT joueur : but d'un joueur
      team1 team2 date hh:mm TIR joueur : tir d'un joueur
      team1 team2 date hh:mm CJA joueur : carton jaune pour un joueur
      team1 team2 date hh:mm CRO joueur : carton rouge pour un joueur
      team1 team2 date hh:mm PEN pays : penalty pour un pays (celui qui commet la faute)
      team1 team2 date hh:mm CGT joueur1 ; joueur2 : changement de joueurs (joueur sortant et joueur entrant)
      team1 team2 date hh:mm D1P : début de la première période du match
      team1 team2 date hh:mm F1P : fin de la première période et score
      team1 team2 date hh:mm D2P : début de la deuxième période
      team1 team2 date hh:mm F2P : fin de la deuxième période
      team1 team2 date hh:mm DPR : début de prolongation
      team1 team2 date hh:mm FPR : fin de prolongation
   '''
   
   strictness = 2
   
   def __init__(self, text):
      try:
         fields = re.split('\t+', text.rstrip())
         self.teams = set([fields[0], fields[1]])
         self.date = datetime.strptime(fields[2], "%Y-%m-%d")
         self.time = datetime.strptime(fields[3], "%H:%M:%S")
         self.type = fields[4]
         self.annotations = tuple(re.split('\s*;\s*', fields[5])) if len(fields) > 5 else () 
      except:
         raise
         
   def __repr__(self):
      return '{0}\t{1}\t{2}\t{3}\t{4}'.format(
                        "\t".join(self.teams),
                        self.date.strftime("%Y-%m-%d"),
                        self.time.strftime("%H:%M:%S"),
                        self.type,
                        ';'.join(self.annotations))

   def __hash__(self):
      return hash(self.__repr__())
   
   def is_equal(self, other, strict):
      '''
      Test if the current event is equal to another event
      3 levels of strictness are implemented: 2=strict, 1=intermediate, 0=loose
      '''
      isEqual = (set(self.teams) == set(other.teams)
                 and self.date == other.date
                 and self.type == other.type)             
      
      if(strict > 0):
         isEqual = (isEqual and
                    ((self.annotations is None and other.annotations is None)
                     or ((self.annotations is not None and other.annotations is not None) and
                         (set(self.annotations) == set(other.annotations)))))
         
      if(strict > 1):
         isEqual = isEqual and abs((self.time - other.time).total_seconds()) <= timedelta(minutes=2).total_seconds()

      return isEqual
   
   def __eq__(self, other):
      return self.is_equal(other, Event.strictness)

   def __ne__(self, other):
      return not self.__eq__(other)


def parse_event_file(file_str):
   if os.path.isfile(file_str):
      events = []
      for line_str in open(file_str, 'r'):
         try:
            event = Event(line_str)
            events.append(event)
         except:
            sys.stderr.write('Ill-formated event (will be discarded): {0}'.format(line_str))
      return events
   else:
      sys.stderr.write('File {0} does not exist or cannot be read.\n'.format(file_str))
      sys.exit(1)


def evaluate(gold, pred, strict):
   Event.strictness = strict
   correct = 0
   cpgold = list(gold)
   for e in pred:
      try:
         i = cpgold.index(e)
         correct = correct + 1
         del cpgold[i]
      except:
         pass
   
   precision = correct / len(pred)
   recall = correct / len(gold)
   f1 = 2*precision*recall / (precision+recall) if precision+recall>0 else 0
   return (precision, recall, f1)


def print_scores(header, scores):
   print header
   print '-' * len(header)
   print 'Precision = {0:.2f} %'.format(scores[0]*100)
   print 'Recall = {0:.2f} %'.format(scores[1]*100)
   print 'F1-measure = {0:.2f} %'.format(scores[2]*100)
   print '-' * len(header)


def main(opts, args):
   gold_events = parse_event_file(args[0])
   pred_events = parse_event_file(args[1])
   
   return (('', '', 'strict',) + evaluate(gold_events, pred_events, 2),
          (opts.team_name, opts.system_name, 'intermediate',) + evaluate(gold_events, pred_events, 1),
          ('', '', 'loose',) + evaluate(gold_events, pred_events, 0))
   

if __name__ == "__main__":
   parser = OptionParser('''%prog gold prediction''')
   parser.add_option('-s', '--system', dest='system_name', default='Default')
   parser.add_option('-t', '--team', dest='team_name', default='Default')
   opts, args = parser.parse_args()
   if len(args) < 2:
      parser.print_usage()
      sys.exit(1)
   
   scores = main(opts, args)
   print tabulate(scores, ('Team', 'System', 'Evaluation', 'Precision', 'Recall', 'F1-measure'))
   