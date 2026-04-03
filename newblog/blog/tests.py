from django.test import TestCase

from .models import Category, Post, Comment


class CategoryModelTest(TestCase):

    def test_category_creation(self):

        category = Category.objects.create(name="Technology")

        self.assertEqual(category.name, "Technology")

        self.assertEqual(str(category), "Technology")


class PostModelTest(TestCase):

    def setUp(self):

        self.category = Category.objects.create(name="Tech")

    def test_post_creation(self):

        post = Post.objects.create(

            title="Test Post",

            author="Vanshika",

            content="This is test content"

        )

        post.categories.add(self.category)

        self.assertEqual(post.title, "Test Post")

        self.assertEqual(post.author, "Vanshika")

        self.assertEqual(post.categories.first().name, "Tech")

        self.assertEqual(str(post), "Test Post")

    def test_excerpt_method(self):

        post = Post.objects.create(

            title="Test",

            author="Author",

            content="A" * 150

        )

        self.assertTrue(len(post.excerpt()) <= 103)  # 100 chars + "..."


class CommentModelTest(TestCase):

    def setUp(self):

        self.post = Post.objects.create(

            title="Test",

            author="Author",

            content="Content"

        )

    def test_comment_creation(self):

        comment = Comment.objects.create(

            post=self.post,

            name="User",

            body="Nice post!"

        )

        self.assertEqual(comment.post.title, "Test")

        self.assertEqual(str(comment), "User")
 