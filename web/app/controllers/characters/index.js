import Ember from 'ember';

export default Ember.Controller.extend({
  queryParams: ['page', 'search', 'race', 'clan', 'gender', 'server'],
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

  gender: null,
  uiGender: Ember.computed('gender', function() {
    return this.get('gender') ? this.get('genders')[this.get('gender') + 1] : null;
  }),

  server: null,
  uiServer: Ember.computed('server', function() {
    return this.get('server') ? this.store.peekRecord('server', this.get('server')) : null;
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
  genders: [
    { id: 1, name: "Male" },
    { id: 2, name: "Female" },
  ],
  servers: Ember.computed(function() {
    return this.store.peekAll('server');
  }),

  actions: {
    filter: function() {
      this.set('search', this.get('uiSearch'));
      this.set('race', this.get('uiRace.id'));
      this.set('clan', this.get('uiClan.id'));
      this.set('gender', this.get('uiGender.id'));
      this.set('server', this.get('uiServer.id'));
    },
    clear: function() {
      this.set('uiSearch', '');
      this.set('uiRace', null);
      this.set('uiClan', null);
      this.set('uiGender', null);
      this.set('uiServer', null);
      this.send('filter');
    },
  },
});
