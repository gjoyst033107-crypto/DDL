
from flask import Flask, render_template, request, jsonify

from algorithms.array import Array
from algorithms.stack import Stack
from algorithms.queue import Queue
from algorithms.linked_list import LinkedList
from algorithms.tree import BSTModule
from algorithms.graph import Graph

from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.linear_search import linear_search
from algorithms.binary_search import binary_search


app = Flask(__name__)


# Create data structure objects
my_array = Array()
my_stack = Stack()
my_queue = Queue()
my_linked_list = LinkedList()
my_tree = BSTModule()
my_graph = Graph()


# Main website
@app.route("/")
def home():
    return render_template("index.html")


# Run data structure operations
@app.route("/run", methods=["POST"])
def run_algorithm():

    global my_tree, my_graph

    data = request.get_json()

    topic = data.get("topic")
    operation = data.get("operation")

    values = data.get("values", [])
    target = data.get("target")

    result = None

    try:

        # ARRAY
        if topic == "array":

            if operation == "insert":
                index = int(data.get("index", 0))
                value = int(data.get("value"))
                result = my_array.insert(value, index)

            elif operation == "delete":
                index = int(data.get("index"))
                result = my_array.delete(index)

            elif operation == "access":
                index = int(data.get("index"))
                result = my_array.access(index)

            elif operation == "update":
                index = int(data.get("index"))
                value = int(data.get("value"))
                result = my_array.update(index, value)

            elif operation == "display":
                result = my_array.display()

        # STACK
        elif topic == "stack":

            if operation == "push":
                result = my_stack.push(int(data.get("value")))

            elif operation == "pop":
                result = my_stack.pop()

            elif operation == "peek":
                result = my_stack.peek()

            elif operation == "display":
                result = my_stack.display()

        # QUEUE
        elif topic == "queue":

            if operation == "enqueue":
                result = my_queue.enqueue(int(data.get("value")))

            elif operation == "dequeue":
                result = my_queue.dequeue()

            elif operation == "front":
                result = my_queue.front()

            elif operation == "display":
                result = my_queue.display()

        # LINKED LIST
        elif topic == "linked_list":

            if operation == "insert":
                my_linked_list.insert(int(data.get("value")))
                result = my_linked_list.display()

            elif operation == "insert_beginning":
                my_linked_list.insert_at_beginning(
                    int(data.get("value"))
                )
                result = my_linked_list.display()

            elif operation == "delete":
                result = my_linked_list.delete(
                    int(data.get("value"))
                )

                if result is None:
                    result = my_linked_list.display()

            elif operation == "search":
                result = my_linked_list.search(
                    int(data.get("target"))
                )

            elif operation == "display":
                result = my_linked_list.display()

        # TREE
        elif topic == "tree":

            if operation == "build":

                my_tree = BSTModule()

                for value in values:
                    my_tree.add(int(value))

                result = {
                    "preorder": my_tree.preorder(my_tree.root),
                    "inorder": my_tree.inorder(my_tree.root),
                    "postorder": my_tree.postorder(my_tree.root),
                    "dfs": my_tree.dfs(),
                    "bfs": my_tree.bfs()
                }

            elif operation == "preorder":
                result = my_tree.preorder(my_tree.root)

            elif operation == "inorder":
                result = my_tree.inorder(my_tree.root)

            elif operation == "postorder":
                result = my_tree.postorder(my_tree.root)

            elif operation == "dfs":
                result = my_tree.dfs()

            elif operation == "bfs":
                result = my_tree.bfs()

        # GRAPH
        elif topic == "graph":

            if operation == "build":

                my_graph = Graph()

                for edge in data.get("edges", []):

                    my_graph.add_edge(
                        edge[0],
                        edge[1]
                    )

                result = my_graph.display()

            elif operation == "dfs":
                result = my_graph.dfs(
                    data.get("start")
                )

            elif operation == "bfs":
                result = my_graph.bfs(
                    data.get("start")
                )

            elif operation == "display":
                result = my_graph.display()

        # BUBBLE SORT
        elif topic == "bubble_sort":

            if operation == "sort":
                result = bubble_sort(values.copy())

        # QUICK SORT
        elif topic == "quick_sort":

            if operation == "sort":
                result = quick_sort(values)

        # LINEAR SEARCH
        elif topic == "linear_search":

            if operation == "search":
                result = linear_search(
                    values,
                    int(target)
                )

        # BINARY SEARCH
        elif topic == "binary_search":

            if operation == "search":
                result = binary_search(
                    values,
                    int(target)
                )

        else:
            return jsonify({
                "success": False,
                "message": "Invalid topic."
            }), 400

        if result is None:
            return jsonify({
                "success": False,
                "message": "Invalid operation or no result returned."
            }), 400

        return jsonify({
            "success": True,
            "result": result
        })

    except (ValueError, TypeError, IndexError) as error:

        return jsonify({
            "success": False,
            "message": str(error)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
