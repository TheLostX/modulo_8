from django.contrib import admin
from .models import CustomerUser, Vehiculos, Parametros, Estacionamientos
from django.contrib.auth.admin import UserAdmin

@admin.register(Vehiculos)
class VehiculosAdmin(admin.ModelAdmin):
    list_display = ("patente", "estacionado")

@admin.register(Parametros)
class ParametrosAdmin(admin.ModelAdmin):
    list_display = ("id", "valor")

@admin.register(Estacionamientos)
class EstacionamientoAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_entreda", "fecha_salida", "patente", "tarifa", "minutos")


@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    model = CustomerUser
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('role',)}),  # Agrega campos personalizados
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Personalizados', {'fields': ('role',)}),  # Agrega campos personalizados al formulario de creación
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)