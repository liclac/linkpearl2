import Ember from 'ember';

export default Ember.Component.extend({
  page: 1,
  model: null,
  resetScroll: Ember.observer('page', function() {
    window.scrollTo(0, 0);
  }),
});
