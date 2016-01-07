import Ember from 'ember';
import RouteMixin from 'ember-cli-pagination/remote/route-mixin';

export default Ember.Route.extend(RouteMixin, {
  perPage: 100,
  resetController: function(controller, isExiting/*, transition*/) {
    if (isExiting) {
      controller.set('page', 1);
    }
  },
  model: function() {
    return this.findPaged('character', {});
  },
});
