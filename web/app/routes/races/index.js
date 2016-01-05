import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    let adapter = this.store.adapterFor('race');
    let baseURL = adapter.get('host') + '/' + adapter.get('namespace');
    return Ember.RSVP.hash({
      'races': this.store.findAll('race'),
      'stats': Ember.$.getJSON(baseURL + '/races/stats'),
    });
  },
});
