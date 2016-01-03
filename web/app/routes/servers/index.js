import Ember from 'ember';
import ENV from 'linkpearl/config/environment';

export default Ember.Route.extend({
  model: function() {
    return this.store.findAll('server');
  }
});
