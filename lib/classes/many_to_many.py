class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            return  
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return  
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        articles_by_author = []
        for article in Article.all:
            if article.author == self:
                articles_by_author.append(article)
        return articles_by_author

    def magazines(self):
        magazine_by_author = []
        for article in Article.all:
            if article.author == self:
                magazine = article.magazine
                if magazine not in magazine_by_author:
                    magazine_by_author.append(magazine)
        return magazine_by_author

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        magazine_list = self.magazines()
        if not magazine_list:
            return None
        topic_areas_set = {magazine.category for magazine in magazine_list}
        return list(topic_areas_set)


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        articles_by_magazine = []
        for article in Article.all:
            if article.magazine == self:
                articles_by_magazine.append(article)
        return articles_by_magazine

    def contributors(self):
        contributors_by_magazine = []
        for article in Article.all:
            if article.magazine == self:
                author = article.author
                if author not in contributors_by_magazine:
                    contributors_by_magazine.append(author)
        return contributors_by_magazine

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        article_titles = []
        for article in articles:
            article_titles.append(article.title)
        return article_titles

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        
        contributing_authors = []
        for author, count in author_count.items():
            if count > 2:
                contributing_authors.append(author)
        
        return contributing_authors if contributing_authors else None