#!/usr/bin/env python

from datetime import datetime
from optparse import OptionParser

from pymongo import MongoClient

class SeedDataLoader:

  def __init__(self, host, port, seed_file_name):
    self.host = host
    self.port = port
    self.seed_file_name = seed_file_name
    self.client = None
    self.__initMongoClient()

  def __readData(self):
    with open(self.seed_file_name, 'r') as stream:
      return stream.read().splitlines()

  def __initMongoClient(self):
    if not self.client:
      self.client = MongoClient(self.host, self.port)

  def processEntries(self):
    today = datetime.today()

    journals = self.client.journal_search.journals

    for name in self.__readData():
      record = {'name': name, 'created_at': today.now(), 'updated_at': today.now()}
      journals.insert_one(record)


def main():
  parser = OptionParser(usage="usage: %prog [options]",
                        version="%prog 1.0")
  parser.add_option("-t", "--host",
                    type="string",
                    dest="host",
                    default="localhost",
                    help="Mongo DB Host")
  parser.add_option("-p", "--port",
                    type="int",
                    dest="port",
                    default=27017,
                    help="Mongo DB Port")
  parser.add_option("-f", "--file",
                    type="string",
                    dest="seed_file_name",
                    default='',
                    help="Seed data file")
  
  (options, args) = parser.parse_args()

  if not options.seed_file_name:
    parser.error("You need to provide seed file name")

  SeedDataLoader(options.host, options.port, options.seed_file_name).processEntries()


if __name__ == "__main__": 
  main()