import Ember from 'ember';

export default Ember.Route.extend({
  model: function(params) {
    return this.store.queryRecord('server', { slug: params.server_slug });
  },
  serialize: function(model) {
    return { server_slug: model.get('slug') };
  },
});
