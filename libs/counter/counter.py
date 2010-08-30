import random

from google.appengine.ext import db
from google.appengine.api import memcache

from globals import *
from models import *


def ChangeCount(nameOfCounter, delta):
  
  shard_id = '/%s/%s' % (nameOfCounter, random.randint(1, SHARDS_PER_COUNTER))
  
  def update():
    shard = CounterShard.get_by_key_name(shard_id)
    if shard:
     shard.count += delta
    else:
     shard = CounterShard(key_name=shard_id, name=nameOfCounter, count=delta)
    shard.put()
    
  db.run_in_transaction(update)


def GetCount(nameOfCounter):
  
  memcache_id = '/CounterShard/%s' %  nameOfCounter
  result = memcache.get(memcache_id)
  
  if not (result == None):
    return result
    
  result = 0
  
  for shard in CounterShard.gql('WHERE name=:1', nameOfCounter):
   result += shard.count
   
  memcache.set(memcache_id, result, 600)
  
  return result