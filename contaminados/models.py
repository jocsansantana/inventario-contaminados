from django.db import models

class BultoContaminado(models.Model):
    # Opciones fijas para Tipo de Material
    class TipoMaterial(models.TextChoices):
        POLIETILENO = 'PE', 'Polietileno (PE)'
        POLIPROPILENO = 'PP', 'Polipropileno (PP)'
        MEZCLA = 'MEZCLA', 'Mezcla PE/PP'
        MB = 'MASTERBATCH', 'MB'
        OTRO = 'OTRO', 'Otro Material'

    # Opciones fijas para Subtipo / Grado
    class SubtipoMaterial(models.TextChoices):
        ALTA_DENSIDAD = 'HDPE', 'Alta Densidad (HDPE)'
        BAJA_DENSIDAD = 'LDPE', 'Baja Densidad (LDPE)'
        PP_HOMO = 'PP_HOMO', 'Polipropileno Homopolímero'
        PP_COPO = 'PP_COPO', 'Polipropileno Copolímero'

    # Opciones fijas para Causa de Contaminación
    class CausaContaminacion(models.TextChoices):
        POLVO_TIERRA = 'POLVO', 'Polvo / Tierra'
        ACEITE_GRASA = 'ACEITE', 'Aceite / Grasa'
        MEZCLA_COLOR = 'COLOR', 'Mezcla de Color / Degradado'
        MATERIAL_EXTRAÑO = 'EXTRAÑO', 'Material Extraño / Metal'
        HUMEDAD = 'HUMEDAD', 'Humedad Excesiva'
        OTRO = 'OTRO', 'Otras Causas'

    # --- CAMPOS DE LA TABLA ---
    # ✅ Se removió 'primary_key=True' para permitir códigos repetidos.
    codigo = models.CharField(
        max_length=50, 
        verbose_name="Código / Lote"
    )
    tipo_material = models.CharField(
        max_length=20, 
        choices=TipoMaterial.choices, 
        verbose_name="Tipo de Material"
    )
    subtipo_material = models.CharField(
        max_length=20, 
        choices=SubtipoMaterial.choices, 
        verbose_name="Subtipo / Grado"
    )
    causa_contaminacion = models.CharField(
        max_length=20, 
        choices=CausaContaminacion.choices, 
        verbose_name="Causa de Contaminación"
    )
    fuente_origen = models.CharField(
        max_length=150, 
        verbose_name="Fuente de Origen",
        blank=True,
        null=True
    )
    peso_neto_kg = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Peso Neto (kg)"
    )
    observaciones = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Observaciones"
    )
    fecha_registro = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Fecha de Registro"
    )

    class Meta:
        db_table = 'bultos_contaminados'
        verbose_name = 'Bulto Contaminado'
        verbose_name_plural = 'Bultos Contaminados'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.codigo} - {self.get_tipo_material_display()} ({self.peso_neto_kg} kg)"