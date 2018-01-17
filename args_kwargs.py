blog_1 = "I am so awesome"
blog_2 = "Cars are cool"
blog_3 = "Aww look at my cat"

def blog_posts(*args):
    for post in args:
        print(post)

def blog_posts2(regular_arg, *args):
    print(regular_arg)
    for post in args:
        print(post)

def blog_posts3(**kwargs):
    for title, post in kwargs.items():
        print(title, post)

#blog_posts2("my blogs: ", blog_1, blog_2, blog_3)

blog_posts3(blog_1="I am so awesome",
            blog_2="Cars are cool",
            blog_3="Awww look at my cat")
