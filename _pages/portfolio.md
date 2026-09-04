---
layout: archive
title: "Projects"
permalink: /portfolio/
author_profile: true
---

{% include base_path %}

Selected work, each page describing the problem, the data and method, my own
contribution, what the results were, and where the approach falls short.

{% assign projects = site.portfolio | sort: "date" | reverse %}
{% for post in projects %}
  {% include archive-single.html %}
{% endfor %}
