from pathlib import Path
import shutil


src_blog_index = "./staged-updates/index.html"
dst_blog_index = "../pperrone-website/blog/index.html"

shutil.move(src_blog_index, dst_blog_index)

src_posts_dir = "./staged-updates/posts/"
dst_posts_dir = "../pperrone-website/blog/posts/"

src_posts_dir = Path("./staged-updates/posts/").glob('*')
new_blog_posts = [x for x in src_posts_dir if x.is_file()]

for post in new_blog_posts:
    dst_post = dst_posts_dir + post.name
    shutil.move(post, dst_post)