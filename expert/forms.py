from django import forms

class FactForm(forms.Form):
    FACT_CHOICES = [
        ('Animal has feathers', 'Animal has feathers'),
        ('Animal can fly', 'Animal can fly'),
        ('Animal has fur', 'Animal has fur'),
        ('Animal gives live birth', 'Animal gives live birth'),
        ('Animal has scales', 'Animal has scales'),
        ('Animal lives in water', 'Animal lives in water'),
        ('Animal has a shell', 'Animal has a shell'),
        ('Animal is slow-moving', 'Animal is slow-moving'),
        ('Animal has long neck', 'Animal has long neck'),
        ('Animal has spots', 'Animal has spots'),
        ('Animal roars', 'Animal roars'),
        ('Animal has mane', 'Animal has mane'),
        ('Animal has stripes', 'Animal has stripes'),
        ('Animal is a large cat', 'Animal is a large cat'),
        ('Animal has a trunk', 'Animal has a trunk'),
        ('Animal has tusks', 'Animal has tusks'),
        ('Animal is small', 'Animal is small'),
        ('Animal is nocturnal', 'Animal is nocturnal'),
        ('Animal hops', 'Animal hops'),
        ('Animal has a pouch', 'Animal has a pouch'),
    ]

    facts = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FACT_CHOICES,
    )