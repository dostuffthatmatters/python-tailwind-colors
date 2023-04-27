
from typing import Literal

__version__ = "1.0.1"


class TAILWIND_COLORS_HEX:
    """
    Provides all colors from TailwindCSS as strings.

    ```python
    print(TAILWIND_COLORS.AMBER_600)
    # prints `#d97706`
    ```
    """
        
    SLATE_050: Literal['#f8fafc'] = '#f8fafc'
    SLATE_100: Literal['#f1f5f9'] = '#f1f5f9'
    SLATE_200: Literal['#e2e8f0'] = '#e2e8f0'
    SLATE_300: Literal['#cbd5e1'] = '#cbd5e1'
    SLATE_400: Literal['#94a3b8'] = '#94a3b8'
    SLATE_500: Literal['#64748b'] = '#64748b'
    SLATE_600: Literal['#475569'] = '#475569'
    SLATE_700: Literal['#334155'] = '#334155'
    SLATE_800: Literal['#1e293b'] = '#1e293b'
    SLATE_900: Literal['#0f172a'] = '#0f172a'
    SLATE_950: Literal['#020617'] = '#020617'

    GRAY_050: Literal['#f9fafb'] = '#f9fafb'
    GRAY_100: Literal['#f3f4f6'] = '#f3f4f6'
    GRAY_200: Literal['#e5e7eb'] = '#e5e7eb'
    GRAY_300: Literal['#d1d5db'] = '#d1d5db'
    GRAY_400: Literal['#9ca3af'] = '#9ca3af'
    GRAY_500: Literal['#6b7280'] = '#6b7280'
    GRAY_600: Literal['#4b5563'] = '#4b5563'
    GRAY_700: Literal['#374151'] = '#374151'
    GRAY_800: Literal['#1f2937'] = '#1f2937'
    GRAY_900: Literal['#111827'] = '#111827'
    GRAY_950: Literal['#030712'] = '#030712'

    ZINC_050: Literal['#fafafa'] = '#fafafa'
    ZINC_100: Literal['#f4f4f5'] = '#f4f4f5'
    ZINC_200: Literal['#e4e4e7'] = '#e4e4e7'
    ZINC_300: Literal['#d4d4d8'] = '#d4d4d8'
    ZINC_400: Literal['#a1a1aa'] = '#a1a1aa'
    ZINC_500: Literal['#71717a'] = '#71717a'
    ZINC_600: Literal['#52525b'] = '#52525b'
    ZINC_700: Literal['#3f3f46'] = '#3f3f46'
    ZINC_800: Literal['#27272a'] = '#27272a'
    ZINC_900: Literal['#18181b'] = '#18181b'
    ZINC_950: Literal['#09090b'] = '#09090b'

    NEUTRAL_050: Literal['#fafafa'] = '#fafafa'
    NEUTRAL_100: Literal['#f5f5f5'] = '#f5f5f5'
    NEUTRAL_200: Literal['#e5e5e5'] = '#e5e5e5'
    NEUTRAL_300: Literal['#d4d4d4'] = '#d4d4d4'
    NEUTRAL_400: Literal['#a3a3a3'] = '#a3a3a3'
    NEUTRAL_500: Literal['#737373'] = '#737373'
    NEUTRAL_600: Literal['#525252'] = '#525252'
    NEUTRAL_700: Literal['#404040'] = '#404040'
    NEUTRAL_800: Literal['#262626'] = '#262626'
    NEUTRAL_900: Literal['#171717'] = '#171717'
    NEUTRAL_950: Literal['#0a0a0a'] = '#0a0a0a'

    STONE_050: Literal['#fafaf9'] = '#fafaf9'
    STONE_100: Literal['#f5f5f4'] = '#f5f5f4'
    STONE_200: Literal['#e7e5e4'] = '#e7e5e4'
    STONE_300: Literal['#d6d3d1'] = '#d6d3d1'
    STONE_400: Literal['#a8a29e'] = '#a8a29e'
    STONE_500: Literal['#78716c'] = '#78716c'
    STONE_600: Literal['#57534e'] = '#57534e'
    STONE_700: Literal['#44403c'] = '#44403c'
    STONE_800: Literal['#292524'] = '#292524'
    STONE_900: Literal['#1c1917'] = '#1c1917'
    STONE_950: Literal['#0c0a09'] = '#0c0a09'

    RED_050: Literal['#fef2f2'] = '#fef2f2'
    RED_100: Literal['#fee2e2'] = '#fee2e2'
    RED_200: Literal['#fecaca'] = '#fecaca'
    RED_300: Literal['#fca5a5'] = '#fca5a5'
    RED_400: Literal['#f87171'] = '#f87171'
    RED_500: Literal['#ef4444'] = '#ef4444'
    RED_600: Literal['#dc2626'] = '#dc2626'
    RED_700: Literal['#b91c1c'] = '#b91c1c'
    RED_800: Literal['#991b1b'] = '#991b1b'
    RED_900: Literal['#7f1d1d'] = '#7f1d1d'
    RED_950: Literal['#450a0a'] = '#450a0a'

    ORANGE_050: Literal['#fff7ed'] = '#fff7ed'
    ORANGE_100: Literal['#ffedd5'] = '#ffedd5'
    ORANGE_200: Literal['#fed7aa'] = '#fed7aa'
    ORANGE_300: Literal['#fdba74'] = '#fdba74'
    ORANGE_400: Literal['#fb923c'] = '#fb923c'
    ORANGE_500: Literal['#f97316'] = '#f97316'
    ORANGE_600: Literal['#ea580c'] = '#ea580c'
    ORANGE_700: Literal['#c2410c'] = '#c2410c'
    ORANGE_800: Literal['#9a3412'] = '#9a3412'
    ORANGE_900: Literal['#7c2d12'] = '#7c2d12'
    ORANGE_950: Literal['#431407'] = '#431407'

    AMBER_050: Literal['#fffbeb'] = '#fffbeb'
    AMBER_100: Literal['#fef3c7'] = '#fef3c7'
    AMBER_200: Literal['#fde68a'] = '#fde68a'
    AMBER_300: Literal['#fcd34d'] = '#fcd34d'
    AMBER_400: Literal['#fbbf24'] = '#fbbf24'
    AMBER_500: Literal['#f59e0b'] = '#f59e0b'
    AMBER_600: Literal['#d97706'] = '#d97706'
    AMBER_700: Literal['#b45309'] = '#b45309'
    AMBER_800: Literal['#92400e'] = '#92400e'
    AMBER_900: Literal['#78350f'] = '#78350f'
    AMBER_950: Literal['#451a03'] = '#451a03'

    YELLOW_050: Literal['#fefce8'] = '#fefce8'
    YELLOW_100: Literal['#fef9c3'] = '#fef9c3'
    YELLOW_200: Literal['#fef08a'] = '#fef08a'
    YELLOW_300: Literal['#fde047'] = '#fde047'
    YELLOW_400: Literal['#facc15'] = '#facc15'
    YELLOW_500: Literal['#eab308'] = '#eab308'
    YELLOW_600: Literal['#ca8a04'] = '#ca8a04'
    YELLOW_700: Literal['#a16207'] = '#a16207'
    YELLOW_800: Literal['#854d0e'] = '#854d0e'
    YELLOW_900: Literal['#713f12'] = '#713f12'
    YELLOW_950: Literal['#422006'] = '#422006'

    LIME_050: Literal['#f7fee7'] = '#f7fee7'
    LIME_100: Literal['#ecfccb'] = '#ecfccb'
    LIME_200: Literal['#d9f99d'] = '#d9f99d'
    LIME_300: Literal['#bef264'] = '#bef264'
    LIME_400: Literal['#a3e635'] = '#a3e635'
    LIME_500: Literal['#84cc16'] = '#84cc16'
    LIME_600: Literal['#65a30d'] = '#65a30d'
    LIME_700: Literal['#4d7c0f'] = '#4d7c0f'
    LIME_800: Literal['#3f6212'] = '#3f6212'
    LIME_900: Literal['#365314'] = '#365314'
    LIME_950: Literal['#1a2e05'] = '#1a2e05'

    GREEN_050: Literal['#f0fdf4'] = '#f0fdf4'
    GREEN_100: Literal['#dcfce7'] = '#dcfce7'
    GREEN_200: Literal['#bbf7d0'] = '#bbf7d0'
    GREEN_300: Literal['#86efac'] = '#86efac'
    GREEN_400: Literal['#4ade80'] = '#4ade80'
    GREEN_500: Literal['#22c55e'] = '#22c55e'
    GREEN_600: Literal['#16a34a'] = '#16a34a'
    GREEN_700: Literal['#15803d'] = '#15803d'
    GREEN_800: Literal['#166534'] = '#166534'
    GREEN_900: Literal['#14532d'] = '#14532d'
    GREEN_950: Literal['#052e16'] = '#052e16'

    EMERALD_050: Literal['#ecfdf5'] = '#ecfdf5'
    EMERALD_100: Literal['#d1fae5'] = '#d1fae5'
    EMERALD_200: Literal['#a7f3d0'] = '#a7f3d0'
    EMERALD_300: Literal['#6ee7b7'] = '#6ee7b7'
    EMERALD_400: Literal['#34d399'] = '#34d399'
    EMERALD_500: Literal['#10b981'] = '#10b981'
    EMERALD_600: Literal['#059669'] = '#059669'
    EMERALD_700: Literal['#047857'] = '#047857'
    EMERALD_800: Literal['#065f46'] = '#065f46'
    EMERALD_900: Literal['#064e3b'] = '#064e3b'
    EMERALD_950: Literal['#022c22'] = '#022c22'

    TEAL_050: Literal['#f0fdfa'] = '#f0fdfa'
    TEAL_100: Literal['#ccfbf1'] = '#ccfbf1'
    TEAL_200: Literal['#99f6e4'] = '#99f6e4'
    TEAL_300: Literal['#5eead4'] = '#5eead4'
    TEAL_400: Literal['#2dd4bf'] = '#2dd4bf'
    TEAL_500: Literal['#14b8a6'] = '#14b8a6'
    TEAL_600: Literal['#0d9488'] = '#0d9488'
    TEAL_700: Literal['#0f766e'] = '#0f766e'
    TEAL_800: Literal['#115e59'] = '#115e59'
    TEAL_900: Literal['#134e4a'] = '#134e4a'
    TEAL_950: Literal['#042f2e'] = '#042f2e'

    CYAN_050: Literal['#ecfeff'] = '#ecfeff'
    CYAN_100: Literal['#cffafe'] = '#cffafe'
    CYAN_200: Literal['#a5f3fc'] = '#a5f3fc'
    CYAN_300: Literal['#67e8f9'] = '#67e8f9'
    CYAN_400: Literal['#22d3ee'] = '#22d3ee'
    CYAN_500: Literal['#06b6d4'] = '#06b6d4'
    CYAN_600: Literal['#0891b2'] = '#0891b2'
    CYAN_700: Literal['#0e7490'] = '#0e7490'
    CYAN_800: Literal['#155e75'] = '#155e75'
    CYAN_900: Literal['#164e63'] = '#164e63'
    CYAN_950: Literal['#083344'] = '#083344'

    SKY_050: Literal['#f0f9ff'] = '#f0f9ff'
    SKY_100: Literal['#e0f2fe'] = '#e0f2fe'
    SKY_200: Literal['#bae6fd'] = '#bae6fd'
    SKY_300: Literal['#7dd3fc'] = '#7dd3fc'
    SKY_400: Literal['#38bdf8'] = '#38bdf8'
    SKY_500: Literal['#0ea5e9'] = '#0ea5e9'
    SKY_600: Literal['#0284c7'] = '#0284c7'
    SKY_700: Literal['#0369a1'] = '#0369a1'
    SKY_800: Literal['#075985'] = '#075985'
    SKY_900: Literal['#0c4a6e'] = '#0c4a6e'
    SKY_950: Literal['#082f49'] = '#082f49'

    BLUE_050: Literal['#eff6ff'] = '#eff6ff'
    BLUE_100: Literal['#dbeafe'] = '#dbeafe'
    BLUE_200: Literal['#bfdbfe'] = '#bfdbfe'
    BLUE_300: Literal['#93c5fd'] = '#93c5fd'
    BLUE_400: Literal['#60a5fa'] = '#60a5fa'
    BLUE_500: Literal['#3b82f6'] = '#3b82f6'
    BLUE_600: Literal['#2563eb'] = '#2563eb'
    BLUE_700: Literal['#1d4ed8'] = '#1d4ed8'
    BLUE_800: Literal['#1e40af'] = '#1e40af'
    BLUE_900: Literal['#1e3a8a'] = '#1e3a8a'
    BLUE_950: Literal['#172554'] = '#172554'

    INDIGO_050: Literal['#eef2ff'] = '#eef2ff'
    INDIGO_100: Literal['#e0e7ff'] = '#e0e7ff'
    INDIGO_200: Literal['#c7d2fe'] = '#c7d2fe'
    INDIGO_300: Literal['#a5b4fc'] = '#a5b4fc'
    INDIGO_400: Literal['#818cf8'] = '#818cf8'
    INDIGO_500: Literal['#6366f1'] = '#6366f1'
    INDIGO_600: Literal['#4f46e5'] = '#4f46e5'
    INDIGO_700: Literal['#4338ca'] = '#4338ca'
    INDIGO_800: Literal['#3730a3'] = '#3730a3'
    INDIGO_900: Literal['#312e81'] = '#312e81'
    INDIGO_950: Literal['#1e1b4b'] = '#1e1b4b'

    VIOLET_050: Literal['#f5f3ff'] = '#f5f3ff'
    VIOLET_100: Literal['#ede9fe'] = '#ede9fe'
    VIOLET_200: Literal['#ddd6fe'] = '#ddd6fe'
    VIOLET_300: Literal['#c4b5fd'] = '#c4b5fd'
    VIOLET_400: Literal['#a78bfa'] = '#a78bfa'
    VIOLET_500: Literal['#8b5cf6'] = '#8b5cf6'
    VIOLET_600: Literal['#7c3aed'] = '#7c3aed'
    VIOLET_700: Literal['#6d28d9'] = '#6d28d9'
    VIOLET_800: Literal['#5b21b6'] = '#5b21b6'
    VIOLET_900: Literal['#4c1d95'] = '#4c1d95'
    VIOLET_950: Literal['#2e1065'] = '#2e1065'

    PURPLE_050: Literal['#faf5ff'] = '#faf5ff'
    PURPLE_100: Literal['#f3e8ff'] = '#f3e8ff'
    PURPLE_200: Literal['#e9d5ff'] = '#e9d5ff'
    PURPLE_300: Literal['#d8b4fe'] = '#d8b4fe'
    PURPLE_400: Literal['#c084fc'] = '#c084fc'
    PURPLE_500: Literal['#a855f7'] = '#a855f7'
    PURPLE_600: Literal['#9333ea'] = '#9333ea'
    PURPLE_700: Literal['#7e22ce'] = '#7e22ce'
    PURPLE_800: Literal['#6b21a8'] = '#6b21a8'
    PURPLE_900: Literal['#581c87'] = '#581c87'
    PURPLE_950: Literal['#3b0764'] = '#3b0764'

    FUCHSIA_050: Literal['#fdf4ff'] = '#fdf4ff'
    FUCHSIA_100: Literal['#fae8ff'] = '#fae8ff'
    FUCHSIA_200: Literal['#f5d0fe'] = '#f5d0fe'
    FUCHSIA_300: Literal['#f0abfc'] = '#f0abfc'
    FUCHSIA_400: Literal['#e879f9'] = '#e879f9'
    FUCHSIA_500: Literal['#d946ef'] = '#d946ef'
    FUCHSIA_600: Literal['#c026d3'] = '#c026d3'
    FUCHSIA_700: Literal['#a21caf'] = '#a21caf'
    FUCHSIA_800: Literal['#86198f'] = '#86198f'
    FUCHSIA_900: Literal['#701a75'] = '#701a75'
    FUCHSIA_950: Literal['#4a044e'] = '#4a044e'

    PINK_050: Literal['#fdf2f8'] = '#fdf2f8'
    PINK_100: Literal['#fce7f3'] = '#fce7f3'
    PINK_200: Literal['#fbcfe8'] = '#fbcfe8'
    PINK_300: Literal['#f9a8d4'] = '#f9a8d4'
    PINK_400: Literal['#f472b6'] = '#f472b6'
    PINK_500: Literal['#ec4899'] = '#ec4899'
    PINK_600: Literal['#db2777'] = '#db2777'
    PINK_700: Literal['#be185d'] = '#be185d'
    PINK_800: Literal['#9d174d'] = '#9d174d'
    PINK_900: Literal['#831843'] = '#831843'
    PINK_950: Literal['#500724'] = '#500724'

    ROSE_050: Literal['#fff1f2'] = '#fff1f2'
    ROSE_100: Literal['#ffe4e6'] = '#ffe4e6'
    ROSE_200: Literal['#fecdd3'] = '#fecdd3'
    ROSE_300: Literal['#fda4af'] = '#fda4af'
    ROSE_400: Literal['#fb7185'] = '#fb7185'
    ROSE_500: Literal['#f43f5e'] = '#f43f5e'
    ROSE_600: Literal['#e11d48'] = '#e11d48'
    ROSE_700: Literal['#be123c'] = '#be123c'
    ROSE_800: Literal['#9f1239'] = '#9f1239'
    ROSE_900: Literal['#881337'] = '#881337'
    ROSE_950: Literal['#4c0519'] = '#4c0519'


class TAILWIND_COLORS_RGB:
    """
    Provides all colors from TailwindCSS as strings.

    ```python
    print(TAILWIND_COLORS_RGB.AMBER_600)
    # prints (217, 119, 6)
    ```
    """
    
    SLATE_050: tuple[Literal[248], Literal[250], Literal[252]] = (248, 250, 252)
    SLATE_100: tuple[Literal[241], Literal[245], Literal[249]] = (241, 245, 249)
    SLATE_200: tuple[Literal[226], Literal[232], Literal[240]] = (226, 232, 240)
    SLATE_300: tuple[Literal[203], Literal[213], Literal[225]] = (203, 213, 225)
    SLATE_400: tuple[Literal[148], Literal[163], Literal[184]] = (148, 163, 184)
    SLATE_500: tuple[Literal[100], Literal[116], Literal[139]] = (100, 116, 139)
    SLATE_600: tuple[Literal[71], Literal[85], Literal[105]] = (71, 85, 105)
    SLATE_700: tuple[Literal[51], Literal[65], Literal[85]] = (51, 65, 85)
    SLATE_800: tuple[Literal[30], Literal[41], Literal[59]] = (30, 41, 59)
    SLATE_900: tuple[Literal[15], Literal[23], Literal[42]] = (15, 23, 42)
    SLATE_950: tuple[Literal[2], Literal[6], Literal[23]] = (2, 6, 23)

    GRAY_050: tuple[Literal[249], Literal[250], Literal[251]] = (249, 250, 251)
    GRAY_100: tuple[Literal[243], Literal[244], Literal[246]] = (243, 244, 246)
    GRAY_200: tuple[Literal[229], Literal[231], Literal[235]] = (229, 231, 235)
    GRAY_300: tuple[Literal[209], Literal[213], Literal[219]] = (209, 213, 219)
    GRAY_400: tuple[Literal[156], Literal[163], Literal[175]] = (156, 163, 175)
    GRAY_500: tuple[Literal[107], Literal[114], Literal[128]] = (107, 114, 128)
    GRAY_600: tuple[Literal[75], Literal[85], Literal[99]] = (75, 85, 99)
    GRAY_700: tuple[Literal[55], Literal[65], Literal[81]] = (55, 65, 81)
    GRAY_800: tuple[Literal[31], Literal[41], Literal[55]] = (31, 41, 55)
    GRAY_900: tuple[Literal[17], Literal[24], Literal[39]] = (17, 24, 39)
    GRAY_950: tuple[Literal[3], Literal[7], Literal[18]] = (3, 7, 18)

    ZINC_050: tuple[Literal[250], Literal[250], Literal[250]] = (250, 250, 250)
    ZINC_100: tuple[Literal[244], Literal[244], Literal[245]] = (244, 244, 245)
    ZINC_200: tuple[Literal[228], Literal[228], Literal[231]] = (228, 228, 231)
    ZINC_300: tuple[Literal[212], Literal[212], Literal[216]] = (212, 212, 216)
    ZINC_400: tuple[Literal[161], Literal[161], Literal[170]] = (161, 161, 170)
    ZINC_500: tuple[Literal[113], Literal[113], Literal[122]] = (113, 113, 122)
    ZINC_600: tuple[Literal[82], Literal[82], Literal[91]] = (82, 82, 91)
    ZINC_700: tuple[Literal[63], Literal[63], Literal[70]] = (63, 63, 70)
    ZINC_800: tuple[Literal[39], Literal[39], Literal[42]] = (39, 39, 42)
    ZINC_900: tuple[Literal[24], Literal[24], Literal[27]] = (24, 24, 27)
    ZINC_950: tuple[Literal[9], Literal[9], Literal[11]] = (9, 9, 11)

    NEUTRAL_050: tuple[Literal[250], Literal[250], Literal[250]] = (250, 250, 250)
    NEUTRAL_100: tuple[Literal[245], Literal[245], Literal[245]] = (245, 245, 245)
    NEUTRAL_200: tuple[Literal[229], Literal[229], Literal[229]] = (229, 229, 229)
    NEUTRAL_300: tuple[Literal[212], Literal[212], Literal[212]] = (212, 212, 212)
    NEUTRAL_400: tuple[Literal[163], Literal[163], Literal[163]] = (163, 163, 163)
    NEUTRAL_500: tuple[Literal[115], Literal[115], Literal[115]] = (115, 115, 115)
    NEUTRAL_600: tuple[Literal[82], Literal[82], Literal[82]] = (82, 82, 82)
    NEUTRAL_700: tuple[Literal[64], Literal[64], Literal[64]] = (64, 64, 64)
    NEUTRAL_800: tuple[Literal[38], Literal[38], Literal[38]] = (38, 38, 38)
    NEUTRAL_900: tuple[Literal[23], Literal[23], Literal[23]] = (23, 23, 23)
    NEUTRAL_950: tuple[Literal[10], Literal[10], Literal[10]] = (10, 10, 10)

    STONE_050: tuple[Literal[250], Literal[250], Literal[249]] = (250, 250, 249)
    STONE_100: tuple[Literal[245], Literal[245], Literal[244]] = (245, 245, 244)
    STONE_200: tuple[Literal[231], Literal[229], Literal[228]] = (231, 229, 228)
    STONE_300: tuple[Literal[214], Literal[211], Literal[209]] = (214, 211, 209)
    STONE_400: tuple[Literal[168], Literal[162], Literal[158]] = (168, 162, 158)
    STONE_500: tuple[Literal[120], Literal[113], Literal[108]] = (120, 113, 108)
    STONE_600: tuple[Literal[87], Literal[83], Literal[78]] = (87, 83, 78)
    STONE_700: tuple[Literal[68], Literal[64], Literal[60]] = (68, 64, 60)
    STONE_800: tuple[Literal[41], Literal[37], Literal[36]] = (41, 37, 36)
    STONE_900: tuple[Literal[28], Literal[25], Literal[23]] = (28, 25, 23)
    STONE_950: tuple[Literal[12], Literal[10], Literal[9]] = (12, 10, 9)

    RED_050: tuple[Literal[254], Literal[242], Literal[242]] = (254, 242, 242)
    RED_100: tuple[Literal[254], Literal[226], Literal[226]] = (254, 226, 226)
    RED_200: tuple[Literal[254], Literal[202], Literal[202]] = (254, 202, 202)
    RED_300: tuple[Literal[252], Literal[165], Literal[165]] = (252, 165, 165)
    RED_400: tuple[Literal[248], Literal[113], Literal[113]] = (248, 113, 113)
    RED_500: tuple[Literal[239], Literal[68], Literal[68]] = (239, 68, 68)
    RED_600: tuple[Literal[220], Literal[38], Literal[38]] = (220, 38, 38)
    RED_700: tuple[Literal[185], Literal[28], Literal[28]] = (185, 28, 28)
    RED_800: tuple[Literal[153], Literal[27], Literal[27]] = (153, 27, 27)
    RED_900: tuple[Literal[127], Literal[29], Literal[29]] = (127, 29, 29)
    RED_950: tuple[Literal[69], Literal[10], Literal[10]] = (69, 10, 10)

    ORANGE_050: tuple[Literal[255], Literal[247], Literal[237]] = (255, 247, 237)
    ORANGE_100: tuple[Literal[255], Literal[237], Literal[213]] = (255, 237, 213)
    ORANGE_200: tuple[Literal[254], Literal[215], Literal[170]] = (254, 215, 170)
    ORANGE_300: tuple[Literal[253], Literal[186], Literal[116]] = (253, 186, 116)
    ORANGE_400: tuple[Literal[251], Literal[146], Literal[60]] = (251, 146, 60)
    ORANGE_500: tuple[Literal[249], Literal[115], Literal[22]] = (249, 115, 22)
    ORANGE_600: tuple[Literal[234], Literal[88], Literal[12]] = (234, 88, 12)
    ORANGE_700: tuple[Literal[194], Literal[65], Literal[12]] = (194, 65, 12)
    ORANGE_800: tuple[Literal[154], Literal[52], Literal[18]] = (154, 52, 18)
    ORANGE_900: tuple[Literal[124], Literal[45], Literal[18]] = (124, 45, 18)
    ORANGE_950: tuple[Literal[67], Literal[20], Literal[7]] = (67, 20, 7)

    AMBER_050: tuple[Literal[255], Literal[251], Literal[235]] = (255, 251, 235)
    AMBER_100: tuple[Literal[254], Literal[243], Literal[199]] = (254, 243, 199)
    AMBER_200: tuple[Literal[253], Literal[230], Literal[138]] = (253, 230, 138)
    AMBER_300: tuple[Literal[252], Literal[211], Literal[77]] = (252, 211, 77)
    AMBER_400: tuple[Literal[251], Literal[191], Literal[36]] = (251, 191, 36)
    AMBER_500: tuple[Literal[245], Literal[158], Literal[11]] = (245, 158, 11)
    AMBER_600: tuple[Literal[217], Literal[119], Literal[6]] = (217, 119, 6)
    AMBER_700: tuple[Literal[180], Literal[83], Literal[9]] = (180, 83, 9)
    AMBER_800: tuple[Literal[146], Literal[64], Literal[14]] = (146, 64, 14)
    AMBER_900: tuple[Literal[120], Literal[53], Literal[15]] = (120, 53, 15)
    AMBER_950: tuple[Literal[69], Literal[26], Literal[3]] = (69, 26, 3)

    YELLOW_050: tuple[Literal[254], Literal[252], Literal[232]] = (254, 252, 232)
    YELLOW_100: tuple[Literal[254], Literal[249], Literal[195]] = (254, 249, 195)
    YELLOW_200: tuple[Literal[254], Literal[240], Literal[138]] = (254, 240, 138)
    YELLOW_300: tuple[Literal[253], Literal[224], Literal[71]] = (253, 224, 71)
    YELLOW_400: tuple[Literal[250], Literal[204], Literal[21]] = (250, 204, 21)
    YELLOW_500: tuple[Literal[234], Literal[179], Literal[8]] = (234, 179, 8)
    YELLOW_600: tuple[Literal[202], Literal[138], Literal[4]] = (202, 138, 4)
    YELLOW_700: tuple[Literal[161], Literal[98], Literal[7]] = (161, 98, 7)
    YELLOW_800: tuple[Literal[133], Literal[77], Literal[14]] = (133, 77, 14)
    YELLOW_900: tuple[Literal[113], Literal[63], Literal[18]] = (113, 63, 18)
    YELLOW_950: tuple[Literal[66], Literal[32], Literal[6]] = (66, 32, 6)

    LIME_050: tuple[Literal[247], Literal[254], Literal[231]] = (247, 254, 231)
    LIME_100: tuple[Literal[236], Literal[252], Literal[203]] = (236, 252, 203)
    LIME_200: tuple[Literal[217], Literal[249], Literal[157]] = (217, 249, 157)
    LIME_300: tuple[Literal[190], Literal[242], Literal[100]] = (190, 242, 100)
    LIME_400: tuple[Literal[163], Literal[230], Literal[53]] = (163, 230, 53)
    LIME_500: tuple[Literal[132], Literal[204], Literal[22]] = (132, 204, 22)
    LIME_600: tuple[Literal[101], Literal[163], Literal[13]] = (101, 163, 13)
    LIME_700: tuple[Literal[77], Literal[124], Literal[15]] = (77, 124, 15)
    LIME_800: tuple[Literal[63], Literal[98], Literal[18]] = (63, 98, 18)
    LIME_900: tuple[Literal[54], Literal[83], Literal[20]] = (54, 83, 20)
    LIME_950: tuple[Literal[26], Literal[46], Literal[5]] = (26, 46, 5)

    GREEN_050: tuple[Literal[240], Literal[253], Literal[244]] = (240, 253, 244)
    GREEN_100: tuple[Literal[220], Literal[252], Literal[231]] = (220, 252, 231)
    GREEN_200: tuple[Literal[187], Literal[247], Literal[208]] = (187, 247, 208)
    GREEN_300: tuple[Literal[134], Literal[239], Literal[172]] = (134, 239, 172)
    GREEN_400: tuple[Literal[74], Literal[222], Literal[128]] = (74, 222, 128)
    GREEN_500: tuple[Literal[34], Literal[197], Literal[94]] = (34, 197, 94)
    GREEN_600: tuple[Literal[22], Literal[163], Literal[74]] = (22, 163, 74)
    GREEN_700: tuple[Literal[21], Literal[128], Literal[61]] = (21, 128, 61)
    GREEN_800: tuple[Literal[22], Literal[101], Literal[52]] = (22, 101, 52)
    GREEN_900: tuple[Literal[20], Literal[83], Literal[45]] = (20, 83, 45)
    GREEN_950: tuple[Literal[5], Literal[46], Literal[22]] = (5, 46, 22)

    EMERALD_050: tuple[Literal[236], Literal[253], Literal[245]] = (236, 253, 245)
    EMERALD_100: tuple[Literal[209], Literal[250], Literal[229]] = (209, 250, 229)
    EMERALD_200: tuple[Literal[167], Literal[243], Literal[208]] = (167, 243, 208)
    EMERALD_300: tuple[Literal[110], Literal[231], Literal[183]] = (110, 231, 183)
    EMERALD_400: tuple[Literal[52], Literal[211], Literal[153]] = (52, 211, 153)
    EMERALD_500: tuple[Literal[16], Literal[185], Literal[129]] = (16, 185, 129)
    EMERALD_600: tuple[Literal[5], Literal[150], Literal[105]] = (5, 150, 105)
    EMERALD_700: tuple[Literal[4], Literal[120], Literal[87]] = (4, 120, 87)
    EMERALD_800: tuple[Literal[6], Literal[95], Literal[70]] = (6, 95, 70)
    EMERALD_900: tuple[Literal[6], Literal[78], Literal[59]] = (6, 78, 59)
    EMERALD_950: tuple[Literal[2], Literal[44], Literal[34]] = (2, 44, 34)

    TEAL_050: tuple[Literal[240], Literal[253], Literal[250]] = (240, 253, 250)
    TEAL_100: tuple[Literal[204], Literal[251], Literal[241]] = (204, 251, 241)
    TEAL_200: tuple[Literal[153], Literal[246], Literal[228]] = (153, 246, 228)
    TEAL_300: tuple[Literal[94], Literal[234], Literal[212]] = (94, 234, 212)
    TEAL_400: tuple[Literal[45], Literal[212], Literal[191]] = (45, 212, 191)
    TEAL_500: tuple[Literal[20], Literal[184], Literal[166]] = (20, 184, 166)
    TEAL_600: tuple[Literal[13], Literal[148], Literal[136]] = (13, 148, 136)
    TEAL_700: tuple[Literal[15], Literal[118], Literal[110]] = (15, 118, 110)
    TEAL_800: tuple[Literal[17], Literal[94], Literal[89]] = (17, 94, 89)
    TEAL_900: tuple[Literal[19], Literal[78], Literal[74]] = (19, 78, 74)
    TEAL_950: tuple[Literal[4], Literal[47], Literal[46]] = (4, 47, 46)

    CYAN_050: tuple[Literal[236], Literal[254], Literal[255]] = (236, 254, 255)
    CYAN_100: tuple[Literal[207], Literal[250], Literal[254]] = (207, 250, 254)
    CYAN_200: tuple[Literal[165], Literal[243], Literal[252]] = (165, 243, 252)
    CYAN_300: tuple[Literal[103], Literal[232], Literal[249]] = (103, 232, 249)
    CYAN_400: tuple[Literal[34], Literal[211], Literal[238]] = (34, 211, 238)
    CYAN_500: tuple[Literal[6], Literal[182], Literal[212]] = (6, 182, 212)
    CYAN_600: tuple[Literal[8], Literal[145], Literal[178]] = (8, 145, 178)
    CYAN_700: tuple[Literal[14], Literal[116], Literal[144]] = (14, 116, 144)
    CYAN_800: tuple[Literal[21], Literal[94], Literal[117]] = (21, 94, 117)
    CYAN_900: tuple[Literal[22], Literal[78], Literal[99]] = (22, 78, 99)
    CYAN_950: tuple[Literal[8], Literal[51], Literal[68]] = (8, 51, 68)

    SKY_050: tuple[Literal[240], Literal[249], Literal[255]] = (240, 249, 255)
    SKY_100: tuple[Literal[224], Literal[242], Literal[254]] = (224, 242, 254)
    SKY_200: tuple[Literal[186], Literal[230], Literal[253]] = (186, 230, 253)
    SKY_300: tuple[Literal[125], Literal[211], Literal[252]] = (125, 211, 252)
    SKY_400: tuple[Literal[56], Literal[189], Literal[248]] = (56, 189, 248)
    SKY_500: tuple[Literal[14], Literal[165], Literal[233]] = (14, 165, 233)
    SKY_600: tuple[Literal[2], Literal[132], Literal[199]] = (2, 132, 199)
    SKY_700: tuple[Literal[3], Literal[105], Literal[161]] = (3, 105, 161)
    SKY_800: tuple[Literal[7], Literal[89], Literal[133]] = (7, 89, 133)
    SKY_900: tuple[Literal[12], Literal[74], Literal[110]] = (12, 74, 110)
    SKY_950: tuple[Literal[8], Literal[47], Literal[73]] = (8, 47, 73)

    BLUE_050: tuple[Literal[239], Literal[246], Literal[255]] = (239, 246, 255)
    BLUE_100: tuple[Literal[219], Literal[234], Literal[254]] = (219, 234, 254)
    BLUE_200: tuple[Literal[191], Literal[219], Literal[254]] = (191, 219, 254)
    BLUE_300: tuple[Literal[147], Literal[197], Literal[253]] = (147, 197, 253)
    BLUE_400: tuple[Literal[96], Literal[165], Literal[250]] = (96, 165, 250)
    BLUE_500: tuple[Literal[59], Literal[130], Literal[246]] = (59, 130, 246)
    BLUE_600: tuple[Literal[37], Literal[99], Literal[235]] = (37, 99, 235)
    BLUE_700: tuple[Literal[29], Literal[78], Literal[216]] = (29, 78, 216)
    BLUE_800: tuple[Literal[30], Literal[64], Literal[175]] = (30, 64, 175)
    BLUE_900: tuple[Literal[30], Literal[58], Literal[138]] = (30, 58, 138)
    BLUE_950: tuple[Literal[23], Literal[37], Literal[84]] = (23, 37, 84)

    INDIGO_050: tuple[Literal[238], Literal[242], Literal[255]] = (238, 242, 255)
    INDIGO_100: tuple[Literal[224], Literal[231], Literal[255]] = (224, 231, 255)
    INDIGO_200: tuple[Literal[199], Literal[210], Literal[254]] = (199, 210, 254)
    INDIGO_300: tuple[Literal[165], Literal[180], Literal[252]] = (165, 180, 252)
    INDIGO_400: tuple[Literal[129], Literal[140], Literal[248]] = (129, 140, 248)
    INDIGO_500: tuple[Literal[99], Literal[102], Literal[241]] = (99, 102, 241)
    INDIGO_600: tuple[Literal[79], Literal[70], Literal[229]] = (79, 70, 229)
    INDIGO_700: tuple[Literal[67], Literal[56], Literal[202]] = (67, 56, 202)
    INDIGO_800: tuple[Literal[55], Literal[48], Literal[163]] = (55, 48, 163)
    INDIGO_900: tuple[Literal[49], Literal[46], Literal[129]] = (49, 46, 129)
    INDIGO_950: tuple[Literal[30], Literal[27], Literal[75]] = (30, 27, 75)

    VIOLET_050: tuple[Literal[245], Literal[243], Literal[255]] = (245, 243, 255)
    VIOLET_100: tuple[Literal[237], Literal[233], Literal[254]] = (237, 233, 254)
    VIOLET_200: tuple[Literal[221], Literal[214], Literal[254]] = (221, 214, 254)
    VIOLET_300: tuple[Literal[196], Literal[181], Literal[253]] = (196, 181, 253)
    VIOLET_400: tuple[Literal[167], Literal[139], Literal[250]] = (167, 139, 250)
    VIOLET_500: tuple[Literal[139], Literal[92], Literal[246]] = (139, 92, 246)
    VIOLET_600: tuple[Literal[124], Literal[58], Literal[237]] = (124, 58, 237)
    VIOLET_700: tuple[Literal[109], Literal[40], Literal[217]] = (109, 40, 217)
    VIOLET_800: tuple[Literal[91], Literal[33], Literal[182]] = (91, 33, 182)
    VIOLET_900: tuple[Literal[76], Literal[29], Literal[149]] = (76, 29, 149)
    VIOLET_950: tuple[Literal[46], Literal[16], Literal[101]] = (46, 16, 101)

    PURPLE_050: tuple[Literal[250], Literal[245], Literal[255]] = (250, 245, 255)
    PURPLE_100: tuple[Literal[243], Literal[232], Literal[255]] = (243, 232, 255)
    PURPLE_200: tuple[Literal[233], Literal[213], Literal[255]] = (233, 213, 255)
    PURPLE_300: tuple[Literal[216], Literal[180], Literal[254]] = (216, 180, 254)
    PURPLE_400: tuple[Literal[192], Literal[132], Literal[252]] = (192, 132, 252)
    PURPLE_500: tuple[Literal[168], Literal[85], Literal[247]] = (168, 85, 247)
    PURPLE_600: tuple[Literal[147], Literal[51], Literal[234]] = (147, 51, 234)
    PURPLE_700: tuple[Literal[126], Literal[34], Literal[206]] = (126, 34, 206)
    PURPLE_800: tuple[Literal[107], Literal[33], Literal[168]] = (107, 33, 168)
    PURPLE_900: tuple[Literal[88], Literal[28], Literal[135]] = (88, 28, 135)
    PURPLE_950: tuple[Literal[59], Literal[7], Literal[100]] = (59, 7, 100)

    FUCHSIA_050: tuple[Literal[253], Literal[244], Literal[255]] = (253, 244, 255)
    FUCHSIA_100: tuple[Literal[250], Literal[232], Literal[255]] = (250, 232, 255)
    FUCHSIA_200: tuple[Literal[245], Literal[208], Literal[254]] = (245, 208, 254)
    FUCHSIA_300: tuple[Literal[240], Literal[171], Literal[252]] = (240, 171, 252)
    FUCHSIA_400: tuple[Literal[232], Literal[121], Literal[249]] = (232, 121, 249)
    FUCHSIA_500: tuple[Literal[217], Literal[70], Literal[239]] = (217, 70, 239)
    FUCHSIA_600: tuple[Literal[192], Literal[38], Literal[211]] = (192, 38, 211)
    FUCHSIA_700: tuple[Literal[162], Literal[28], Literal[175]] = (162, 28, 175)
    FUCHSIA_800: tuple[Literal[134], Literal[25], Literal[143]] = (134, 25, 143)
    FUCHSIA_900: tuple[Literal[112], Literal[26], Literal[117]] = (112, 26, 117)
    FUCHSIA_950: tuple[Literal[74], Literal[4], Literal[78]] = (74, 4, 78)

    PINK_050: tuple[Literal[253], Literal[242], Literal[248]] = (253, 242, 248)
    PINK_100: tuple[Literal[252], Literal[231], Literal[243]] = (252, 231, 243)
    PINK_200: tuple[Literal[251], Literal[207], Literal[232]] = (251, 207, 232)
    PINK_300: tuple[Literal[249], Literal[168], Literal[212]] = (249, 168, 212)
    PINK_400: tuple[Literal[244], Literal[114], Literal[182]] = (244, 114, 182)
    PINK_500: tuple[Literal[236], Literal[72], Literal[153]] = (236, 72, 153)
    PINK_600: tuple[Literal[219], Literal[39], Literal[119]] = (219, 39, 119)
    PINK_700: tuple[Literal[190], Literal[24], Literal[93]] = (190, 24, 93)
    PINK_800: tuple[Literal[157], Literal[23], Literal[77]] = (157, 23, 77)
    PINK_900: tuple[Literal[131], Literal[24], Literal[67]] = (131, 24, 67)
    PINK_950: tuple[Literal[80], Literal[7], Literal[36]] = (80, 7, 36)

    ROSE_050: tuple[Literal[255], Literal[241], Literal[242]] = (255, 241, 242)
    ROSE_100: tuple[Literal[255], Literal[228], Literal[230]] = (255, 228, 230)
    ROSE_200: tuple[Literal[254], Literal[205], Literal[211]] = (254, 205, 211)
    ROSE_300: tuple[Literal[253], Literal[164], Literal[175]] = (253, 164, 175)
    ROSE_400: tuple[Literal[251], Literal[113], Literal[133]] = (251, 113, 133)
    ROSE_500: tuple[Literal[244], Literal[63], Literal[94]] = (244, 63, 94)
    ROSE_600: tuple[Literal[225], Literal[29], Literal[72]] = (225, 29, 72)
    ROSE_700: tuple[Literal[190], Literal[18], Literal[60]] = (190, 18, 60)
    ROSE_800: tuple[Literal[159], Literal[18], Literal[57]] = (159, 18, 57)
    ROSE_900: tuple[Literal[136], Literal[19], Literal[55]] = (136, 19, 55)
    ROSE_950: tuple[Literal[76], Literal[5], Literal[25]] = (76, 5, 25)
    
    
TAILWIND_COLORS = TAILWIND_COLORS_HEX
"""Alias for TAILWIND_COLORS_HEX."""
