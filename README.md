# Python Tailwind Colors

Use the default color palette from TailwindCSS (https://tailwindcss.com/docs/customizing-colors) in your python code for plotting, image generation, etc..

<br/>

**Installation:**

```bash
pip install tailwind_colors
# or
pdm add tailwind_colors
# or
uv add tailwind_colors
# or
poetry add tailwind_colors
```

<br/>

**Usage:**

```python
from tailwind_colors import TAILWIND_COLORS_HEX, TAILWIND_COLORS_RGB

print(TAILWIND_COLORS_HEX.FUCHSIA_600)  # prints '#c026d3'
print(TAILWIND_COLORS_RGB.FUCHSIA_600)  # prints (192, 38, 211)
print(TAILWIND_COLORS_HEX.RAINBOW_450)  # prints ['#f35a5a', '#fa8229', ...
```

You can also use the short import variants:

```python
from tailwind_colors import TCH, TCR

print(TCH.FUCHSIA_600)  # prints '#c026d3'
print(TCR.FUCHSIA_600)  # prints (192, 38, 211)
print(TCH.RAINBOW_450)  # prints ['#f35a5a', '#fa8229', ...
