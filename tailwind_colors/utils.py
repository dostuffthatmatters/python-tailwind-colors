def hex_to_rgb(hex_value):
    """Convert a hex color code to RGB tuple."""
    hex_value = hex_value.lstrip('#')
    lv = len(hex_value)
    return tuple(int(hex_value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb_value):
    """Convert an RGB tuple to hex color code."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb_value)


def is_valid_hex(value):
    """Check if the value is a valid hex color code."""
    return isinstance(value, str) and \
        value.startswith('#') and \
        len(value) == 7 and \
        all(c in '0123456789abcdefABCDEF' for c in value[1:])


def is_valid_rgb(value):
    """Check if the value is a valid RGB tuple."""
    return isinstance(value, tuple) and \
        len(value) == 3 and \
        all(isinstance(i, int) and 0 <= i <= 255 for i in value)
