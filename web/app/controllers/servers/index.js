import Ember from 'ember';

export default Ember.Controller.extend({
  sortedServersBy: ['population:desc', 'name'],
  sortedServers: Ember.computed.sort('model', 'sortedServersBy'),
  populationData: Ember.computed('model', function() {
    return this.get('model').map(function(server) {
      return { value: server.get('population'), label: server.get('name') };
    });
  }),
});
