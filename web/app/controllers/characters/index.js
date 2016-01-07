import Ember from 'ember';

export default Ember.Controller.extend({
  queryParams: ['page', 'search', 'race'],
  page: 1,

  search: '',
  uiSearch: '',

  race: null,
  uiRace: null,

  races: Ember.computed(function() {
    return this.store.peekAll('race');
  }),
  actions: {
    filter: function() {
      this.set('search', this.get('uiSearch'));
      this.set('race', this.get('uiRace.id'));
    }
  },
  updateUI: Ember.observer('search', 'race', function() {
    this.set('uiSearch', this.get('search'));
    this.set('uiRace', this.store.peekRecord('race', this.get('race')));
  }),
});
