from flask import *
import json, time

app = Flask(__name__)    # this is the name of the project "__name__"

# Methods: GET/POST/PUT/DELETE
# GET: it is used to request data from a specified resource.  [Retrieve]
# POST : to create or pass any data.                          [Create]
# PUT: it is used to update the existing data.                [Update]
# delete : it is used to delete from the data.                [Delete]


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully created an api', 'Time': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    user_request = str(request.args.get('user'))  # the query gets generated is now-. /user/?user= amith kulkarni

    data_set = {'Page': 'Request', 'Message': f'We got the user name = {user_request}', 'Time': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump
    


if __name__ == '__main__':
    # here we are assigning the name of the project as '__main__'  , its like this is the main server..
    app.run(port=7777)  # to run the application on the local host, we use the port 7777, 7776, 7775 and so on...









