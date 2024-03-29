from extras.models.tags import Tag
from utilities.choices import ColorChoices

from startup_script_utils import load_yaml
import sys

tags = load_yaml("/opt/netbox/initializers/tags.yml")

if tags is None:
    sys.exit()

for params in tags:
    if "color" in params:
        color = params.pop("color")

        for color_tpl in ColorChoices:
            if color in color_tpl:
                params["color"] = color_tpl[0]

    tag, created = Tag.objects.get_or_create(**params)

    if created:
        print("🏷 Created tag", tag.name)
