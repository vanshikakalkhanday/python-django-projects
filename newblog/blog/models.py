from django.db import models

class Category(models.Model):
   
   name = models.CharField(max_length=100)

   def __str__(self):
       return self.name
    

class Post(models.Model):

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    content = models.TextField()
#one post many caqtagories
    categories = models.ManyToManyField(Category)

    created_at = models.DateTimeField(auto_now_add=True)

    last_modified =models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title
    #to return first 100 characters
    def excerpt(self):
        return self.content[:100]+ "..."

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name
     
 