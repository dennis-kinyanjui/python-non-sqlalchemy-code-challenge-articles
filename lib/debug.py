from author import Author
from magazine import Magazine
from article import Article

# Create sample instances to test
author1 = Author("John Doe")
magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Health Weekly", "Health")

article1 = author1.add_article(magazine1, "The Future of AI")
article2 = author1.add_article(magazine2, "Healthy Living in 2024")

# Check methods
print(author1.name)
print(author1.articles())
print(author1.magazines())
print(author1.topic_areas())

print(magazine1.name)
print(magazine1.articles())
print(magazine1.contributors())
print(magazine1.article_titles())
print(magazine1.contributing_authors())

print(Article.top_publisher())
