(function() {
  Vue.component('section-header', {
    template: '<h2>Header</h2>'
  });
  let comp1 = {
    template: '<div>Content 1</div>'
  };
  let comp2 = {
    template: '<div>Content 2</div>'
  };
  let footer = {
    template: '<p><b>Footer</b></p>'
  }
  new Vue({
    el: '#app1',
    components: {
      'section-content': comp1,
      'section-footer': footer
    }
  });
  new Vue({
    el: '#app2',
    components: {
      'section-content': comp2
    }
  })
})();