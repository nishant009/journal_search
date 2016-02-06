#!/usr/bin/env python

from flask import Flask
from flask import request, render_template

from journal_client import JournalClient

app = Flask(__name__)

__client = JournalClient()

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/v1/journals", methods=['GET'])
def list_journals():
  return render_template('journal_list.html', journals=__client.list_journals())

@app.route("/v1/journals", methods=['POST'])
def add_journal():
  id = __client.add_journal(request.form['name'])
  return "Added journal with id %s" % id

@app.route("/v1/journals/<journal_id>", methods=['GET', 'PUT', 'DELETE'])
def journal(journal_id):
  if request.method == 'GET':
    return render_template('journal.html', journal=__client.get_journal(journal_id))
  elif request.method == 'PUT':
    res = __client.update_journal(journal_id, request.form['name'])
    if res:
      return "Journal updated"
    else:
      return "Error updating journal"
  elif request.method == 'DELETE':
    __client.delete_journal(journal_id)
    return "Journal deleted"

if __name__ == "__main__":
  app.run()
