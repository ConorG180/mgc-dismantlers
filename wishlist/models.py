from django.db import models
from django.contrib.auth.models import User

# Can't be set up as foreign keys, as these
# cannot be null and therefore wont' allow
# the user to add blank values in the wishlist.
# Therefore, just using integer fields to
# store each make/model/part id, not the
# instances of the models themselves, which
# is what the foreign key would do.


class Wishlist(models.Model):
    user = models.ManyToManyField(User)
    make_id = models.PositiveIntegerField(null=True, blank=True)
    car_model_id = models.PositiveIntegerField(null=True, blank=True)
    part_id = models.IntegerField(null=True, blank=True)
    model_year = models.IntegerField(null=True, blank=True)
    on_add = models.BooleanField()
    on_sale = models.BooleanField()

    def __str__(self):
        return f"{self.make_id} {self.car_model_id} {self.model_year} {self.part_id}"  # noqa
