from flask import Flask, jsonify, request
from post import Post

app = Flask(__name__)

posts = []


@app.route("/post/", methods=["POST"])
def create():
    data = request.get_json()
    post = Post(data["id"], data["body"], data["author"])
    posts.append(post)
    return jsonify({"id": post.id})


@app.route("/post/<int:_id>/", methods=["GET"])
def read(_id: int):
    for post in posts:
        if post.id == _id:
            return jsonify({"id": post.id, "body": post.body, "author": post.author})


@app.route("/post/<int:_id>/", methods=["PUT"])
def update(_id: int):
    for post in posts:
        if post.id == _id:
            posts.remove(post)
            data = request.get_json()
            post = Post(data["id"], data["body"], data["author"])
            posts.append(post)
            return jsonify({"id": post.id, "body": post.body, "author": post.author})


@app.route("/post/<int:_id>/", methods=["DELETE"])
def delete(_id: int):
    for post in posts:
        if post.id == _id:
            posts.remove(post)
    return f"Delete post with id {_id}"


if __name__ == "__main__":
    app.run()
