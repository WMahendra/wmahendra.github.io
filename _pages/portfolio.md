---
layout: archive
title: "Projects"
permalink: /portfolio/
author_profile: true
---

{% include base_path %}

Work is grouped into research, professional application, and shorter technical
explorations. Each project page describes the problem, the data and method, my own
contribution, and the limitations.

{% assign projects = site.portfolio | sort: "date" | reverse %}
{% assign featured = projects | where: "featured", true %}
{% assign research = projects | where: "category", "research" %}
{% assign professional = projects | where: "category", "professional" %}
{% assign technical = projects | where: "category", "technical" %}

{% comment %} Sections render only when they contain a project. {% endcomment %}

{% if featured.size > 0 %}
<h2>Featured work</h2>
{% for post in featured %}
  {% include project-card.html %}
{% endfor %}
{% endif %}

{% if research.size > 0 %}
<h2>Research &amp; publications</h2>
<p>Work based on research, theses and peer-reviewed publications.</p>
{% for post in research %}
  {% include project-card.html %}
{% endfor %}
{% endif %}

{% if professional.size > 0 %}
<h2>Professional &amp; applied work</h2>
<p>Applied geospatial projects delivered in a professional setting.</p>
{% for post in professional %}
  {% include project-card.html %}
{% endfor %}
{% endif %}

{% if technical.size > 0 %}
<h2>Technical explorations</h2>
<p>Shorter, code-oriented experiments in remote sensing and geospatial analysis.</p>
{% for post in technical %}
  {% include project-card.html %}
{% endfor %}
{% endif %}
