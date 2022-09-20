---
tags: [dailynote]
cssclass: []
---

Stats: [[!vault stats]]

Today's weather in <% tp.user.weather() %>

[[<% tp.date.yesterday("YYYY-MM-DD") %>]] 👈 👉 [[<% tp.date.tomorrow("YYYY-MM-DD") %>]]

# {{date:dddd, D MMMM YYYY}}

## Today's notes

```dataview
list
from [[{{date:YYYY-MM-DD}}]]
where tag != "dailynote"
```

## Today's thoughts
