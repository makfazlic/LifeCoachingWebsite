from django.db import models
from datetime import datetime 


# Create your models here.
class Configure(models.Model):
    main_banner = models.CharField(
        max_length=20,
	default="Life Coaching",
	help_text="Enter the main banner text"
    )
    main_title = models.CharField(
        max_length=50,
        default="Ana Veljković",
        help_text="Enter main webpage title"
    )
    sub_title = models.CharField(
        max_length=100,
        default="Identify, clarify and create a vision for what you want.",
        help_text="Write a short description (10 words)"
    )
    main_image = models.ImageField(
        upload_to="pics/",
        default="pics/profile.png",
        help_text="Please submit a main image"
    )




    mini_item_title_1 = models.CharField(
        max_length=20,
        default="Personal Growth",
        help_text="Enter title of the first circular item"
    )
    mini_item_descript_1 = models.CharField(
        max_length=290,
        default="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis en",
        help_text="Enter description of the first circular item"
    )
    mini_item_image_1= models.ImageField(
        upload_to="pics/",
        default="pics/sunflower.jpg",
        help_text="Please submit a mini image"
    )




    mini_item_title_2 = models.CharField(
        max_length=20,
        default="Communication Skills",
        help_text="Enter title of the second circular item"
    )
    mini_item_descript_2 = models.CharField(
        max_length=290,
        default="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis en",
        help_text="Enter description of the second circular item"
    )
    mini_item_image_2= models.ImageField(
        upload_to="pics/",
        default="pics/public_speaking.jpg",
        help_text="Please submit a mini image"
    )




    mini_item_title_3 = models.CharField(
        max_length=20,
        default="Expat Support",
        help_text="Enter title of the third circular item"
    )
    mini_item_descript_3 = models.CharField(
        max_length=290,
        default="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis en",
        help_text="Enter description of the third circular item"
    )
    mini_item_image_3= models.ImageField(
        upload_to="pics/",
        default="pics/plane.jpg",
        help_text="Please submit a mini image"
    )



    slideshow_title_1 = models.CharField(
        max_length=50,
        default="- Tony Robbins",
        help_text="Slideshow Heading description"
    )
    slideshow_banner_1 = models.CharField(
        max_length=20,
        default="Personal Growth",
        help_text="Slideshow Left Banner"
    )
    slideshow_subtitle_1 = models.CharField(
        max_length=100,
        default="Demand more from yourself than anyone else could ever expect.",
        help_text="Slideshow Subheading description"
    )
    slideshow_background_1 = models.ImageField(
        upload_to="pics/",
        default="pics/success.jpg",
        help_text="Please submit a darkened slideshow background - 1920x1080 minimum"
    )



    slideshow_title_2 = models.CharField(
        max_length=50,
        default="- James Humes",
        help_text="Slideshow Heading description"
    )
    slideshow_banner_2 = models.CharField(
        max_length=20,
        default="Communication Skills",
        help_text="Slideshow Left Banner"
    )
    slideshow_subtitle_2 = models.CharField(
        max_length=100,
        default="The art of communication is the language of leadership.",
        help_text="Slideshow Subheading description"
    )
    slideshow_background_2 = models.ImageField(
        upload_to="pics/",
        default="pics/sparrows.jpg",
        help_text="Please submit a darkened slideshow background - 1920x1080 minimum"
    )



    slideshow_title_3 = models.CharField(
        max_length=50,
        default="- Zig Ziglar",
        help_text="Slideshow Heading description"
    )
    slideshow_banner_3 = models.CharField(
        max_length=20,
        default="Expat Support",
        help_text="Slideshow Left Banner"
    )
    slideshow_subtitle_3 = models.CharField(
        max_length=100,
        default="Make a big life change is pretty scarry. But know what's even scarier? Regret.",
        help_text="Slideshow Subheading description"
    )
    slideshow_background_3 = models.ImageField(
        upload_to="pics/",
        default="pics/hands.jpg",
        help_text="Please submit a darkened slideshow background - 1920x1080 minimum"
    )



    block_title_black_1 = models.CharField(
        max_length=100,
        default="Who am I?",
        help_text="Enter black block title"
    )
    block_title_silver_1 = models.CharField(
        max_length=100,
        default="A brief overview.",
        help_text="Enter silver block title"
    )
    block_descritption_1 = models.CharField(
        max_length=250,
        default="Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.",
        help_text="Enter block discription"
    )
    block_image_1 = models.ImageField(
        upload_to="pics/",
        default="pics/me.jpg",
        help_text="Please submit a block image - 500x500px preferably"
    )



    block_title_black_2 = models.CharField(
        max_length=100,
        default="Unlock your potential.",
        help_text="Enter black block title"
    )
    block_title_silver_2 = models.CharField(
        max_length=100,
        default="And yes you can.",
        help_text="Enter silver block title"
    )
    block_descritption_2 = models.CharField(
        max_length=250,
        default="Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.",
        help_text="Enter block discription"
    )
    block_image_2 = models.ImageField(
        upload_to="pics/",
        default="pics/keyboard.jpg",
        help_text="Please submit a block image - 500x500px preferably"
    )



    block_title_black_3 = models.CharField(
        max_length=100,
        default="Want to talk?",
        help_text="Enter black block title"
    )
    block_title_silver_3 = models.CharField(
        max_length=100,
        default="This is how I work.",
        help_text="Enter silver block title"
    )
    block_descritption_3 = models.CharField(
        max_length=250,
        default="Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.",
        help_text="Enter block discription"
    )
    block_image_3 = models.ImageField(
        upload_to="pics/",
        default="pics/calendar.jpg",
        help_text="Please submit a block image - 500x500px preferably"
    )


    scroll_through_title = models.CharField(
        max_length=100,
        default="Find peace and equilibrium.",
        help_text="Enter scroll title"
    )
    scroll_through_subtitle = models.CharField(
        max_length=300,
        default="It's never too late.",
        help_text="Enter scroll subtitle"
    )
    scroll_through_image = models.ImageField(
        upload_to="pics/",
        default="pics/tree.jpg",
        help_text="Please submit a darkened slideshow background - 1920x1080 minimum"
    )

    
    def __str__(self):
        return self.main_title



class Contact(models.Model):
    name = models.CharField(
        max_length=150
    )
    email = models.EmailField(
       max_length=150 
    )
    date = models.DateTimeField(
        default=datetime.now, blank=True
    )
    message = models.CharField(
        max_length=10000
    )

    def __str__(self):
        return self.name
