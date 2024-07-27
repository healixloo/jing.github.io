---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on my <a href="{{site.author.googlescholar}}">Google Scholar</a>.</div>
{% endif %}

<iframe src="https://healixloo.github.io/jing.github.io/files/2024-07-27-publications.html" style="width: 100%; height: 1000px; border: none;">
  Your browser does not support iframes. If you are seeing this message, it means the iframe content could not be loaded.
</iframe>

<div id="embedded-content">Loading...</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    fetch('https://healixloo.github.io/jing.github.io/files/2024-07-27-publications.html')
      .then(response => response.text())
      .then(html => {
        document.getElementById('embedded-content').innerHTML = html;
      })
      .catch(error => {
        console.error('Error fetching the HTML content:', error);
        document.getElementById('embedded-content').innerText = 'Failed to load content.';
      });
  });
</script>

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
