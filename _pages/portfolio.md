---
layout: archive
title: "Projects"
permalink: /portfolio/
author_profile: true
---

{% include base_path %}

{% assign projects = site.portfolio | sort: "date" | reverse %}
{% assign featured = projects | where: "featured", true %}
{% assign research = projects | where: "category", "research" %}
{% assign professional = projects | where: "category", "professional" %}
{% assign technical = projects | where: "category", "technical" %}

{% comment %} Sections render only when they contain a project. {% endcomment %}

{% if featured.size > 0 %}
<h2 class="section-label">Featured work</h2>
<div class="pcard-grid">{% for post in featured %}{% include project-card.html %}{% endfor %}</div>
{% endif %}

{% if research.size > 0 %}
<h2 class="section-label">Research &amp; publications</h2>
<div class="pcard-grid">{% for post in research %}{% include project-card.html %}{% endfor %}</div>
{% endif %}

{% if professional.size > 0 %}
<h2 class="section-label">Professional &amp; applied work</h2>
<div class="pcard-grid">{% for post in professional %}{% include project-card.html %}{% endfor %}</div>
{% endif %}

{% if technical.size > 0 %}
<h2 class="section-label">Technical explorations</h2>
<div class="pcard-grid">{% for post in technical %}{% include project-card.html %}{% endfor %}</div>
{% endif %}
