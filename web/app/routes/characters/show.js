import Ember from 'ember';

export default Ember.Route.extend({
  model: function(params) {
    return this.store.queryRecord('character', { lodestone_id: params.character_lid });
  },
  serialize: function(model) {
    return { character_lid: model.get('lodestone_id') };
  },
});
