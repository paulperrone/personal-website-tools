from datetime import datetime
from pathlib import Path
import shutil

# Variables
now = datetime.now()

src_blog_index = "./staged-updates/index.html"
dst_blog_index = "../pperrone-website/index.html"

src_posts_dir = "./staged-updates/posts/"
dst_posts_dir = f"../pperrone-website/blog/{now.year}/"

# Create new blog post folder for the year if one doesn't already exist
dst_dir = Path(dst_posts_dir)
if dst_dir.exists() == False:
    dst_dir.mkdir()

# Move blog index over if a new index exists
src_index = Path(src_blog_index)
if src_index.exists():
    shutil.move(src_blog_index, dst_blog_index)

# Move all posts ready for publishing to the website
src_posts_dir = Path("./staged-updates/posts/").glob('*')
new_blog_posts = [x for x in src_posts_dir if x.is_file()]
for post in new_blog_posts:
    dst_post = dst_posts_dir + post.name
    shutil.move(post, dst_post)