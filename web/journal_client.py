#!/usr/bin/env python

from datetime import datetime

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

  def add_journal(self, name):
    today = datetime.today()

    res = self.client.journal_search.journals.insert_one({
            "name": name,
            "created_at": today.now(),
            "updated_at": today.now()
          })

    return res.inserted_id

  def get_journal(self, journal_id):
    return self.client.journal_search.journals.find_one({
                "_id": ObjectId(journal_id)})

  def update_journal(self, journal_id, new_name):
    today = datetime.today()

    updated_journal = self.client.journal_search.journals.find_one_and_update(
                        {"_id": ObjectId(journal_id)},
                        {
                          '$set': {
                                    'name': new_name,
                                    'created_at': today.now(),
                                    'updated_at': today.now()
                                  }
                        },
                        return_document=ReturnDocument.AFTER
                      )
    return updated_journal['name'] == new_name

    def delete_journal(self, journal_id):
      self.client.journal_search.journals.find_one_and_delete(
        {"_id": ObjectId(journal_id)}
      )