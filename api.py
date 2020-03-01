from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, request
from services import get_cover

app = Flask(__name__)
api = Api(app)

STORIES = {
    1: {'title': 'Talking Fish', 'author': 'Aquaman', 'content': "Fish is awesome!"},
    2: {'title': 'Self-driving car', 'author': 'Ilon Musk', 'content': "The best car is one, that you don't need to drive"},
    3: {'title': 'Drug addict', 'author': 'Irvine Welsh', 'content': "Choose us. Choose life. Choose mortgage payments. choose washing machines. choose cars. choose sitting on a couch watching mind-numbing and spirit-crushing game shows, stuffing fuckin junk food intae yir mooth. Choose rotting away, pishing and shiteing yersel in a home, a total fuckin embarrassment tae the selfish, fucked-up brats ye've produced. Choose life."},
}


def abort_if_doesnt_exist(id):
    if id not in STORIES:
        abort(404, message="Story {} doesn't exist".format(id))



# Story
# shows a single story item and allows to edit it 
class Story(Resource):
    def get(self, story_id):
        abort_if_doesnt_exist(story_id)
        return STORIES[story_id]

    def delete(self, story_id):
        abort_if_doesnt_exist(story_id)
        del STORIES[story_id]
        return "Story {} deleted".format(id), 204

    def put(self, story_id):
        abort_if_doesnt_exist(story_id)
        content = request.json
        STORIES[story_id].update((key, content[key]) for key in content.keys() if key in STORIES[story_id])
        return STORIES[story_id], 201


# TodoList
# shows a list of all STORIES, and lets you POST to add new story
class StoryList(Resource):
    def get(self):
        return STORIES

    def post(self):
        content = request.json
        story_id = max(STORIES.keys()) + 1
        STORIES[story_id] = content
        return STORIES[story_id], 200


##
## Actually setup the Api resource routing here
##
api.add_resource(StoryList, '/stories')
api.add_resource(Story, '/stories/<int:story_id>')


if __name__ == '__main__':
    app.run(debug=True)