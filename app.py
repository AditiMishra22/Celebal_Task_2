from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return "Node added as head"
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return "Node added"

    def delete_nth_node(self, n):
        if self.head is None:
            raise Exception("List is empty")

        if n <= 0:
            raise Exception("Invalid index")

        if n == 1:
            self.head = self.head.next
            return f"Node {n} deleted"

        current = self.head
        for _ in range(n - 2):
            if current is None or current.next is None:
                raise Exception("Index out of range")
            current = current.next

        if current.next is None:
            raise Exception("Index out of range")

        current.next = current.next.next
        return f"Node {n} deleted"

    def print_list(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' -> '.join(result) if result else "List is empty"

linked_list = LinkedList()

# Routes
@app.route("/")
def home():
    message = request.args.get("message")
    return render_template("index.html", message=message, list=linked_list.print_list())

@app.route("/add", methods=["POST"])
def add():
    data = request.form["data"]
    message = linked_list.append(data)
    return redirect(url_for("home", message=message))

@app.route("/delete", methods=["POST"])
def delete():
    try:
        index = int(request.form["index"])
        message = linked_list.delete_nth_node(index)
    except Exception as e:
        message = str(e)
    return redirect(url_for("home", message=message))

if __name__ == "__main__":
    app.run(debug=True)
