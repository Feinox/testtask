import random as rd
from flask import Flask

app = Flask(__name__)


@app.route('/number', methods=['GET'])
def test_number():
	return str(rd.randint(1, 500))


# Run in HTTP
if __name__ == '__main__':
	app.run(host='127.0.0.1', port='5000')