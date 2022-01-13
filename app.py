from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {
        "item_name" : "Toys",
        "price" : 10.99
    }

]

@app.route("/items")
def get_items():
    return jsonify("items:", items)

@app.route("/additem/<string:name>", methods=["POST"])
def add_item(name: str):
    data = request.get_json()
    items.append({"item_name": name, "price": data["price"]})
    return jsonify("items", items)

@app.route("/deleteitem/<string:name>", methods=["DELETE"])
def delete_item(name: str):
    items[:] = [item for item in items if item.get("item_name") != name]
    return jsonify("items", items)
            

if __name__ == "__main__":
    app.run()