from flask import Flask, request, jsonify

app = Flask(__name__)

# example for get request..


@app.route("/get-user/<user_name>")  # <user_name> what ever the variable written inside the < > is the requested variable, path
def get_user(user_name):
    data_set = {"user_name": user_name, "message": " Hi i got the user user name i am learning get method in api", "name": "amith", "email": "amittalentplace@gmail.com"}
    get_data = request.args.get("extra")

    if get_data:
        data_set["extra"] = get_data

    return jsonify(data_set), 200   # here the 200 is status code for success. we have many like that.


# example for post request:
# to work on the post we need the data-base.. so we are just learning how it looks like.

@app.route('/create-user', methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True, port=7777)



