from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, request
from services import get_cover, save_to_file, load_file
import json

app = Flask(__name__)
api = Api(app)

STORIES = load_file()


def abort_if_doesnt_exist(id):
    if id not in STORIES:
        abort(404, message="Story {} doesn't exist".format(id))


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('author', required=True)
parser.add_argument('content', required=True)


# Story
# shows a single story item and allows to edit it 
class Story(Resource):
    def get(self, story_id):
        abort_if_doesnt_exist(story_id)
        return STORIES[story_id]

    def delete(self, story_id):
        global STORIES
        abort_if_doesnt_exist(story_id)
        del STORIES[story_id]
        STORIES = save_to_file(STORIES)
        return "Story {} deleted".format(id), 204

    def put(self, story_id):
        global STORIES
        abort_if_doesnt_exist(story_id)
        content = request.json
        STORIES[story_id].update((key, content[key]) for key in content.keys() if key in STORIES[story_id])
        STORIES = save_to_file(STORIES)
        return STORIES[story_id], 201


# TodoList
# shows a list of all STORIES, and lets you POST to add new story
class StoryList(Resource):
    def get(self):
        return STORIES

    def post(self):
        global STORIES
        args = parser.parse_args()
        
        story_id = str(int(max(STORIES.keys())) + 1)
        
        STORIES[story_id] = {'title': args['title'], 
                             'author': args['author'],
                             'content': args['content']}
        STORIES[story_id]['cover'] = get_cover(STORIES[story_id])
        
        STORIES = save_to_file(STORIES)
        return STORIES[story_id], 200


##
## Actually setup the Api resource routing here
##
api.add_resource(StoryList, '/stories')
api.add_resource(Story, '/stories/<story_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')