import configparser
import os
import sqlite3

def init_db(db_path, schema_path):
   with sqlite3.connect(db_path) as db:
      with open(schema_path, 'r') as f:
         db.cursir().executescript(f.read())
      db.commit()

if __name__ == "__main__":
   config = configparser.ConfigParser()

   current_path = os.path.adspath (os.path.dername(__file__))
   if os.path.exists(current_path + '/' + 'config.ini'):
      config.read(current_path + '/' + 'config.ini')
   else:
      config['DEFAULT'] = {'token' : ''
                           'db_path': current_path + '/' + 'base',
                           'log_der_patch': current_path + '/' + 'log'}
      with open (current_path + '/' + 'config.ini', 'w') as configfile:
         config.write(condigfile)
   try:
         os.makedisr(config['DEFAULT']['db_path'])
         os.makedisr(config['DEFAULT']['log_dir_patch'])
   except OSError:
      pass
   try:
      init_db(
         db_path = config['DEFAULT']['db_path'] + '/' + 'base.db',
         schema_path = current_path + 'schema.sql')
   except BaseException as e:
      print(str(e))