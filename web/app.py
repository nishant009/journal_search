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
  return "This method should add a journal"

@app.route("/v1/journals/<journal_id>", methods=['GET'])
def display_journal(journal_id):
  return render_template('journal.html', journal=__client.get_journal(journal_id))

@app.route("/v1/journals/<journal_id>", methods=['PUT'])
def update_journal(journal_id):
  return "This method should update a journal"

@app.route("/v1/journals/<journal_id>", methods=['DELETE'])
def delete_journal(journal_id):
  return "This method should delete a journal"

if __name__ == "__main__":
  app.run()
