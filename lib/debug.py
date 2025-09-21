import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create authors
    author_one = Author("J.K. Rowling")
    author_two = Author("George R.R. Martin")
    author_three = Author("Stephen King")

    # Create magazines
    magazine_one = Magazine("Tech Today", "Technology")
    magazine_two = Magazine("Foodies Digest", "Food & Cuisine")

    # Create articles, making sure some authors contribute more than twice
    # Author One writes 3 articles for Magazine One (to test contributing_authors)
    article_one = Article(author_one, magazine_one, "The Future of AI")
    article_two = Article(author_one, magazine_one, "A Guide to Python")
    article_three = Article(author_one, magazine_one, "Machine Learning for Beginners")

    # Author Two writes 2 articles for Magazine One
    article_four = Article(author_two, magazine_one, "Top 10 Gadgets of 2025")
    article_five = Article(author_two, magazine_one, "The Best Smartwatch")

    # Author One also writes an article for Magazine Two (to test magazines & topic_areas)
    article_six = Article(author_one, magazine_two, "The Art of Baking Sourdough")

    # Author Three has no articles (to test methods that return None)

    # Test the methods for Author One
    print("\n--- TESTING AUTHOR ONE ---")
    print(f"Author One's name: {author_one.name}")
    print(f"Author One's articles: {[article.title for article in author_one.articles()]}")
    print(f"Author One's magazines: {[magazine.name for magazine in author_one.magazines()]}")
    print(f"Author One's topic areas: {author_one.topic_areas()}")

    # Test the methods for Magazine One
    print("\n--- TESTING MAGAZINE ONE ---")
    print(f"Magazine One's name: {magazine_one.name}")
    print(f"Magazine One's articles: {[article.title for article in magazine_one.articles()]}")
    print(f"Magazine One's contributors: {[author.name for author in magazine_one.contributors()]}")
    print(f"Magazine One's contributing authors: {[author.name for author in magazine_one.contributing_authors()]}")
    
    # Test the None case for Author Three
    print("\n--- TESTING NONE CASE ---")
    print(f"Author Three's topic areas: {author_three.topic_areas()}")
    
    # Test the article titles method
    print("\n--- TESTING ARTICLE TITLES ---")
    print(f"Magazine One's article titles: {magazine_one.article_titles()}")
    
    # don't remove this line, it's for debugging!
    ipdb.set_trace()