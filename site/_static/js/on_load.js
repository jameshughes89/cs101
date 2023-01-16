$(document).ready(function() {
    // Remove "Build with Sphinx" text in the footer:
    var elem = $("footer div[role='contentinfo']").get(0);
    while (elem.nextSibling)
      elem.nextSibling.remove();
  
    // Code block header:
    var $highlight = $("div.rst-content div.highlight");
    $highlight.prepend("<div class='mac-header'><span class='dot red'></span><span class='dot yellow'></span><span class='dot green'></span><span class='copy fa fa-clipboard' title='Copy to clipboard'></span></div>");
  
    // Copy text in code blocks:
    $highlight.find('span.copy').click(function() {
      navigator.clipboard.writeText($(this).parent().parent().text().slice(0, -1));
    });
  


  });

