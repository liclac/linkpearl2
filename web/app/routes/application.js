import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    // Preload globally interesting data on load
    return Ember.RSVP.hash({
      'servers': this.store.findAll('server'),
    });
  }
});
