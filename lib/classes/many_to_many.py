class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._validate_auth_and_mag(author, magazine)
        self._author = author
        self._magazine = magazine
        self._validate_title(title)
        self._title = title
        Article.all.append(self)

        author._append_to_magazines_list(self, magazine)
        magazine._append_to_magazine_authors(self, author)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("The Author must be an instance of Author class.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError(
                "The Magazine must be an instance of Magazine class.")
        self._magazine = value

    @property
    def title(self):
        return self._title

    def _validate_title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        if not 5 <= len(value.strip()) <= 50:
            raise ValueError("Title must be between 5 and 50 characters long.")

    @staticmethod  # turning this into a static method so that i can call it from the Author class for DRY purposes
    def _validate_auth_and_mag(author, magazine):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")


class Author:
    def __init__(self, name):
        self._validate_name(name)
        self._name = name

        self.articles_list = []
        self.magazines_list = []

    @property
    def name(self):
        return self._name

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Author name must be a non-empty string.")
        if len(name.strip()) == 0:
            raise ValueError("Author name cannot be empty.")

    def articles(self):
        return self.articles_list

    def magazines(self):
        return self.magazines_list

    def add_article(self, magazine, title):
        Article._validate_auth_and_mag(self, magazine)
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.magazines_list:
            return None
        # I'm using a set comprehension here rather than a list comprehension because I specifically want unique categories and sets dont allow duplicates
        magazine_categories = {mag.category for mag in self.magazines_list}

        return list(magazine_categories)

    def _append_to_magazines_list(self, article, magazine):
        self.articles_list.append(article)
        if magazine not in self.magazines_list:
            self.magazines_list.append(magazine)


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.magazine_articles = []
        self.magazine_authors = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._validate_category(value)
        self._category = value

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Magazine name must be a string.")
        if not 2 <= len(name.strip()) <= 16:
            raise ValueError(
                "Magazine name must be a string between 2 and 16 characters.")

    def _validate_category(self, category):
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return self.magazine_articles

    def contributors(self):
        return self.magazine_authors

    def article_titles(self):
        if not self.magazine_articles:
            return None

        return [article.title for article in self.magazine_articles]

    def contributing_authors(self):
        if not self.magazine_authors:
            return None

        # I'm using a dict because the key-value pair structure will help me track articles coount per author
        per_author_article_count = {}

        for article in self.magazine_articles:
            author = article.author
            per_author_article_count[author] = per_author_article_count.get(
                author, 0) + 1

        contributing = [author for author,
                        count in per_author_article_count.items() if count > 2]

        if not contributing:
            return None

        return contributing

    def _append_to_magazine_authors(self, article, author):
        self.magazine_articles.append(article)
        if author not in self.magazine_authors:
            self.magazine_authors.append(author)

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None

        magazines_with_articles = [
            magazine for magazine in cls.all if magazine.magazine_articles]

        if not magazines_with_articles:
            return None

        top_magazine = max(magazines_with_articles,
                           key=lambda mag: len(mag.magazine_articles))

        return top_magazine
