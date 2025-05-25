class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title


class Author:
    def __init__(self, name):
        self._validate_name(name)
        self._name = name

    @property
    def name(self):
        return self._name

    def _validate_name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot modify name after initialization")
        if len(name.strip()) == 0 or not isinstance(self.name, str):
            raise ValueError("Author name must be a non-empty string.")

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    def _validate_name(self, name):
        if 2 < len(name.strip()) > 16 or not isinstance(name, str):
            raise ValueError(
                "Magazine name must be a string between 2 and 16 characters.")

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
