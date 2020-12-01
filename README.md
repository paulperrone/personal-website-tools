# personal-website-tools

personal-website-tools

## Prerequisites  

You must have the ./pperrone-website/ directory in the same directory as ./personal-website-tools/  

## Steps to Publish a Blog Post  

Create a blog post in a markdown file in the ./drafts/ directory  
Run the prepare_post.py script in the command line (tag argument is optional)  
```python prepare_post.py stage_new_post --filename="<YOUR-FILENAME>" --title="<YOUR-TITLE>" --tag="<YOUR-TAG>"```  

* The filename parameter should equal the name of your markdown file  
* The filename parameter should not have the file extension attached  
* The title parameter should equal the title you want your post to have on the website  
* The tag parameter indicates the post type  

Run the update_website.py script in the command line  
```python update_website.py```  
Switch to the pperrone-website directory in the command line  
Push your changes in pperrone-website to GitHub  
Netlify will pick up the changes and push them to your domain
