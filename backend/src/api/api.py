from flask import Flask, jsonify
import controller

app = Flask(__name__)


# localhost:8000/recipes
@app.route("/recipes")
def serve_all_recpies():
    return controller.CONTROLLER_INSTANCE.get_all_recipe_metadata()


# localhost:8000/recipes/1
@app.route("/recipes/<int:recipe_id>")
def serve_recipe_information(recipe_id):
    return controller.CONTROLLER_INSTANCE.get_a_recipe(recipe_id)


# localhost:8000/steps/1/start
@app.route("/steps/<int:recipe_id>/start")
def start_new_recipe(recipe_id):
    return jsonify(success=controller.CONTROLLER_INSTANCE.new_recipe(recipe_id))


# localhost:8000/steps/{recipe_id}
@app.route("/steps/<int:recipe_id>")
def serve_step(recipe_id):
    return controller.CONTROLLER_INSTANCE.get_current_recipe_step()
