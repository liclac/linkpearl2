import Ember from 'ember';

export default Ember.Controller.extend({
  queryParams: ['page'],
  page: 1,
  resetScroll: Ember.observer('page', function() {
    window.scrollTo(0, 0);
  }),
});
