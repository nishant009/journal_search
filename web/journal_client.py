#!/usr/bin/env python

from pymongo import MongoClient

class JournalClient:

  def __init__(self, host='localhost', port=27017):
    self.host = host
    self.port = port
    self.client = None
    self.__initMongoClient()

  def __initMongoClient(self):
    if not self.client:
      self.client = MongoClient(self.host, self.port)

  def list_journals(self):
    journals = self.client.journal_search.journals.find()

    results = []
    for journal in journals:
      results.append({'id': journal['_id'], 'name': journal['name'].encode('utf-8')})

    return results