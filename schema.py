from marshmallow import Schema, fields, pre_load
import datetime

class ArticlesSchema(Schema):
    source = fields.Dict()
    author = fields.String()
    title = fields.String()
    description = fields.String()
    url = fields.String()
    urlToImage = fields.String()
    publishedAt = fields.String()
    content = fields.String()

    @pre_load
    def format_date(self, data, **kwargs):
        if len(data["publishedAt"]) >= 10:
            date = data["publishedAt"]
            data["publishedAt"] = date[:10]
        return data