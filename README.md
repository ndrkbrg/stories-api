# stories-api
REST API for Stories.  
Python 3.8 + Flask-RESTful

## Usage:
```
docker-compose build
docker-compose up
```

## API:
### Get all stories:
```
GET http://localhost:5000/stories
```
### Add a Story:
```
POST -H "Content-Type: application/json" -d "{"title":"", "author":"", "content":""}" http://localhost:5000/stories
```
### Get one Story
```
GET http://localhost:5000/stories/<id>
```
### Change Story
```
PUT -H "Content-Type: application/json" -d "{"title":"", "author":"", "content":""}" http://localhost:5000/stories/<id>
```
### Delete story
```
DELETE http://localhost:5000/stories/<id>
```
### Get Story Cover
```
GET http://localhost:5000/story_cover/<id>
```
