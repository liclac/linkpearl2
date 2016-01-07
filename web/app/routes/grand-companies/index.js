import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    let adapter = this.store.adapterFor('grand-company');
    let baseURL = adapter.get('host') + '/' + adapter.get('namespace');
    return Ember.RSVP.hash({
      'gcs': this.store.findAll('grand-company'),
      'stats': Ember.$.getJSON(baseURL + '/grand-companies/stats'),
    });
  }
});
