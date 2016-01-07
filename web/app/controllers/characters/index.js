import Ember from 'ember';

export default Ember.Controller.extend({
  queryParams: ['page', 'search', 'race', 'clan'],
  page: 1,

  search: '',
  uiSearch: Ember.computed('search', function() {
    return this.get('search');
  }),

  race: null,
  uiRace: Ember.computed('race', function() {
    return this.get('race') ? this.store.peekRecord('race', this.get('race')) : null;
  }),

  clan: null,
  uiClan: Ember.computed('clan', function() {
    return this.get('clan') ? this.get('clans')[this.get('clan') + 1] : null;
  }),

  races: Ember.computed(function() {
    return this.store.peekAll('race');
  }),
  clans: Ember.computed('uiRace', function() {
    return [
      { id: 1, name: this.get('uiRace.clan_1') },
      { id: 2, name: this.get('uiRace.clan_2') },
    ];
  }),

  actions: {
    filter: function() {
      this.set('search', this.get('uiSearch'));
      this.set('race', this.get('uiRace.id'));
      this.set('clan', this.get('uiClan.id'));
    }
  },
});
