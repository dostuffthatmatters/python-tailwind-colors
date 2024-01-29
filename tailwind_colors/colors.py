from .utils import *


class ColorShadeManager:
    @classmethod
    def override_shade(cls, shade_name, value):
        """
        Overrides the specified color shade with a new color value.

        This method updates the color shade of the class based on the provided value.
        If the value is a valid hexadecimal color code, it sets the color using the hex format.
        If the value is a valid RGB tuple, it sets the color using the RGB format.
        An error is raised if the shade name does not exist or if the value format is invalid.

        Args:
            shade_name (str): The name of the shade to be overridden.
            value (str or tuple): The new color value in hexadecimal or RGB format.

        Raises:
            ValueError: If the shade name is invalid or the value format is not recognized.
        """
        if hasattr(cls, shade_name):
            if is_valid_hex(value):
                setattr(cls, shade_name, ColorShade(hex_value=value))
            elif is_valid_rgb(value):
                setattr(cls, shade_name, ColorShade(rgb_value=value))
            else:
                raise ValueError("Invalid color format. Please provide a valid hex or RGB value.")
        else:
            raise ValueError(f"Invalid shade name: {shade_name}")


class ColorShade:
    def __init__(self, hex_value=None, rgb_value=None):
        self.rgb = None
        self.hex = None
        if hex_value:
            self.set_hex(hex_value)
        elif rgb_value:
            self.set_rgb(rgb_value)

    def set_hex(self, hex_value):
        self.hex = hex_value
        self.rgb = hex_to_rgb(hex_value)

    def set_rgb(self, rgb_value):
        self.rgb = rgb_value
        self.hex = rgb_to_hex(rgb_value)


class Slate(ColorShadeManager):
    shade_050 = ColorShade("#f8fafc", (248, 250, 252))
    shade_100 = ColorShade("#f1f5f9", (241, 245, 249))
    shade_200 = ColorShade("#e2e8f0", (226, 232, 240))
    shade_300 = ColorShade("#cbd5e1", (203, 213, 225))
    shade_400 = ColorShade("#94a3b8", (148, 163, 184))
    shade_500 = ColorShade("#64748b", (100, 116, 139))
    shade_600 = ColorShade("#475569", (71, 85, 105))
    shade_700 = ColorShade("#334155", (51, 65, 85))
    shade_800 = ColorShade("#1e293b", (30, 41, 59))
    shade_900 = ColorShade("#0f172a", (15, 23, 42))
    shade_950 = ColorShade("#020617", (2, 6, 23))


class Gray(ColorShadeManager):
    shade_050 = ColorShade("#f9fafb", (249, 250, 251))
    shade_100 = ColorShade("#f3f4f6", (243, 244, 246))
    shade_200 = ColorShade("#e5e7eb", (229, 231, 235))
    shade_300 = ColorShade("#d1d5db", (209, 213, 219))
    shade_400 = ColorShade("#9ca3af", (156, 163, 175))
    shade_500 = ColorShade("#6b7280", (107, 114, 128))
    shade_600 = ColorShade("#4b5563", (75, 85, 99))
    shade_700 = ColorShade("#374151", (55, 65, 81))
    shade_800 = ColorShade("#1f2937", (31, 41, 55))
    shade_900 = ColorShade("#111827", (17, 24, 39))
    shade_950 = ColorShade("#030712", (3, 7, 18))


class Zinc(ColorShadeManager):
    shade_050 = ColorShade("#fafafa", (250, 250, 250))
    shade_100 = ColorShade("#f4f4f5", (244, 244, 245))
    shade_200 = ColorShade("#e4e4e7", (228, 228, 231))
    shade_300 = ColorShade("#d4d4d8", (212, 212, 216))
    shade_400 = ColorShade("#a1a1aa", (161, 161, 170))
    shade_500 = ColorShade("#71717a", (113, 113, 122))
    shade_600 = ColorShade("#52525b", (82, 82, 91))
    shade_700 = ColorShade("#3f3f46", (63, 63, 70))
    shade_800 = ColorShade("#27272a", (39, 39, 42))
    shade_900 = ColorShade("#18181b", (24, 24, 27))
    shade_950 = ColorShade("#09090b", (9, 9, 11))


class Neutral(ColorShadeManager):
    shade_050 = ColorShade("#fafafa", (250, 250, 250))
    shade_100 = ColorShade("#f5f5f5", (245, 245, 245))
    shade_200 = ColorShade("#e5e5e5", (229, 229, 229))
    shade_300 = ColorShade("#d4d4d4", (212, 212, 212))
    shade_400 = ColorShade("#a3a3a3", (163, 163, 163))
    shade_500 = ColorShade("#737373", (115, 115, 115))
    shade_600 = ColorShade("#525252", (82, 82, 82))
    shade_700 = ColorShade("#404040", (64, 64, 64))
    shade_800 = ColorShade("#262626", (38, 38, 38))
    shade_900 = ColorShade("#171717", (23, 23, 23))
    shade_950 = ColorShade("#0a0a0a", (10, 10, 10))


class Stone(ColorShadeManager):
    shade_050 = ColorShade("#fafaf9", (250, 250, 249))
    shade_100 = ColorShade("#f5f5f4", (245, 245, 244))
    shade_200 = ColorShade("#e7e5e4", (231, 229, 228))
    shade_300 = ColorShade("#d6d3d1", (214, 211, 209))
    shade_400 = ColorShade("#a8a29e", (168, 162, 158))
    shade_500 = ColorShade("#78716c", (120, 113, 108))
    shade_600 = ColorShade("#57534e", (87, 83, 78))
    shade_700 = ColorShade("#44403c", (68, 64, 60))
    shade_800 = ColorShade("#292524", (41, 37, 36))
    shade_900 = ColorShade("#1c1917", (28, 25, 23))
    shade_950 = ColorShade("#0c0a09", (12, 10, 9))


class Red(ColorShadeManager):
    shade_050 = ColorShade("#fef2f2", (254, 242, 242))
    shade_100 = ColorShade("#fee2e2", (254, 226, 226))
    shade_200 = ColorShade("#fecaca", (254, 202, 202))
    shade_300 = ColorShade("#fca5a5", (252, 165, 165))
    shade_400 = ColorShade("#f87171", (248, 113, 113))
    shade_500 = ColorShade("#ef4444", (239, 68, 68))
    shade_600 = ColorShade("#dc2626", (220, 38, 38))
    shade_700 = ColorShade("#b91c1c", (185, 28, 28))
    shade_800 = ColorShade("#991b1b", (153, 27, 27))
    shade_900 = ColorShade("#7f1d1d", (127, 29, 29))
    shade_950 = ColorShade("#450a0a", (69, 10, 10))


class Orange(ColorShadeManager):
    shade_050 = ColorShade("#fff7ed", (255, 247, 237))
    shade_100 = ColorShade("#ffedd5", (255, 237, 213))
    shade_200 = ColorShade("#fed7aa", (254, 215, 170))
    shade_300 = ColorShade("#fdba74", (253, 186, 116))
    shade_400 = ColorShade("#fb923c", (251, 146, 60))
    shade_500 = ColorShade("#f97316", (249, 115, 22))
    shade_600 = ColorShade("#ea580c", (234, 88, 12))
    shade_700 = ColorShade("#c2410c", (194, 65, 12))
    shade_800 = ColorShade("#9a3412", (154, 52, 18))
    shade_900 = ColorShade("#7c2d12", (124, 45, 18))
    shade_950 = ColorShade("#431407", (67, 20, 7))


class Amber(ColorShadeManager):
    shade_050 = ColorShade("#fffbeb", (255, 251, 235))
    shade_100 = ColorShade("#fef3c7", (254, 243, 199))
    shade_200 = ColorShade("#fde68a", (253, 230, 138))
    shade_300 = ColorShade("#fcd34d", (252, 211, 77))
    shade_400 = ColorShade("#fbbf24", (251, 191, 36))
    shade_500 = ColorShade("#f59e0b", (245, 158, 11))
    shade_600 = ColorShade("#d97706", (217, 119, 6))
    shade_700 = ColorShade("#b45309", (180, 83, 9))
    shade_800 = ColorShade("#92400e", (146, 64, 14))
    shade_900 = ColorShade("#78350f", (120, 53, 15))
    shade_950 = ColorShade("#451a03", (69, 26, 3))


class Yellow(ColorShadeManager):
    shade_050 = ColorShade("#fefce8", (254, 252, 232))
    shade_100 = ColorShade("#fef9c3", (254, 249, 195))
    shade_200 = ColorShade("#fef08a", (254, 240, 138))
    shade_300 = ColorShade("#fde047", (253, 224, 71))
    shade_400 = ColorShade("#facc15", (250, 204, 21))
    shade_500 = ColorShade("#eab308", (234, 179, 8))
    shade_600 = ColorShade("#ca8a04", (202, 138, 4))
    shade_700 = ColorShade("#a16207", (161, 98, 7))
    shade_800 = ColorShade("#854d0e", (133, 77, 14))
    shade_900 = ColorShade("#713f12", (113, 63, 18))
    shade_950 = ColorShade("#422006", (66, 32, 6))


class Lime(ColorShadeManager):
    shade_050 = ColorShade("#f7fee7", (247, 254, 231))
    shade_100 = ColorShade("#ecfccb", (236, 252, 203))
    shade_200 = ColorShade("#d9f99d", (217, 249, 157))
    shade_300 = ColorShade("#bef264", (190, 242, 100))
    shade_400 = ColorShade("#a3e635", (163, 230, 53))
    shade_500 = ColorShade("#84cc16", (132, 204, 22))
    shade_600 = ColorShade("#65a30d", (101, 163, 13))
    shade_700 = ColorShade("#4d7c0f", (77, 124, 15))
    shade_800 = ColorShade("#3f6212", (63, 98, 18))
    shade_900 = ColorShade("#365314", (54, 83, 20))
    shade_950 = ColorShade("#1a2e05", (26, 46, 5))


class Green(ColorShadeManager):
    shade_050 = ColorShade("#f0fdf4", (240, 253, 244))
    shade_100 = ColorShade("#dcfce7", (220, 252, 231))
    shade_200 = ColorShade("#bbf7d0", (187, 247, 208))
    shade_300 = ColorShade("#86efac", (134, 239, 172))
    shade_400 = ColorShade("#4ade80", (74, 222, 128))
    shade_500 = ColorShade("#22c55e", (34, 197, 94))
    shade_600 = ColorShade("#16a34a", (22, 163, 74))
    shade_700 = ColorShade("#15803d", (21, 128, 61))
    shade_800 = ColorShade("#166534", (22, 101, 52))
    shade_900 = ColorShade("#14532d", (20, 83, 45))
    shade_950 = ColorShade("#052e16", (5, 46, 22))


class Emerald(ColorShadeManager):
    shade_050 = ColorShade("#ecfdf5", (236, 253, 245))
    shade_100 = ColorShade("#d1fae5", (209, 250, 229))
    shade_200 = ColorShade("#a7f3d0", (167, 243, 208))
    shade_300 = ColorShade("#6ee7b7", (110, 231, 183))
    shade_400 = ColorShade("#34d399", (52, 211, 153))
    shade_500 = ColorShade("#10b981", (16, 185, 129))
    shade_600 = ColorShade("#059669", (5, 150, 105))
    shade_700 = ColorShade("#047857", (4, 120, 87))
    shade_800 = ColorShade("#065f46", (6, 95, 70))
    shade_900 = ColorShade("#064e3b", (6, 78, 59))
    shade_950 = ColorShade("#022c22", (2, 44, 34))


class Teal(ColorShadeManager):
    shade_050 = ColorShade("#f0fdfa", (240, 253, 250))
    shade_100 = ColorShade("#ccfbf1", (204, 251, 241))
    shade_200 = ColorShade("#99f6e4", (153, 246, 228))
    shade_300 = ColorShade("#5eead4", (94, 234, 212))
    shade_400 = ColorShade("#2dd4bf", (45, 212, 191))
    shade_500 = ColorShade("#14b8a6", (20, 184, 166))
    shade_600 = ColorShade("#0d9488", (13, 148, 136))
    shade_700 = ColorShade("#0f766e", (15, 118, 110))
    shade_800 = ColorShade("#115e59", (17, 94, 89))
    shade_900 = ColorShade("#134e4a", (19, 78, 74))
    shade_950 = ColorShade("#042f2e", (4, 47, 46))


class Cyan(ColorShadeManager):
    shade_050 = ColorShade("#ecfeff", (236, 254, 255))
    shade_100 = ColorShade("#cffafe", (207, 250, 254))
    shade_200 = ColorShade("#a5f3fc", (165, 243, 252))
    shade_300 = ColorShade("#67e8f9", (103, 232, 249))
    shade_400 = ColorShade("#22d3ee", (34, 211, 238))
    shade_500 = ColorShade("#06b6d4", (6, 182, 212))
    shade_600 = ColorShade("#0891b2", (8, 145, 178))
    shade_700 = ColorShade("#0e7490", (14, 116, 144))
    shade_800 = ColorShade("#155e75", (21, 94, 117))
    shade_900 = ColorShade("#164e63", (22, 78, 99))
    shade_950 = ColorShade("#083344", (8, 51, 68))


class Sky(ColorShadeManager):
    shade_050 = ColorShade("#f0f9ff", (240, 249, 255))
    shade_100 = ColorShade("#e0f2fe", (224, 242, 254))
    shade_200 = ColorShade("#bae6fd", (186, 230, 253))
    shade_300 = ColorShade("#7dd3fc", (125, 211, 252))
    shade_400 = ColorShade("#38bdf8", (56, 189, 248))
    shade_500 = ColorShade("#0ea5e9", (14, 165, 233))
    shade_600 = ColorShade("#0284c7", (2, 132, 199))
    shade_700 = ColorShade("#0369a1", (3, 105, 161))
    shade_800 = ColorShade("#075985", (7, 89, 133))
    shade_900 = ColorShade("#0c4a6e", (12, 74, 110))
    shade_950 = ColorShade("#082f49", (8, 47, 73))


class Blue(ColorShadeManager):
    shade_050 = ColorShade("#eff6ff", (239, 246, 255))
    shade_100 = ColorShade("#dbeafe", (219, 234, 254))
    shade_200 = ColorShade("#bfdbfe", (191, 219, 254))
    shade_300 = ColorShade("#93c5fd", (147, 197, 253))
    shade_400 = ColorShade("#60a5fa", (96, 165, 250))
    shade_500 = ColorShade("#3b82f6", (59, 130, 246))
    shade_600 = ColorShade("#2563eb", (37, 99, 235))
    shade_700 = ColorShade("#1d4ed8", (29, 78, 216))
    shade_800 = ColorShade("#1e40af", (30, 64, 175))
    shade_900 = ColorShade("#1e3a8a", (30, 58, 138))
    shade_950 = ColorShade("#172554", (23, 37, 84))


class Indigo(ColorShadeManager):
    shade_050 = ColorShade("#eef2ff", (238, 242, 255))
    shade_100 = ColorShade("#e0e7ff", (224, 231, 255))
    shade_200 = ColorShade("#c7d2fe", (199, 210, 254))
    shade_300 = ColorShade("#a5b4fc", (165, 180, 252))
    shade_400 = ColorShade("#818cf8", (129, 140, 248))
    shade_500 = ColorShade("#6366f1", (99, 102, 241))
    shade_600 = ColorShade("#4f46e5", (79, 70, 229))
    shade_700 = ColorShade("#4338ca", (67, 56, 202))
    shade_800 = ColorShade("#3730a3", (55, 48, 163))
    shade_900 = ColorShade("#312e81", (49, 46, 129))
    shade_950 = ColorShade("#1e1b4b", (30, 27, 75))


class Violet(ColorShadeManager):
    shade_050 = ColorShade("#f5f3ff", (245, 243, 255))
    shade_100 = ColorShade("#ede9fe", (237, 233, 254))
    shade_200 = ColorShade("#ddd6fe", (221, 214, 254))
    shade_300 = ColorShade("#c4b5fd", (196, 181, 253))
    shade_400 = ColorShade("#a78bfa", (167, 139, 250))
    shade_500 = ColorShade("#8b5cf6", (139, 92, 246))
    shade_600 = ColorShade("#7c3aed", (124, 58, 237))
    shade_700 = ColorShade("#6d28d9", (109, 40, 217))
    shade_800 = ColorShade("#5b21b6", (91, 33, 182))
    shade_900 = ColorShade("#4c1d95", (76, 29, 149))
    shade_950 = ColorShade("#2e1065", (46, 16, 101))


class Purple(ColorShadeManager):
    shade_050 = ColorShade("#faf5ff", (250, 245, 255))
    shade_100 = ColorShade("#f3e8ff", (243, 232, 255))
    shade_200 = ColorShade("#e9d5ff", (233, 213, 255))
    shade_300 = ColorShade("#d8b4fe", (216, 180, 254))
    shade_400 = ColorShade("#c084fc", (192, 132, 252))
    shade_500 = ColorShade("#a855f7", (168, 85, 247))
    shade_600 = ColorShade("#9333ea", (147, 51, 234))
    shade_700 = ColorShade("#7e22ce", (126, 34, 206))
    shade_800 = ColorShade("#6b21a8", (107, 33, 168))
    shade_900 = ColorShade("#581c87", (88, 28, 135))
    shade_950 = ColorShade("#3b0764", (59, 7, 100))


class Fuchsia(ColorShadeManager):
    shade_050 = ColorShade("#fdf4ff", (253, 244, 255))
    shade_100 = ColorShade("#fae8ff", (250, 232, 255))
    shade_200 = ColorShade("#f5d0fe", (245, 208, 254))
    shade_300 = ColorShade("#f0abfc", (240, 171, 252))
    shade_400 = ColorShade("#e879f9", (232, 121, 249))
    shade_500 = ColorShade("#d946ef", (217, 70, 239))
    shade_600 = ColorShade("#c026d3", (192, 38, 211))
    shade_700 = ColorShade("#a21caf", (162, 28, 175))
    shade_800 = ColorShade("#86198f", (134, 25, 143))
    shade_900 = ColorShade("#701a75", (112, 26, 117))
    shade_950 = ColorShade("#4a044e", (74, 4, 78))


class Pink(ColorShadeManager):
    shade_050 = ColorShade("#fdf2f8", (253, 242, 248))
    shade_100 = ColorShade("#fce7f3", (252, 231, 243))
    shade_200 = ColorShade("#fbcfe8", (251, 207, 232))
    shade_300 = ColorShade("#f9a8d4", (249, 168, 212))
    shade_400 = ColorShade("#f472b6", (244, 114, 182))
    shade_500 = ColorShade("#ec4899", (236, 72, 153))
    shade_600 = ColorShade("#db2777", (219, 39, 119))
    shade_700 = ColorShade("#be185d", (190, 24, 93))
    shade_800 = ColorShade("#9d174d", (157, 23, 77))
    shade_900 = ColorShade("#831843", (131, 24, 67))
    shade_950 = ColorShade("#500724", (80, 7, 36))


class Rose(ColorShadeManager):
    shade_050 = ColorShade("#fff1f2", (255, 241, 242))
    shade_100 = ColorShade("#ffe4e6", (255, 228, 230))
    shade_200 = ColorShade("#fecdd3", (254, 205, 211))
    shade_300 = ColorShade("#fda4af", (253, 164, 175))
    shade_400 = ColorShade("#fb7185", (251, 113, 133))
    shade_500 = ColorShade("#f43f5e", (244, 63, 94))
    shade_600 = ColorShade("#e11d48", (225, 29, 72))
    shade_700 = ColorShade("#be123c", (190, 18, 60))
    shade_800 = ColorShade("#9f1239", (159, 18, 57))
    shade_900 = ColorShade("#881337", (136, 19, 55))
    shade_950 = ColorShade("#4c0519", (76, 5, 25))
