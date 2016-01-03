import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    // Preload globally interesting data on load
    return Ember.RSVP.hash({
      'servers': this.store.findAll('server'),
      'jobs': this.store.findAll('job'),
      'races': this.store.findAll('race'),
      'grand_companies': this.store.findAll('grand-company'),
      'minions': this.store.findAll('minion'),
      'mounts': this.store.findAll('mount'),
    });
  }
});
