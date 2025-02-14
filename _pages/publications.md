---
layout: single
title: Selected Publications
permalink: /publications/
---

A full and current list of my publications can be found on my google scholar profile [here](https://scholar.google.com/citations?user=8-FI_t0AAAAJ&hl=en).
**Bolded names** indicate equal contribution.

{% assign sorted_refs = site.data.references | sort: "year" | reverse %}
{% for item in sorted_refs %}
- {{item.author}}, *{{item.title}}*, {{item.venue}}, {{item.year}}.
{% endfor %}
