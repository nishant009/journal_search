#!/usr/bin/env python

import redis

class SuggestClient:

  def __init__(self,
               redis_host=localhost,
               mongo_host=localhost,
               mongo_port=27017
              ):
    self.host = host
    self.mongo_host = mongo_host
    self.mongo_port = mongo_port
    
    self.client = None
    self.__initRedisClient()
    
    self.mongo_client = None
    self.__initMongoClient()

  def __initRedisClient(self):
    if not self.client:
      self.client = redis.Redis(self.host)

  def __initMongoClient(self):
    if not self.mongo_client:
      self.mongo_client = JournalClient(self.mongo_host, self.mongo_port)

  def suggest(self, query):
    # Check if the query is cached.
    if self.client.exists(query):
      results = self.client.lrange(query, 0 , -1)
      self.client.expire(query, 60)
      return results

    results = self.mongo_client.get_journal_suggestions(query)
    [self.client.rpush(query, result) for result in results]
    self.client.expire(query, 60)
    return results