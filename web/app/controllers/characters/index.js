import Ember from 'ember';

export default Ember.Controller.extend({
  queryParams: ['page', 'search'],
  page: 1,
  search: '',
  actions: {
    filter: function() {
      this.set('search', this.get('uiSearch'));
    }
  },
  updateUI: Ember.observer('search', function() {
    this.set('uiSearch', this.get('search'));
  }),
});
