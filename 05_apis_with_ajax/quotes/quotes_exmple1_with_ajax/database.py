class DevelopmentDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'quotes_api' # change this line to connect to our database!!!!
    DB_HOST = 'localhost'
    """ unix_socket is used for connecting with MAMP. Take this out if you aren't using MAMP """
    DB_OPTIONS = {
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock'
    }

routes['default_controller'] = "Quotes";

from system.core.controller import *
class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        self.load_model('Quote')
    def index(self):
        return self.load_view('quotes/index.html')
    def index_json(self):
        quotes = self.models['Quote'].all()
        return jsonify(quotes=quotes)

from system.core.model import Model
class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()
    def all(self):
        query = "SELECT * FROM quotes"
        return self.db.query_db(query)