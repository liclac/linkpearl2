import Ember from 'ember';

export default Ember.Controller.extend({
  queryParams: ['page', 'search', 'race'],
  page: 1,

  search: '',
  uiSearch: Ember.computed('search', function() {
    return this.get('search');
  }),

  race: null,
  uiRace: Ember.computed('race', function() {
    return this.get('race') ? this.store.peekRecord('race', this.get('race')) : null;
  }),

  races: Ember.computed(function() {
    return this.store.peekAll('race');
  }),
  actions: {
    filter: function() {
      this.set('search', this.get('uiSearch'));
      this.set('race', this.get('uiRace.id'));
    }
  },
});
