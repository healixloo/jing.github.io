---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

<iframe src="https://healixloo.github.io/jing.github.io/files/2024-07-27-publications.html" style="width: 100%; height: 1000px; border: none;">
  Your browser does not support iframes. If you are seeing this message, it means the iframe content could not be loaded.
</iframe>


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
