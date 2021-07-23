from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,

)
from .models import EmployeeModel


class EmployeeAdmin(ModelAdmin):
    model = EmployeeModel
    menu_label = "Employee"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name_of_employee",
                    "position_of_employee",
                    "img_of_employee",
                    "introduction_of_employee",
    )
    search_fields = ("name_of_employee")

modeladmin_register(EmployeeAdmin)
