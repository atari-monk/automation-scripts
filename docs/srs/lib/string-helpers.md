## String Helpers

`lib/string-helpers.py`

### get_page_title

- function `get_page_title(repository_name: str)->str`
- assume input:
  - lower letters
  - kebab-case
  - for example: `automation-scripts`
- return output:
  - input with upper first letters
  - space as delimiter
  - for example: `Automation Scripts`
