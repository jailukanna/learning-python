# Optional Assignment: Django AJAX

You'll be incorporating a AJAX into a very basic Django app. Follow the steps below and refer back to the AJAX section of web fundamentals if you need help.

To Do:
1. Create a new project capable of serving a single view when the root route is requested.

2. Create a static directory inside your app directory. The structure here will be very similar to templates. Here's an example file path: my_app/static/my_app/main.js

3. Link to static in your templates. At the top of your head section in your html document add the following: {% load static %}. Now, you can use the static variable as a way of directing Django to your static documents. Like so: <script type="text/javascript" src="{% static "my_app/js/main.js" %}"></script>

4. Make sure your static document is linked. Test it by console logging or sending an alert pop-up.

5. We'll be using jQuery. Link to the CDN

6. Layout your template like the wireframe shown below.

7. Have 2 routes: one to load index and another to send a response.

8. Have only one template. When the button is clicked, send a $.get() request to your Django server to your second route, /message.

9. Have your server send back an HTTP response. How will that response be available to you in your JavaScript file? Refer back to AJAX in web fundamentals. It doesn't matter whether the response comes from your server or someone else's. You will access it the same way.

10. Have the message you got back from your server appear below the button.

11. Feel free to experiment! Try adding other elements to your page using AJAX! Don't spend more than another hour playing around.

*See wireframe.png for more information.*
