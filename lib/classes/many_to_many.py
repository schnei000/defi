class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)


class Author:
    def __init__(self, name):
        self.name = name

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
        article_titles = []
        for article in Article.all:
            if article.magazine == self:
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
