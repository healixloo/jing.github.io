---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

<div id="embedded-content">Loading...</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    fetch('https://healixloo.github.io/jing.github.io/files/2024-07-27-publications.html')
      .then(response => {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error('Failed to load content');
        }
      })
      .then(html => {
        document.getElementById('embedded-content').innerHTML = html;
      })
      .catch(error => {
        console.error('Error fetching the HTML content:', error);
        document.getElementById('embedded-content').innerText = 'Failed to load content.';
      });
  });
</script>
