"use strict";

ckan.module('iframeHelper', function ($, _) {
  return {
    initialize: function() {
      alert(this.el);
      alert(this.el.attr("src"));
    }
  };
});
