import Ember from 'ember';

export default Ember.Controller.extend({
  sortedServersBy: ['num_characters:desc', 'name'],
  sortedServers: Ember.computed.sort('model', 'sortedServersBy'),
  chartData: Ember.computed('model', function() {
    return this.get('model').map(function(server) {
      return { value: server.get('num_characters'), label: server.get('name') };
    });
  }),
});
