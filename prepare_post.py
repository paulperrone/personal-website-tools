from bs4 import BeautifulSoup
import pandas as pd
import fire
from datetime import datetime
import markdown2

class Post(object):
    
    def __init__(self, filename, title, tag):
        self.filename = filename
        self.title = title
        self.tag = tag
        self.timestamp = datetime.now()
        self.display_date = self.timestamp.strftime("%d-%b-%Y")

    def stage_new_post(self):
        self.generate_post_html()
        self.add_post_to_csv()
        #self.generate_index_html()
        #self.remove_draft()

    def generate_post_html(self):
        post_html_from_markdown = markdown2.markdown_path(f"./drafts/{self.filename}.md")
        post_content = f"""
<!DOCTYPE html>
<html>
    <head>
        <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css"
        />
        <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic"
        />
        <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css"
        />
        <link rel="stylesheet" href="../../main.css" />
    </head>
    <body>
        <p class="site-text" style="margin-top: 1em">paul perrone</p>
        <div class="container">
        <div class="row row-center">
            <div class="column">
            <div style="display: flex; justify-content: space-between">
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <a class="site-link" href="../../index.html">home</a>
                <a class="site-link" href="../../about/index.html">about</a>
                <a class="site-link" href="../index.html">blog</a>
                <a class="site-link" href="../../career/index.html">career</a>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            </div>
        </div>
        <hr />
        <div class="row">
            <div class="column"></div>
            <div class="column column-80 site-text" style="text-align: left;">
                <h1>{self.title}</h1>
                <h6>{self.timestamp} | {self.tag}</h6>
                <hr />
                <!--START BLOG POST CONTENT-->
                {post_html_from_markdown}
                <!--END BLOG POST CONTENT-->
            <p class="site-text copyright">Copyright © 2020 Paul Perrone</p>
            </div>
            <div class="column"></div>
        </div>
        </div>
    </body>
</html>
        """
        f = open(f"./staged-updates/posts/{self.filename}.html", "w")
        f.write(post_content)
        f.close()

    #filename, title, timestamp, tag
    def add_post_to_csv(self):
        all_posts = pd.read_csv("./posts.csv")
        details = [self.filename, self.title, self.timestamp, self.tag]
        post_info = pd.Series(details, index = all_posts.columns)
        all_posts = all_posts.append(post_info, ignore_index=True)
        all_posts['Date'] = pd.to_datetime(all_posts['timestamp'])
        all_posts.sort_values(by=['Date'], ascending=False)
        all_posts = all_posts.drop_duplicates(subset = ["title"], keep='first')
        all_posts.to_csv("./posts.csv", index=False)

    def generate_index_html(self):
        index_template = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <link
                rel="stylesheet"
                href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css"
                />
                <link
                rel="stylesheet"
                href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic"
                />
                <link
                rel="stylesheet"
                href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css"
                />
                <link rel="stylesheet" href="../main.css" />
            </head>
            <body>
                <p class="site-text" style="margin-top: 1em">paul perrone</p>
                <div class="container">
                <div class="row row-center">
                    <div class="column">
                    <div style="display: flex; justify-content: space-between">
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <a class="site-link" href="../index.html">home</a>
                        <a class="site-link" href="../about/index.html">about</a>
                        <a class="site-link" href="./index.html">blog</a>
                        <a class="site-link" href="../career/index.html">career</a>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                    </div>
                </div>
                <hr />
                <div class="row">
                    <div class="column"></div>
                    <div class="column column-80" style="text-align: left;">
                    <!--START LIST OF BLOG POSTS-->
                    <p><a href="./posts/test-post.html" class="blog-link">blog post 1</a></p>
                    <p><a href="./posts/" class="blog-link">blog post 2</a></p>
                    <p><a href="./posts/" class="blog-link">blog post 3</a></p>
                    <p><a href="./posts/" class="blog-link">blog post 4</a></p>
                    <!--END LIST OF BLOG POSTS-->
                    <p class="site-text copyright">Copyright © 2020 Paul Perrone</p>
                    </div>
                    <div class="column"></div>
                </div>
                </div>
            </body>
            </html>
        """
        print('test')
    
    def remove_draft(self):
        print("test")
        
        
#post_title=self.title, post_timestamp=self.timestamp, post_tag=self.tag, post_link=self.filename

if __name__ == '__main__':
  fire.Fire(Post)