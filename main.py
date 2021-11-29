from flask import Flask
from flask_restful import Api
from routes.data_science_salaries import DataScienceSalaries

from routes.help import Help

app = Flask(__name__)
api = Api(app)


api.add_resource(Help, '/')
api.add_resource(DataScienceSalaries, '/data-science-salaries')

if __name__ == '__main__':
    app.run(debug=True)
