from tailwind_colors import TailwindPalette as tp

# Example 1: Accessing colors
# Using any of these 2 method will return the same result.

# Method 1: Accessing a specific color shade directly
slate_100 = tp.SLATE.shade_100
print(f"Slate 100 Hex: {slate_100.hex}, RGB: {slate_100.rgb}")

# Method 2: Using the .get() method
pink_500 = tp.get("pink-500")
print(f"Pink 500 Hex: {pink_500.hex}, RGB: {pink_500.rgb}")
# or
emerald_500 = tp.get("emerald").shade_500
print(f"Emerald 500 Hex: {emerald_500.hex}, RGB: {emerald_500.rgb}")


# Example 2: Overriding a color shade

# Using hex value
tp.SLATE.override_shade('shade_100', value="#abcdef")
updated_slate_100 = tp.SLATE.shade_100  # or tp.get('slate-100')
print(f"Updated Slate 100 Hex: {updated_slate_100.hex}, RGB: {updated_slate_100.rgb}")

# OR using RGB value
tp.SLATE.override_shade('shade_200', value=(12, 34, 56))
updated_slate_200 = tp.SLATE.shade_200  # or tp.get('slate-200')
print(f"Updated Slate 200 Hex: {updated_slate_200.hex}, RGB: {updated_slate_200.rgb}")



