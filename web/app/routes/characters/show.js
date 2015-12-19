import Ember from 'ember';

export default Ember.Route.extend({
  model: function(params) {
    return this.store.find('character', params.character_id);
  }
});
