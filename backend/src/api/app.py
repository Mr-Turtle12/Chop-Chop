from flask import Flask, jsonify
import controller

app = Flask(__name__)


# http://127.0.0.1:5000/recipes
@app.route("/recipes")
def serve_all_recpies():
    return controller.CONTROLLER_INSTANCE.get_all_recipe_metadata()


# http://127.0.0.1:5000/recipes/1
@app.route("/recipes/<int:recipe_id>")
def serve_recipe_information(recipe_id):
    return controller.CONTROLLER_INSTANCE.get_a_recipe(recipe_id)


# http://127.0.0.1:5000/steps/1/start
@app.route("/recipes/<int:recipe_id>/start")
def start_new_recipe(recipe_id):
    return jsonify(success=controller.CONTROLLER_INSTANCE.new_recipe(recipe_id))


# http://127.0.0.1:5000/recipe/1/step
@app.route("/recipes/<int:recipe_id>/step")
def serve_step(recipe_id):
    return controller.CONTROLLER_INSTANCE.get_current_recipe_step()
