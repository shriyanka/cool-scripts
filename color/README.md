# Color extension for Bootstrap for django projects

I always find it diffcult to use bootstrap in my project and creating a custom file just for changing the colors of my nav bar or text element. So created a middleware that would solve this problem of creating a another custom file and setting the color manually.

Meet SetColorMiddleware of color that easily helps you to set the html tag colors for bootstrap framework or even simple HTML

# How to use it

Download the zip file and place it in your django-project

add 'color' to your INSTALLED_APPS and 'color.middleware.SetColorMiddleware' in your MIDDLEWARE_CLASSES

Now, suppose you have a following HTML snippet using bootsrap framework

```
<div class="container-fluid">
	<nav class="navbar navbar-default navbar-fixed-top">
		<div class="container">
			<ul class="nav nav-pills pull-right" role="tablist">
				<li role="presentation" ><a href="#" class="navigation">Home</a></li>
				<li role="presentation" ><a href="#" class="navigation">Profile</a></li>
				<li role="presentation" ><a href="#" class="navigation">Messages</a></li>
			</ul>
		</div>
	</nav>
</div>
```

Now if you want to change the background color of navbar then you have to simply add {{ request.purple_lighten_2 }} inside the tag.

```
<nav class="navbar navbar-default navbar-fixed-top" {{ request.purple_lighten_2 }}>
```

If you want to change the text color of "Home" in the list you have to add {{ request.purple_text_text_lighten_4 }} inside the tag.

```
<li role="presentation" ><a href="#" class="navigation" {{ request.purple_text_text_lighten_4 }}>Home</a></li>
```

Note that we have used purple_lighten_2 for changing background and purple_text_text_lighten_4 for changing the Text color. So if you want to change the text color use the tag with _text_ in it other wise use the other one.

If you find any bug feel free to create a PR 

Special thanks to Materialize framework for the color codes. I have used it in my script. For further info visit http://materializecss.com/color.html
