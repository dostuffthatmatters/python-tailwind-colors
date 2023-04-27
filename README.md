# Python Tailwind Colors

Use the default color palette from TailwindCSS (https://tailwindcss.com/docs/customizing-colors) in your python code for plotting, image generation, etc..

<br/>

**Installation:**

```bash
poetry add tailwind_colors
# or
pip install tailwind_colors
```

<br/>

**Usage:**

```python
from tailwind_colors import TAILWIND_COLORS_HEX, TAILWIND_COLORS_RGB

print(TAILWIND_COLORS_HEX.FUCHSIA_600)  # prints '#c026d3'
print(TAILWIND_COLORS_RGB.FUCHSIA_600)  # prints (192, 38, 211)
```
