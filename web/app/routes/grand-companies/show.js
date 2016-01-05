import Ember from 'ember';

export default Ember.Route.extend({
  model: function(params) {
    return this.store.queryRecord('grand-company', { slug: params.gc_slug });
  },
  serialize: function(model) {
    return { gc_slug: model.get('slug') };
  },
});
