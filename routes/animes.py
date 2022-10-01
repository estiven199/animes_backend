import json
import flask        
import requests
from flask import request ,jsonify
from flask_restful import Api, Resource
# from common.fields import fields_animes as tpf

animes= flask.Blueprint('animes', __name__)
api = Api(animes)

class general():
    def put_recomendation(self,anime):
        if anime['score'] == None:
            anime['recomendation'] == "See for yourself and give us your opinion"
            return anime
        anime['recomendation'] = "I do not recommend it." if float(anime['score']) >= 1 and float(anime['score']) <= 4  else "You may have fun." if float(anime['score']) >= 5 and float(anime['score']) <= 7 else "Great, this is one of the best anime."
        return anime
    def while_for_pages(self,title):
        page = 1
        state = True
        data_full = []
        while state ==True:
            data,state = self.get(title,page=page)
            page += 1
            data_full += data
        return data_full

class Animes(Resource,general):
    def get(self):
        args = json.loads(json.dumps({k: request.args[k] for k in request.args.keys()}))
        title = args['title']
        print(title)
        data = getattr(requests, "get")(url=f"https://api.jikan.moe/v4/anime?q={title}&sfw").json()
        data_full = [self.put_recomendation(anime) for anime in data['data'] ]
        return data_full,data['pagination']['has_next_page']
    def get_by_pages(self,title):
        return self.while_for_pages(title)

api.add_resource(Animes, '/api/v1.0/animes',endpoint='')