#!/usr/bin/env python

from bson.objectid import ObjectId
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
      results.append({'id': journal['_id'], 'name': journal['name']})

    return results

  def get_journal(self, journal_id):
    return self.client.journal_search.journals.find_one({
                "_id": ObjectId(journal_id)})