from .colors import *


class ColorGroup:
    def __init__(self):
        # This class will hold color shades as attributes
        pass


class ColorPalette:
    SLATE = Slate
    GRAY = Gray
    ZINC = Zinc
    NEUTRAL = Neutral
    STONE = Stone
    RED = Red
    ORANGE = Orange
    AMBER = Amber
    YELLOW = Yellow
    LIME = Lime
    GREEN = Green
    EMERALD = Emerald
    TEAL = Teal
    CYAN = Cyan
    SKY = Sky
    BLUE = Blue
    INDIGO = Indigo
    VIOLET = Violet
    PURPLE = Purple
    FUCHSIA = Fuchsia
    PINK = Pink
    ROSE = Rose

    GREY = Gray

    @staticmethod
    def build_color_dictionary():
        colors_dict = {}
        for color_name, color_class in ColorPalette.__dict__.items():
            if isinstance(color_class, type):
                color_group = ColorGroup()
                for shade_name, shade_obj in color_class.__dict__.items():
                    if isinstance(shade_obj, ColorShade):
                        shade_key = shade_name.split('_')[1]
                        setattr(color_group, f"shade_{shade_key}", shade_obj)
                        colors_dict[f"{color_name.lower()}-{shade_key}"] = shade_obj
                colors_dict[color_name.lower()] = color_group
        return colors_dict

    @staticmethod
    def get(color_shade_key):
        """
        Retrieves the color shade object based on the provided key.

        This method looks up a color shade in the color dictionary created by the `build_color_dictionary` method of the
        `ColorPalette` class. It returns the `ColorShade` object associated with the given key if it exists. If the
        specified key is not found in the dictionary, it raises a `ValueError`.

        The method can be used in two ways:
        1. To directly retrieve a specific color shade (e.g., 'pink-500').
        2. To retrieve a color family object and then access a specific shade from it (e.g., 'emerald').

        Args:
            color_shade_key (str): The key corresponding to the color shade or color family to be retrieved.

        Returns:
            ColorShade: The `ColorShade` object associated with the given key, or a color family object.

        Raises:
            ValueError: If the `color_shade_key` is not found in the color dictionary.

        Example:
            # Directly retrieving a specific color shade:
            pink_500 = ColorPalette.get("pink-500")
            print(f"Pink 500 Hex: {pink_500.hex}, RGB: {pink_500.rgb}")

            # Retrieving a color family object and accessing a specific shade:
            emerald_500 = ColorPalette.get("emerald").shade_500
            print(f"Emerald 500 Hex: {emerald_500.hex}, RGB: {emerald_500.rgb}")
        """
        colors_dict = ColorPalette.build_color_dictionary()
        if color_shade_key in colors_dict:
            return colors_dict[color_shade_key]
        else:
            raise ValueError(f"Color shade '{color_shade_key}' not found.")


TailwindPalette = ColorPalette()
