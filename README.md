# PromptVault

**PromptVault** is a tiny, zero‑dependency helper class for keeping reusable
prompt templates in memory and filling them with runtime values.  Templates
use double‑braces (`{{variable}}`) to mark the parts that should be replaced.

---

## Installation

```shell
pip install promptvault        
```

---

## Quick‑start

```python
from promptvault import PromptVault 

pv = PromptVault()
```

### 1.  Add a template

```python
pv.add({
    "name": "blog-post-generator",
    "prompt": (
        "Write a detailed blog post about {{topic}}, aimed at {{audience}}, "
        "in a {{tone}} tone."
    )
})
```

### 2.  Inspect the raw template (no inputs)

```python
pv.get("blog-post-generator")
```
Output:
```
{
    'name': 'blog-post-generator',
    'prompt': 'Write a detailed blog post about {{topic}}, aimed at {{audience}}, in a {{tone}} tone.',
    'variables': ['topic', 'audience', 'tone']
}
```

### 3.  Fill the template with data

```python
filled = pv.get(
    name="blog-post-generator",
    inputs={
        "topic": "AI in Healthcare",
        "audience": "health‑care professionals",
        "tone": "professional"
    }
)

```
Output:
```
{
    'name': 'blog-post-generator',
    'prompt': 'Write a detailed blog post about AI in Healthcare, aimed at health‑care professionals, in a professional tone.',
    'variables': ['topic', 'audience', 'tone']
}
```


