import Ember from 'ember';
import RouteMixin from 'ember-cli-pagination/remote/route-mixin';

export default Ember.Route.extend(RouteMixin, {
  perPage: 100,
  queryParams: {
    search: { refreshModel: true },
    race: { refreshModel: true },
  },
  resetController: function(controller, isExiting/*, transition*/) {
    if (isExiting) {
      controller.set('page', 1);
    }
  },
  model: function(params) {
    return this.findPaged('character', params);
  }
});
