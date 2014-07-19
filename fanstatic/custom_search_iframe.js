"use strict";

ckan.module('custom_search_iframe', function ($, _) {
   return {
     initialize: function() {
       alert(this.el);
       alert(this.el.src);
     }
   };
});
