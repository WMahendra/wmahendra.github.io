---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A list of all the pages and entries found on this site. For robots, an [XML version]({{ base_path }}/sitemap.xml) is also available.

<h2>Pages</h2>
{% for post in site.pages %}
  {% unless post.sitemap == false %}
  {% include archive-single.html %}
  {% endunless %}
{% endfor %}

{% for collection in site.collections %}
{% unless collection.output == false or collection.label == "posts" %}
  <h2>{{ collection.label | capitalize }}</h2>
  {% for post in collection.docs %}
    {% include archive-single.html %}
  {% endfor %}
{% endunless %}
{% endfor %}
