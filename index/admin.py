from django.contrib import admin

# Register your models here.
from index.models import *

admin.site.register([profile, testimonial,
                     resumetitle, Resume,
                     myfield, client,
                     project,myskills
                     ])
