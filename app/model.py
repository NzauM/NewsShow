class News:
    def __init__(self,name,description,url):
        self.name = name
        self.description = description
        self.url = url

class Articles:
    def __init__(self,id,title,description,image,publishedAt,readMore):
        self.id = id
        self.title =title
        self.description = description
        self.image = image
        self.publishedAt = publishedAt
        self.readMore = readMore